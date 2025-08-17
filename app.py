from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os


from agents.summary_agent import summarize_with_chain  

load_dotenv()

app = Flask(__name__)


app.config["MAIL_SERVER"]   = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"]     = int(os.getenv("MAIL_PORT", "587"))
app.config["MAIL_SENDER"]   = os.getenv("MAIL_SENDER")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"]  = os.getenv("MAIL_USE_TLS", "True").lower() == "true"
app.config["MAIL_USE_SSL"]  = os.getenv("MAIL_USE_SSL", "False").lower() == "true"

mail = Mail(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json(silent=True) or {}
        transcript = data.get("transcript", "").strip()
        instruction = data.get("instruction", "").strip()
        if not transcript or not instruction:
            return jsonify({"error": "Missing transcript or instruction"}), 400

        summary = summarize_with_chain(transcript, instruction)

        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500

@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        data = request.get_json(silent=True) or {}
        recipients_field = data.get("recipients", "").strip()
        subject = data.get("subject", "Meeting Summary").strip() or "Meeting Summary"
        body = data.get("body", "").strip()

        if not recipients_field or not body:
            return jsonify({"error": "Missing recipients or body"}), 400

        recipients = [r.strip() for r in recipients_field.split(",") if r.strip()]
        if not recipients:
            return jsonify({"error": "No valid recipient addresses"}), 400

        msg = Message(subject=subject,
                      sender=app.config["MAIL_SENDER"],
                      recipients=recipients,
                      body=body)
        mail.send(msg)
        return jsonify({"message": "Email sent successfully."})
    except Exception as e:
        return jsonify({"error": f"Email send error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

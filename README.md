# 🤖 AI Meeting Notes Summarizer

This project is a simple web application that uses a large language model to summarize meeting transcripts and allows you to email the generated summary.

### 📜 How to Use This Project

This repository provides a simple, AI-powered meeting notes summarizer using a Flask backend and a basic HTML frontend. The application allows you to upload a meeting transcript, provide a custom summarization instruction, and then generate and email the summary.

#### 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.10+**
* **Git** (for cloning the repository)

#### 🚀 Getting Started

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Bhavesh-Mankar51/AI-Powered-meeting-notes-summarizer.git
    ```

2.  **Set up the virtual environment**:
    It's best practice to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies**:
    Install all the necessary Python libraries from the `requirements.txt` file (you'll need to create this file yourself with the dependencies).
    ```bash
    pip install Flask python-dotenv Flask-Mail langchain-openai langchain-core langchainhub
    ```

4.  **Configure environment variables**:
    Create a file named `.env` in the root directory of the project and add your API keys and email credentials.

    ```bash
    # OpenAI API Key for summarization
    OPENAI_API_KEY="your_openai_api_key_here"

    # Flask-Mail configuration for sending emails
    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME="your_email@gmail.com"
    MAIL_PASSWORD="your_app_password"
    MAIL_SENDER="your_email@gmail.com"
    ```
    🚨 **Note:** For Gmail, you'll need to generate an **App Password** as your `MAIL_PASSWORD` because regular passwords are not secure for this purpose. You can do this in your Google Account settings under Security > 2-Step Verification > App Passwords.

#### ▶️ Running the Application

Once everything is configured, you can start the Flask server.

1.  **Run the application**:
    ```bash
    python app.py
    ```
2.  **Access the web app**:
    Open your web browser and navigate to `http://127.0.0.1:5000`. You will see the interface to upload a 
    transcript, generate a summary, and send an email. 







#### How to Contribute

We welcome contributions! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  **Fork** the repository.
2.  Create a new branch: `git checkout -b feature/your-feature-name`
3.  Make your changes and commit them with a descriptive message: `git commit -m 'feat: Add new summarization model'`
4.  Push to your fork: `git push origin feature/your-feature-name`
5.  Open a **Pull Request** to the `main` branch of this repository.


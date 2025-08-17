from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain import hub

from tools.tools import pass_through

load_dotenv()

def summarize_with_chain(transcript: str, instruction: str) -> str:
    """
    Simple, single-call summarization using a prompt stuffed with the transcript.
    This is the most robust and fastest path.
    """
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    prompt = ChatPromptTemplate.from_template(
        "You are an expert meeting notes assistant.\n"
        "Follow the user's instruction strictly.\n\n"
        "Instruction:\n{instruction}\n\n"
        "Transcript:\n{transcript}\n\n"
        "Return only the final summary."
    )

    prompt_str = prompt.format(instruction=instruction, transcript=transcript)
    result = llm.invoke(prompt_str).content
    if isinstance(result, str):
        return result
    elif isinstance(result, list):
        return " ".join(str(item) for item in result)
    else:
        return str(result)

def summarize_with_agent(transcript: str, instruction: str) -> str:
    """
    Demonstrates a ReAct agent mirroring your create_react_agent usage.
    """
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    tools_for_agent = [
        Tool(
            name="PassThrough",
            func=pass_through,
            description="Echo utility to return any provided text as-is."
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=False)

    result = agent_executor.invoke({
        "input": (
            "Summarize the following transcript per the instruction. "
            "Use tools if needed.\n\n"
            f"Instruction: {instruction}\n\nTranscript:\n{transcript}"
        )
    })
    return result.get("output", "").strip()

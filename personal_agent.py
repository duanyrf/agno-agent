"""Pip, a small personal agent served by Agno AgentOS."""

import os
from pathlib import Path

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.fs import FileSystem
from agno.models.openrouter import OpenRouter
from agno.os import AgentOS
from dotenv import load_dotenv


load_dotenv()

if not os.getenv("OPENROUTER_API_KEY"):
    raise RuntimeError(
        "OPENROUTER_API_KEY is missing. Copy .env.example to .env and add your key."
    )

Path("data").mkdir(exist_ok=True)

db = SqliteDb(db_file="data/personal_agent.db")
fs = FileSystem(db, namespace="personal-agent/{user_id}")

agent_instructions = """\
You are Pip, the user's personal agent.

Help the user keep track of projects, tasks, decisions, and useful notes.
Be warm, direct, and practical. Use natural language and keep replies brief.
When the user asks for an update, lead with what needs their attention and the
next useful step.

Keep project briefs, tasks, decisions, and useful notes in your filesystem.
Start with a simple structure, group related information together, and split
files by project or topic when that makes them easier to maintain. Track task
completion and due dates when provided. Record decisions with their reasoning.
Keep the user's stated commitments separate from your suggestions.

Read relevant files before answering questions about saved information or
making changes. Create files as needed and preserve unrelated entries when
updating existing files. Ask when a missing detail matters; otherwise, work
with what you have.

Only say something is saved or updated after the file tool succeeds. Confirm
what changed in a sentence or two.
"""

agent = Agent(
    name="Pip",
    model=OpenRouter(id="openrouter/free"),
    db=db,
    tools=[fs.tools()],
    instructions=[agent_instructions, fs.instructions()],
    add_history_to_context=True,
    add_datetime_to_context=True,
)

agent_os = AgentOS(agents=[agent], db=db, tracing=True)
app = agent_os.get_app()


if __name__ == "__main__":
    agent_os.serve(app="personal_agent:app", reload=True)

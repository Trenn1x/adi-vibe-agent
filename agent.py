#!/usr/bin/env python3
import sys, os, textwrap
from dotenv import load_dotenv
# 💡 NEW import ↓
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage   # unchanged

load_dotenv()

# Switch to the chat-style Ollama wrapper
LLM = ChatOllama(model="mistral", temperature=0.3)

def ask(prompt_str):
    """Send prompt_str to the model and return the reply text."""
    msgs = [
        SystemMessage(content="You are a helpful expert writer."),
        HumanMessage(content=prompt_str)
    ]
    return LLM.invoke(msgs).content.strip()         # .invoke = future-proof
def main(path):
    with open(path, "r") as f:
        job = f.read()

    summary_prompt = f"""Summarize this job post for a senior GenAI engineer in 6-8 bullet points. 
Focus on mission, first-90-day goals, daily stack, and success metrics.

JOB POST:
{job}"""
    email_prompt = f"""You are the VP of Edge AI at Analog Devices. 
Draft a 150-word intro email to candidates, written in your confident, visionary voice, 
inviting them to explore the Vibe Coder-in-Residence role. 
Highlight: (1) daily shipping culture, (2) digital-twin roadmap, (3) expectation to work CA timezone."""

    summary = ask(summary_prompt)
    email   = ask(email_prompt)

    with open("summary.txt", "w") as f: f.write(summary)
    with open("intro_email.txt", "w") as f: f.write(email)

    print("\n=== Summary ===\n", summary, "\n")
    print("=== Intro Email ===\n", email)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py job_post.txt"); sys.exit(1)
    main(sys.argv[1])


# ADI Vibe Coder-in-Residence Demo Agent

**What it does**  
1. Summarizes any job post in compact bullets  
2. Drafts an intro email in the VP’s voice  
Outputs land in `summary.txt` and `intro_email.txt`.

**Stack**  
- Python · LangChain-Ollama · Local `mistral` model via [Ollama](https://ollama.com/)  
- CLI for speed; swap in OpenAI/HF by editing `agent.py`

**How to run**

```bash
git clone https://github.com/Trenn1x/adi-vibe-agent.git
cd adi-vibe-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
ollama run mistral   # first time pulls model, then keeps running
python agent.py job_post.txt

**Architecture choices**

| Decision | Rationale |
|----------|-----------|
| Local LLM (Mistral) | Zero cloud cost / works without OpenAI quota |
| LangChain-Ollama | Chat interface → easy message structuring |
| Single-file CLI | Fast to audit & extend (wrap in Teams bot on Day 2) |

Made by Thomas Verdier – more projects on https://github.com/Trenn1x

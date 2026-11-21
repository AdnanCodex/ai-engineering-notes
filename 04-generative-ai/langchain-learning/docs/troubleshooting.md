# Troubleshooting

| Problem | Fix |
|---------|-----|
| `OPENAI_API_KEY` not found | Copy `.env.example` to `.env`, add the key, restart the kernel |
| `python: can't open file` | Run scripts from the repo root, e.g. `python 02_Prompts/1_prompt_template.py` |
| `ModuleNotFoundError` | Activate `.venv` and run `pip install -r requirements.txt` |
| `get_transcript` attribute error (notebook 11) | Keep `youtube-transcript-api<1.0` as pinned |
| `create_react_agent` / `hub` import error (notebook 13) | Keep `langchain<1.0` as pinned and install `langchainhub` |
| `KeyError: WEATHERSTACK_API_KEY` | Add a free Weatherstack key to `.env` |
| DuckDuckGo rate-limit errors | Wait a minute and retry |
| Chroma "collection already exists" or duplicates | Delete `data/chroma_db` (`make clean`) |
| `RateLimitError` / quota | Check billing and usage on your OpenAI account |

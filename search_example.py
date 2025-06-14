from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = ddgs.text("open source LLM", max_results=5)
    for r in results:
        print(r["title"], "-", r["href"])

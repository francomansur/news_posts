import os, requests

language: str = "pt"           
page_size: int = 4             
sort_by: str = "publishedAt"  

def buscar_manchetes(theme: str):
    """
    Retorna até 5 artigos mais recentes da NewsAPI para o tema dado.
    """
    if not theme or not theme.strip():
        raise ValueError("Informe um tema para a busca (theme).")

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise EnvironmentError("NEWS_API_KEY não encontrada.")

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": theme,
        "language": language,
        "pageSize": page_size,
        "sortBy": sort_by,
        "apiKey": api_key,
    }

    resp = requests.get(url, params=params, timeout=20)
    resp.raise_for_status()
    data = resp.json()

    articles = data.get("articles", [])
    if not articles:
        raise LookupError(f"Nenhuma manchete encontrada para: {theme!r}")

    return articles 

# openrouter_utils.py
import os
import requests
import trafilatura
import json
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-3.5-turbo"
api_key = os.getenv("OPENROUTER_KEY")

def gerar_elementos(article_url: str) -> tuple[str, str, str]:
    """
    Lê a URL do artigo, extrai o texto e retorna (kicker, headline, legenda) para o post.
    - Kicker: 3 a 6 palavras em CAIXA ALTA (linha acima da headline).
    - Headline: pt-BR, curta, no máximo 20 palavras, CAIXA ALTA.
    - Legenda: pt-BR, no máximo 1500 caracteres.
    """
    if not isinstance(article_url, str) or not article_url.strip():
        raise ValueError("article_url vazio.")

    # Extrair texto do artigo
    r = requests.get(article_url.strip(), timeout=(5, 30), headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    texto = trafilatura.extract(r.text, include_images=False, include_links=False)
    if not texto:
        raise RuntimeError("Não foi possível extrair o texto do artigo.")
    texto = texto.strip()[:12000]

    # Prompt para pedir KICKER + HEADLINE + LEGENDA em JSON
    system = (
        'Responda ESTRITAMENTE em JSON com os campos {"kicker": string, "headline": string, "legenda": string}. '
        "kicker: 3–6 palavras em CAIXA ALTA, sem emojis/hashtags e sem pontuação final. "
        "headline: pt-BR, jornalística, clara e objetiva, no máximo 20 palavras, em CAIXA ALTA. "
        "legenda: pt-BR, sem repetir a headline, no máximo 1500 caracteres."
    )
    user = f"ARTIGO:\n{texto}\n\nTarefa: gere kicker, headline e legenda conforme instruções."

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.5,
        "max_tokens": 420,
    }

    resp = requests.post(
        OPENROUTER_URL,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=payload,
        timeout=(10, 60),
    )
    resp.raise_for_status()

    content = resp.json()["choices"][0]["message"]["content"].strip()
    data = json.loads(content)

    kicker = data["kicker"].strip().upper()
    headline = data["headline"].strip().upper()
    legenda = data["legenda"].strip()

    return kicker, headline, legenda

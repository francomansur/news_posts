# News Posts

Projeto simples para buscar notícias em uma API e gerar elementos de post (kicker, headline, legenda).

---

## 🚀 Iniciando com Poetry

1. Instale as dependências:
    ```bash 
   poetry install
    ```

2. Ative o ambiente virtual:  
    ```bash
   poetry shell  
    ```

   ou rode direto com:
   ```bash  
   poetry run python -m src.news.main
   ```

---

## ⚙️ Configuração do .env

O projeto usa variáveis de ambiente para acessar APIs externas.  

1. Copie o arquivo de exemplo:
    ```bash
   cp .env.example .env
   ```

2. Preencha o `.env` com suas chaves:  
   OPENROUTER_KEY=sua_chave_aqui  
   NEWS_API_KEY=sua_chave_aqui  

Importante: o arquivo `.env` deve estar no `.gitignore` para não versionar suas chaves.

---

## 📂 Estrutura Atual

src/  
  news/  
    __init__.py  
    buscar_noticias.py  
    criar_elementos.py  
    main.py  

---

## 🧩 Módulos e Funções

1. buscar_noticias.py  
   - Função: buscar_manchetes(theme: str) -> list[dict]  
   - Descrição: busca notícias relacionadas ao tema informado e retorna uma lista de dicionários com dados dos artigos (incluindo a URL).  

2. criar_elementos.py  
   - Função: gerar_elementos(article_url: str) -> tuple[str, str, str]  
   - Descrição: recebe a URL de uma notícia e retorna uma tupla com:  
     - kicker: 3–6 palavras em caixa alta  
     - headline: título curto em caixa alta  
     - legenda: resumo do artigo em até 1500 caracteres  

---

## ▶️ Executando o fluxo

poetry run python -m src.news.main

O script irá:  
1. Perguntar um tema para buscar notícias.  
2. Selecionar a primeira notícia encontrada.  
3. Gerar kicker, headline e legenda.  

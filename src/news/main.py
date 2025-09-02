from .buscar_noticias import buscar_manchetes
from .criar_elementos import gerar_elementos


def main():
    theme = input("Tema para buscar notícias: ").strip()
    if not theme:
        print("Informe um tema.")
        return

    print("Buscando notícias...")
    artigos = buscar_manchetes(theme) 
    if not artigos:
        print("Nenhuma notícia encontrada.")
        return

    primeiro = artigos[0]
    url = primeiro.get("url") or primeiro.get("link")
    if not url:
        raise RuntimeError("A primeira notícia não possui URL ('url' ou 'link').")

    print(f"Gerando elementos para: {url}")
    kicker, headline, legenda = gerar_elementos(url)

    print(" ")
    print(f"KICKER  : {kicker}")
    print(f"HEADLINE: {headline}")
    print("LEGENDA :")
    print(legenda)


if __name__ == "__main__":
    main()

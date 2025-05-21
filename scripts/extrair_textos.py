import os
import pdfplumber
import json

PASTA_PDFS = "pdfs"
PASTA_SAIDA = "resultados/textos_extraidos"

def extrair_texto_pdf(caminho_arquivo):
    texto = ""
    with pdfplumber.open(caminho_arquivo) as pdf:
        for pagina in pdf.pages:
            pagina_texto = pagina.extract_text()
            if pagina_texto:
                texto += pagina_texto + "\n"
    return texto.strip()

if __name__ == "__main__":
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    arquivos = [f for f in os.listdir(PASTA_PDFS) if f.endswith(".pdf")]
    print(" Lendo arquivos PDF na pasta:", PASTA_PDFS)
    print(" Arquivos encontrados:", arquivos)

    for nome_arquivo in arquivos:
        caminho_pdf = os.path.join(PASTA_PDFS, nome_arquivo)
        print(f" Processando: {nome_arquivo}")

        texto = extrair_texto_pdf(caminho_pdf)

        if not texto:
            print(f" Nenhum texto extraído de: {nome_arquivo}")

        dados = {
            "arquivo": nome_arquivo,
            "texto": texto
        }

        nome_saida = nome_arquivo.replace(".pdf", ".json")
        caminho_saida = os.path.join(PASTA_SAIDA, nome_saida)

        with open(caminho_saida, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    print("\n Extração concluída! JSONs salvos em:", PASTA_SAIDA)

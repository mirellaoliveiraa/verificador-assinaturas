import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from pdf2image import convert_from_path
import json, os, subprocess, platform, csv


POPPLER_PATH = r"C:\Users\Mirella Chaves\Desktop\Release-24.08.0-0\poppler-24.08.0\Library\bin"


# CONFIGURAÇÕES
PASTA_JSONS = "./resultados/textos_extraidos"
PASTA_PDFS = "./pdfs"
ARQUIVO_VERIFICADOS = "./resultados/verificados_manual.json"
ARQUIVO_CSV = "./resultados/verificados_manual.csv"
# Verifica se as pastas existem
if not os.path.exists(PASTA_JSONS):
    messagebox.showerror("Erro", f"Pasta de JSONs não encontrada:\n{PASTA_JSONS}")
    exit(1)


arquivos = [f for f in os.listdir(PASTA_JSONS) if f.endswith(".json")]
index_atual = 0
nome_arquivo_atual = ""

# FUNÇÕES PRINCIPAIS
def exportar_para_csv(lista):
    campos = ["uuid", "arquivo", "status", "detectado_automatico", "confirmado_manual", "tem_assinatura"]
    with open(ARQUIVO_CSV, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)
    print("✅ CSV atualizado:", ARQUIVO_CSV)

def salvar_resposta():
    global index_atual
    nome_arquivo = arquivos[index_atual]
    detectado = checkbox_var1.get()
    confirmado = checkbox_var2.get()
    assinatura = assinatura_var.get()

    if assinatura == "":
        status = "sem_assinatura"
    elif detectado == confirmado:
        status = "confirmado"
    else:
        status = "revisar"

    resultado = {
        "uuid": os.path.splitext(nome_arquivo)[0],
        "arquivo": nome_arquivo,
        "status": status,
        "detectado_automatico": "sim" if detectado else "não",
        "confirmado_manual": "sim" if confirmado else "não",
        "tem_assinatura": assinatura
    }

    if os.path.exists(ARQUIVO_VERIFICADOS):
        with open(ARQUIVO_VERIFICADOS, "r", encoding="utf-8") as f:
            dados_atuais = json.load(f)
    else:
        dados_atuais = []

    dados_atuais = [d for d in dados_atuais if d["uuid"] != resultado["uuid"]]
    dados_atuais.append(resultado)

    with open(ARQUIVO_VERIFICADOS, "w", encoding="utf-8") as f:
        json.dump(dados_atuais, f, ensure_ascii=False, indent=2)

    exportar_para_csv(dados_atuais)
    avancar_arquivo()

def pular_arquivo():
    avancar_arquivo()

def remover_ultima():
    if not os.path.exists(ARQUIVO_VERIFICADOS): return
    with open(ARQUIVO_VERIFICADOS, "r", encoding="utf-8") as f:
        dados = json.load(f)
    if dados:
        dados.pop()
        with open(ARQUIVO_VERIFICADOS, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        exportar_para_csv(dados)
        print("❌ Última entrada removida")

def abrir_pdf():
    caminho_pdf = os.path.join(PASTA_PDFS, nome_arquivo_atual)
    if not os.path.exists(caminho_pdf):
        messagebox.showerror("Erro", f"PDF não encontrado:\n{caminho_pdf}")
        return
    try:
        if platform.system() == "Windows":
            os.startfile(caminho_pdf)
        elif platform.system() == "Darwin":
            subprocess.call(["open", caminho_pdf])
        else:
            subprocess.call(["xdg-open", caminho_pdf])
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir PDF:\n{e}")

def atualizar_texto():
    global nome_arquivo_atual
    nome_json = arquivos[index_atual]
    nome_arquivo_atual = nome_json.replace(".json", ".pdf")

    for widget in frame_direita.winfo_children():
        widget.destroy()

    caminho_pdf = os.path.join(PASTA_PDFS, nome_arquivo_atual)
    try:
        imagens = convert_from_path(caminho_pdf, poppler_path=POPPLER_PATH)
        imagem = imagens[0]

        imagem_tk = ImageTk.PhotoImage(imagem.resize((700, 900)))
        label = tk.Label(frame_direita, image=imagem_tk)
        label.image = imagem_tk
        label.pack()

    except Exception as e:
        label = tk.Label(frame_direita, text=f"Erro ao carregar PDF:\n{e}", fg="red", bg="#eeeeee")
        label.pack()

def proximo_arquivo():
    if index_atual >= len(arquivos):
        if os.path.exists(ARQUIVO_VERIFICADOS):
            with open(ARQUIVO_VERIFICADOS, "r", encoding="utf-8") as f:
                dados = json.load(f)
                total = len(dados)
                confirmados = sum(1 for d in dados if d["status"] == "confirmado")
                revisar = sum(1 for d in dados if d["status"] == "revisar")
                sem = sum(1 for d in dados if d["status"] == "sem_assinatura")
                print(f"\n✅ Verificação concluída!\n- Confirmados: {confirmados}\n- Revisar: {revisar}\n- Sem Assinatura: {sem}\n- Total: {total}")
        messagebox.showinfo("Fim", "Todos os arquivos foram verificados.")
        return
    atualizar_texto()

def voltar_arquivo():
    global index_atual
    if index_atual > 0:
        index_atual -= 1
        atualizar_texto()

def avancar_arquivo():
    global index_atual
    if index_atual < len(arquivos) - 1:
        index_atual += 1
        atualizar_texto()
    else:
        index_atual += 1
        proximo_arquivo()

# INTERFACE
janela = tk.Tk()
janela.title("🔍 Verificação de Assinaturas Digitais")
janela.geometry("1200x720")
janela.configure(bg="#2e2e2e")

container = tk.Frame(janela, bg="#2e2e2e")
container.pack(fill="both", expand=True, padx=20, pady=20)

frame_esquerda = tk.Frame(container, bg="#f4f4f4", bd=1, relief="flat")
frame_esquerda.pack(side="left", fill="y", padx=(0, 10), ipadx=15, ipady=15)

checkbox_var1 = tk.BooleanVar()
checkbox_var2 = tk.BooleanVar()
assinatura_var = tk.StringVar(value="")

tk.Checkbutton(frame_esquerda, text="🧠 Sistema detectou assinatura digital?", variable=checkbox_var1, bg="#f4f4f4").pack(anchor="w", pady=(0, 5))
tk.Checkbutton(frame_esquerda, text="👀 Você confirma manualmente que há assinatura?", variable=checkbox_var2, bg="#f4f4f4").pack(anchor="w", pady=(0, 10))
tk.Label(frame_esquerda, text="📌 Este documento TEM assinatura digital?", bg="#f4f4f4").pack(anchor="w")
tk.Radiobutton(frame_esquerda, text="✅ Sim", variable=assinatura_var, value="sim", bg="#f4f4f4").pack(anchor="w")
tk.Radiobutton(frame_esquerda, text="❌ Não", variable=assinatura_var, value="não", bg="#f4f4f4").pack(anchor="w", pady=(0, 10))

tk.Button(frame_esquerda, text="💾 Salvar e Próximo", command=salvar_resposta, width=20).pack(pady=(5, 5))
tk.Button(frame_esquerda, text="⏩ Pular", command=pular_arquivo, width=20).pack(pady=(0, 5))
tk.Button(frame_esquerda, text="❌ Remover Último", command=remover_ultima, width=20).pack(pady=(0, 10))
tk.Button(frame_esquerda, text="⬅️ Voltar", command=voltar_arquivo, width=20).pack(pady=(0, 5))
tk.Button(frame_esquerda, text="➡️ Avançar", command=avancar_arquivo, width=20).pack(pady=(0, 10))
tk.Button(frame_esquerda, text="🖥️ Abrir PDF", command=abrir_pdf, width=20).pack()

frame_direita = tk.Frame(container)
frame_direita.pack(side="left", fill="both", expand=True)

proximo_arquivo()
janela.mainloop()

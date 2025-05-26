# 🔏 Verificador de Assinaturas Digitais em PDFs

Este projeto é uma ferramenta desenvolvida em **Python**, com interface gráfica em **Tkinter**, para realizar a verificação **manual** de assinaturas digitais em documentos PDF.  
O sistema exibe o conteúdo dos arquivos como **imagem** (não apenas texto) para facilitar a inspeção visual de assinaturas e elementos gráficos.

🛡️ Todo o processamento é realizado **localmente**, garantindo a privacidade e segurança dos arquivos PDF.

---

## 🛠️ Instalação

1. Certifique-se de ter o **Python 3.8 ou superior** instalado no sistema.

2. Clone este repositório:

```bash
git clone https://github.com/mirellaoliveiraa/verificador-assinaturas.git
cd verificador-assinaturas
Instale as dependências:

 
pip install -r requirements.txt
Baixe o Poppler for Windows:

Extraia o ZIP em um local fixo (ex: Desktop)

Copie o caminho da pasta Library\bin

No arquivo verificador_assinaturas.py, edite a linha do POPPLER_PATH, por exemplo:

 
POPPLER_PATH = r"C:\Users\SeuUsuario\Desktop\Release-24.08.0-0\poppler-24.08.0\Library\bin"
 Estrutura do Projeto
 
verificador-assinaturas/
├── pdfs/                         # Coloque aqui os PDFs a serem verificados
├── resultados/
│   ├── verificados_manual.csv    # Resultado da verificação manual (CSV)
│   └── verificados_manual.json   # Resultado da verificação manual (JSON)
├── scripts/
│   ├── extrair_textos.py         # (Opcional) Extrai o texto dos PDFs
│   └── verificador_assinaturas.py # Interface principal para validação
├── .gitignore
├── requirements.txt
└── README.md
🧪 Como Usar
1. Adicione os arquivos PDF
Coloque todos os arquivos que deseja verificar na pasta pdfs/.

2. Execute o verificador
 
python scripts/verificador_assinaturas.py
A interface abrirá mostrando cada PDF como imagem.
Você poderá marcar:

✅ Se o sistema detectou assinatura digital

👁️ Se confirma manualmente a assinatura

📌 Se o documento tem ou não assinatura digital

Os resultados são salvos automaticamente na pasta resultados/.

3. Consultar resultados
Verifique os arquivos:

resultados/verificados_manual.csv

resultados/verificados_manual.json

Cada linha contém:

UUID do documento

Nome do arquivo

Status da verificação: confirmado, revisar, sem_assinatura

Detecção automática

Confirmação manual

Indicação de assinatura

4. (Opcional) Extrair textos dos PDFs
Se quiser apenas visualizar o texto extraído dos PDFs (sem imagem), execute:


python scripts/extrair_textos.py
🔐 Segurança e Privacidade
🔒 100% local: Nenhum dado é enviado para a internet

🧠 Verificação manual assistida: você tem controle total

📄 Os arquivos PDF não são alterados

📝 Licença
Este projeto está licenciado sob os termos da Licença MIT.

👩‍💻 Desenvolvido por
Mirella Oliveira
Idealizadora e desenvolvedora
🔗 GitHub: @mirellaoliveiraa

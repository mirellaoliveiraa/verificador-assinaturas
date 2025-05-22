🔏 Verificador de Assinaturas Digitais em PDFs


Este projeto é uma ferramenta desenvolvida em Python, usando Tkinter, para auxiliar na validação manual de assinaturas digitais em documentos PDF. Ele permite extrair o texto de arquivos PDF e visualizar informações sobre certificados digitais das assinaturas presentes, ajudando o usuário a verificar a autenticidade de documentos assinados digitalmente. Todo o processamento é realizado localmente, garantindo que os arquivos confidenciais não saiam do seu ambiente.




🛠️ Instalação

Antes de começar, certifique-se de ter o Python 3.x instalado em seu sistema.
Clone o repositório ou faça o download do código fonte do projeto.
Instale as dependências listadas no arquivo requirements.txt. Você pode fazer isso executando o seguinte comando em um terminal na pasta raiz do projeto:
bash
Copiar
Editar
pip install -r requirements.txt
Isso irá instalar todas as bibliotecas Python necessárias para rodar o projeto.


📂 Estrutura de Pastas

css
Copiar
Editar
verificador-assinaturas/
├── Scripts/
│   ├── extrair_textos.py
│   └── verificador_assinaturas.py
├── resultados/
│   ├── verificados_manual.csv
│   └── verificados_manual.json
├── pdfs/
│   └── *coloque aqui os PDFs a serem verificados*
├── LICENSE
├── README.md
└── .gitignore
A pasta Scripts contém os scripts Python principais: o extractor de textos e o verificador de assinaturas.
A pasta pdfs deve conter os arquivos PDF que serão analisados pelo sistema.
A pasta resultados é onde serão gerados os relatórios (CSV/JSON) das verificações manuais realizadas.


🧪 Como usar

Prepare os documentos: coloque todos os arquivos PDF que deseja verificar dentro da pasta pdfs do projeto.
Extraia o texto dos PDFs (opcional): Execute o script de extração para obter o conteúdo textual dos PDFs e auxiliar na verificação manual do conteúdo:
bash
Copiar
Editar
python Scripts/extrair_textos.py
Este comando irá ler cada PDF em pdfs e exibir no console o texto extraído. Recomenda-se analisar esse texto para verificar se há algo suspeito ou oculto no documento antes de proceder à verificação da assinatura.
Verifique as assinaturas digitais: Execute o script principal de verificação de assinaturas:
bash
Copiar
Editar
python Scripts/verificador_assinaturas.py
Ao executar este comando, uma interface gráfica será aberta. Nela, você poderá visualizar as informações das assinaturas digitais presentes (como o nome do signatário, a autoridade certificadora e a validade do certificado) em cada documento PDF. Com base nessas informações e na sua análise manual, marque cada documento como válido ou inválido conforme o resultado da verificação da assinatura digital.
Resultados da verificação: Após verificar os documentos, o sistema salvará automaticamente um resumo dos resultados na pasta resultados. Consulte os arquivos verificados_manual.csv ou verificados_manual.json para ver o registro de quais PDFs foram marcados como válidos ou inválidos na verificação manual. Cada entrada inclui o nome do arquivo e o status atribuído durante a checagem.




🛡️ Segurança

Processamento Local: Todo o processamento dos PDFs e das assinaturas digitais é feito localmente. Nenhum dado dos documentos ou informações de certificados é enviado para servidores externos, garantindo a privacidade e confidencialidade dos seus arquivos.
Verificação Manual: Esta ferramenta não realiza a validação automática da cadeia de certificação das assinaturas. Em vez disso, ela exibe os dados relevantes para que você possa verificar manualmente a autenticidade de cada assinatura digital. Certifique-se de checar o emissor do certificado, a data de validade e outros detalhes importantes de cada assinatura de acordo com as normas de segurança que você confia.
Integridade dos Arquivos: Os arquivos PDF não são modificados pelo sistema – eles são apenas lidos para extração de informações. Você pode abrir os PDFs normalmente em um leitor de PDF para inspeção adicional, se necessário, enquanto utiliza o verificador para registrar os resultados da validação.


📃 Licença
Este projeto é licenciado sob os termos da Licença MIT. Consulte o arquivo LICENSE para obter detalhes sobre os direitos e limitações de uso. Sinta-se livre para usar, modificar e distribuir este projeto conforme os termos da licença.


🙋‍♀️ Desenvolvido por
Mirella Oliveira – GitHub (Idealizadora e desenvolvedora do projeto)
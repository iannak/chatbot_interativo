## Documentação - Instalação e Execução da Aplicação Chatbot Interativo

Visão Geral
Esta aplicação é um chatbot interativo que foi projetado para responder a perguntas e aprender com base nas interações dos usuários. A aplicação foi construída usando Streamlit, Groq LLM API para processamento de linguagem natural, e LangChain para manipulação da cadeia de conversação. A aplicação também pode ser executada dentro de um container Docker.

Pré-requisitos
Antes de começar a instalação e execução da aplicação, é necessário ter algumas ferramentas instaladas em sua máquina:

1. Python 3.9+
A aplicação foi construída para funcionar com Python 3.9 ou versões superiores. Você pode verificar sua versão do Python executando:

bash
```
python --version
```
Caso não tenha o Python instalado, você pode baixá-lo aqui.

2. Docker (Opcional, caso queira rodar a aplicação em container)
Se você deseja rodar a aplicação dentro de um container Docker, precisará ter o Docker instalado. Você pode verificar se o Docker está instalado com o seguinte comando:

bash
```
docker --version
```
Caso não tenha o Docker, siga as instruções para instalação aqui.

Passo 1: Clonar o Repositório
Primeiro, clone o repositório contendo o código da aplicação:

bash
```
git clone <URL_do_repositório>
cd <diretório_do_repositório>
```

Passo 2: Instalar Dependências

1. Instalar Dependências com Pip
Caso esteja executando a aplicação localmente (fora de um container Docker), você pode instalar as dependências usando o pip.

No diretório raiz do projeto, crie e ative um ambiente virtual (opcional, mas recomendado):

bash
```
python -m venv venv  # Criação do ambiente virtual
source venv/bin/activate  # Ativação do ambiente (Linux/macOS)
```
# ou
```
venv\Scripts\activate  # Ativação do ambiente (Windows)
```
Em seguida, instale as dependências listadas no arquivo requirements.txt:

bash
```
pip install -r requirements.txt
```

2. Dependências Principais
streamlit: Framework para construção da interface do usuário.
requests: Para fazer requisições HTTP para a API.
langchain: Para construção de cadeias de conversação.
groq: Para utilizar o modelo de linguagem Groq LLM.

Passo 3: Configuração de Variáveis de Ambiente

1. API da Groq
Se você estiver utilizando a API da Groq, será necessário definir a variável de ambiente para a chave de API. Para isso, crie um arquivo .env no diretório raiz do projeto e adicione sua chave da Groq:

bash
```
GROQ_API_KEY=sua_chave_da_api
```
Ou, no terminal (se preferir definir a variável diretamente):

bash
```
export GROQ_API_KEY=sua_chave_da_api  # Linux/macOS
```

# ou
```
set GROQ_API_KEY=sua_chave_da_api  # Windows
```

2. Chave da API do OpenAI (se necessário)
Caso queira usar a API do OpenAI (em vez da Groq), defina a variável de ambiente com a chave da API do OpenAI:

bash
```
export OPENAI_API_KEY=sua_chave_da_api_openai  # Linux/macOS
```

# ou
```
set OPENAI_API_KEY=sua_chave_da_api_openai  # Windows
```

Passo 4: Executar a Aplicação Localmente
Agora você está pronto para rodar a aplicação localmente.

1. Rodar a Aplicação com Streamlit
Para executar a aplicação com Streamlit, use o seguinte comando:

bash
```
streamlit run app.py
```
Isso abrirá o aplicativo no navegador na URL:

http://localhost:8501

A partir dessa URL, você poderá interagir com o chatbot e testar suas funcionalidades.

2. Rodar a Aplicação em Docker (opcional)
Se preferir rodar a aplicação em um container Docker, você precisará de um arquivo Dockerfile configurado corretamente (já fornecido anteriormente).

Passo 1: Construir a Imagem Docker
No diretório raiz do projeto (onde está o Dockerfile), execute o seguinte comando para construir a imagem Docker:

bash
```
docker build -t chatbot-app .
```

Passo 2: Rodar o Container Docker
Após a imagem ser construída com sucesso, execute o container:

bash
```
docker run -p 8501:8501 chatbot-app
```
Isso mapeará a porta 8501 do container para a porta 8501 da sua máquina local, permitindo o acesso à aplicação.

Passo 5: Usando a Aplicação
1. Interagindo com o Chatbot
Após a aplicação ser executada, você verá um campo de entrada onde pode digitar suas mensagens.
O chatbot responderá com base nas informações que ele aprendeu ou nas regras programadas.
Você pode testar diferentes perguntas e até adicionar informações ao banco de dados interno do chatbot (se configurado).
2. Exemplos de Uso
Aqui estão alguns exemplos de interações com o chatbot:

Pergunta: "Quem é o presidente do Brasil?"

Resposta: O chatbot fornecerá uma resposta com base nos dados armazenados ou usará a API para recuperar a informação.

Preferência: "Prefiro um tom mais formal nas respostas."

Resposta: O chatbot adaptará seu estilo de resposta para ser mais formal nas interações subsequentes.

Passo 6: Personalizações e Configurações Avançadas
Se você deseja personalizar o comportamento do chatbot ou fazer ajustes finos, aqui estão algumas áreas que você pode explorar:

Alterar o Modelo de Linguagem: Se você estiver usando a Groq ou o OpenAI, pode alterar o modelo de linguagem para outro modelo disponível. Modifique o arquivo chatbot.py com o nome do modelo desejado.

Adicionar Funcionalidade: O chatbot pode ser ampliado para lidar com mais tipos de interações, como integração com outros serviços ou aprendizado de novas informações. Adapte o código dentro de chatbot.py para lidar com essas situações.

Armazenar Preferências: Você pode adicionar mais lógica para armazenar e recuperar preferências do usuário, garantindo que o chatbot se adapte ao longo do tempo.


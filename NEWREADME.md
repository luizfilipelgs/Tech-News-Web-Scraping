# Boas vindas ao repositório do projeto Job Insights !
 # O que foi desenvolvido  👨‍💻 

  Este projeto de web scraping foi desenvolvido para coletar notícias sobre tecnologia de um site específico. Utilizando técnicas de raspagem de dados, foi possível extrair informações como o título da notícia, sua categoria, o resumo e o link para a notícia completa. Com a automação desse processo, foi possível coletar uma grande quantidade de informações em um curto espaço de tempo, permitindo a manipulação e análise dos dados coletados.
 
![Apresentação](/technews.gif)

# Tecnologias utilizadas <a name="tecnologias"></a>
- [**Python**](https://www.python.org/)
- [**requests**](https://pypi.org/project/requests/)
- [**parsel**](https://pypi.org/project/parsel/)
- [**mongodb**](https://www.mongodb.com/)
- [**pymongo**](https://pypi.org/project/pymongo/) 


# Orientações <a name="orientacoes"></a>

<details>
<summary><strong> 🔰 Iniciando o projeto e Comandos Úteis</strong></summary><br />

  1. Clone o repositório

  - `git clone git@github.com:luizfilipelgs/Tech-News-Web-Scraping`

  2. Entre na pasta do repositório que você acabou de clonar:

  - `cd Tech-News-Web-Scraping`

  3. Crie o ambiente virtual para o projeto e ativeo 

  - `python3 -m venv .venv && source .venv/bin/activate`

  4. Caso já se tenha clonado e criado o ambiente virtual antes, apenas ative com:

  - `source .venv/bin/activate`
  
  5. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  6. Caso Não tenha o mongoDB localmente, rode via docker com:

  - `docker-compose up -d mongodb`

  7. Inicialize a aplicação.

  - digite o comando `tech-news-analyzer` para acessar o menu em seu terminal e utilizar a aplicação.
  
  
</details>

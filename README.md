# Power Data Tecnologia - CASE TÉCNICO

## Objetivo

Construir e disponibilizar uma plataforma que visa oferecer uma experiência envolvente, onde os usuários podem explorar informações detalhadas sobre personagens, planetas, naves e filmes da saga. Para isso, necessitamos da criação de uma API capaz de capturar as necessidades dos usuários e responder perguntas básicas sobre os filmes, personagens, planetas e naves.

## Critérios
- [x] Ambiente **GCP (Cloud Function e API Gateway/Apigee)**.
- [x] Utilizar Python para construção da solução.
- [x] Consumir os dados a partir da API de [StarWars](https://swapi.dev/).
- [x] Filtragem de dados com base em dados específicos.


## Requisitos Funcionais
- [x] RF001 - O sistema deve permitir que o usuário consulte diferentes informações através de um único endpoint.
- [x] RF002 - O sistema deve permitir que o usuário interaja com os dados utilizando filtros específicos.
- [x] RF003 - O sistema deve permitir que o usuário faça buscas com digitação livre.
- [x] RF004 - O sistema deve permitir o usuário consultar informações sobre filmes, personagens, planetas e naves.
- [x] RF005 - O sistema deve permitir o usuário ordenar os resultados utilizando valores específicos.
- [x] RF006 - O sistema deve permitir o usuário uma navegação controlada (Paginação)

## Instalação
  ### Pré-requisito

  Para inicializar o projeto é necessário que seja instalado o [**uv**](https://docs.astral.sh/uv/getting-started/installation/). Acesse o link ou siga uma das alternativas abaixo.

  - **Escolha uma das alternativas:**
    - **pip:**
      ```sh
      pip install uv
      ```
    - **MacOs/Linux:**
      ```sh
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```
    - **Windows:**
      ```sh
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```

  ### Instalação

  - **Clone o repositório:**
    ```sh
    git clone https://github.com/daavii-b/portfolio.git
    ```
  - **Instale as dependências do projeto:**
    ```sh
    uv sync --extra dev
    ```


## Utilização

**OBS: Garanta que o seu ambiente virtual está ativado. Por padrão o uv irá criar o ambiente virtual e instalar as dependências ao executar o comando listado anteriormente. Porém, você precisa ativá-lo manualmente:**

- **MacOS/Linux**:
  ```sh
  source .venv/bin/activate
  ```

- **Windows:**
  ```sh
  .venv\Scripts\Activate.ps1
  ```

### Executando comandos:

- **Inicializar a API:**
  ```sh
  fastapi run src/main.py
  ```

- **Rodar os testes da aplicação:**
  ```sh
  pytest
  ```

## Referência da API:

### Endpoints:
*Consulte diferentes informações sobre  filmes, personagens, planetas e naves do **StarWars**.*
  - **POST** `/dashboard`:
     - **Query Params:**
       - `resource`:
         - `people` **(default)**
         - `films`
         - `planets`
         - `starships`

*Consulte a disponibilidade da API.*
  - **GET** `/heath`


 **Acesse a [documentação](https://pwd-api-case-67qoea42.ue.gateway.dev/docs) da API para mais detalhes.**

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `pyproject.toml` para detalhes.

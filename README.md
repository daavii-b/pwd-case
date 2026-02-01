# Power Data Tecnologia - CASE TÉCNICO

## Objetivo

Construir e disponibilizar uma plataforma que visa oferecer uma experiência envolvente, onde os usuários podem explorar informações detalhadas sobre personagens, planetas, naves e filmes da saga. Para isso, necessitamos da criação de uma API capaz de capturar as necessidades dos usuários e responder perguntas básicas sobre os filmes, personagens, planetas e naves.

## Critérios
- [ ] Ambiente **GCP (Cloud Function e API Gateway/Apigee)**.
- [ ] Utilizar Python para construção da solução.
- [ ] Consumir os dados a partir da API de [StarWars](https://swapi.dev/).
- [ ] Filtragem de dados com base em dados específicos.


## Requisitos Funcionais
- [ ] RF001 - O sistema deve permitir que o usuário consulte diferente informações através de um único endpoint.
- [ ] RF002 - O sistema deve permitir que o usuário interaja com os dados utilizando filtros específicos. 
- [ ] RF003 - O sistema deve permitir que o usuário faça buscas com digitação livre.
- [ ] RF004 - O sistema deve permitir o usuário consultar informações sobre filmes, personagens, planetas e naves.

## Requisitos Não Funcionais
- [ ] RNF001 - O sistema deve utilizar cache para melhora de performance.
- [ ] RNF002 - O sistema deve utilizar paginação para listagem de dados.
- [ ] RNF003 - O sistema deve ter uma cobertura de tests acima de 80%.


## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `pyproject.toml` para detalhes.
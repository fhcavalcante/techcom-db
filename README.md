# techcom-db

# MVP Arquitetura de Software

Componente database do projeto Tech.com

Este projeto foi desenvolvido por Flávio Cavalcante e faz parte do trabalho de conclusão do módulo de Arquitetura de software da Pós-Graduação em Engenharia de Software da Puc-Rio.

O sistema é um terminal de consultas auxíliado por inteligência artificial, onde os colaboradores de uma determinada empresa podem tirar suas dúvidas. Um frontend se comunica
com um serviço de respostas, que utilizando Retrieval Augmented Generation (RAG) em um modelo LLM disponibilizado pelo popular Hugging Face analisa um manual fornecido por uma empresa fictícia e fornece a resposta adequada ao usuário. Uma terceira componenete faz o registro das perguntas e respostas e gera um histórico.

---
## Como executar

Com o Docker instalado, monte o container com o comando:

docker build -t techcom-db . 

2 - Execute:

docker run -p 5002:5002 techcom-db

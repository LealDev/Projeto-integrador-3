# Projeto Integrador 3

Essa é a documentação básica para execução da análise feita com base nos dados do prouni

# Como inicializar esse projeto

Esse é um projeto construido em python e postgres, porém para que a execução seja feita de forma mais simples, os códigos estão em containers docker.

## Pré-requisitos para inicialização

**- Docker instalado no computador**

**- Baixar os dados na origem (baixar o arquivo csv no link abaixo)**

[Link para download da base de dados](https://www.kaggle.com/datasets/lfarhat/brasil-students-scholarship-prouni-20052019)

Após o download da base é necessário que ela esteja na raiz do projeto, junto dos arquivos `docker-compose.yml` e `Dockerfile`

Uma vez que a base de dados esteja no local correto basta utilizar o comando abaixo

```
docker-compose up -d
```

Após a execução do comando o sistema estará funcionando na `porta 8501` do computador
[http://localhost:8501/](http://localhost:8501/)

**Importante:** Por se tratar de uma base de dados muito grande, existe um delay para inicialização do sistema.

Quando iniciar o sistema, basta aguardar que a página será atualizada quando o banco de dados estiver carregado.

## Componentes:

**- Allan Jones da Silva Jesus**

**- Christiano Augusto Betzel Lemke de Resende**

**- Emanuel Nascimento leal**

**- Igor Paraiso Demuner**

**- Lucas Dalvi Rodrigues**

**- Rodrigo Andreatta Vieira**

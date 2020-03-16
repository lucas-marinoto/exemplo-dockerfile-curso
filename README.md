# Curso Python SysAdmin - Conceitos Dockerfile

**Principais Comandos Docker**

```sh docker pull NomedaImagem ``` (Baixa uma imagem do Docker Hub)

```sh docker ps``` (ps listar containers ativos)

```sh docker ps -a```  (-a listar todos os containers existentes)

```sh docker start idimagem```  (inicia um container)

```sh docker stop idimagem```  (para um container)

```sh docker rm idImagem``` (remover uma imagem da maquina)

```sh docker run nomeimagem``` (startar uma imagem e se nao tiver vai baixar e criar)

```sh docker run -ti fedora``` (-ti é um terminal interativo, ele abrira o terminar da imagem do container e fedora é o nome de uma imagem)

```sh docker run -dti fedora``` (-d é para dar persistencia e executar o container em background)

```sh docker run -dti --name fedora1 fedora``` (--name associar um nome a uma imagem)

```sh docker inspect fedora1``` (inspect mostra um json sobre informações do container)

```sh docker top nomeimagem ou id``` (mostra informacoes do container)

```sh docker stats nomeimagem ou id``` (stats mostra o consumo do container, memória etc...)

```sh docker rm -f $(docker ps -qa)``` (apaga todas as imagens de container em massa. -qa lista 
sh todos os ids. Este é um subshell

```sh docker search nomedaimagem``` (lista imagens que existem no dockerhub pelo terminal)

```sh docker images``` (mostra imagens que eu ja fiz download localmente)

```sh docker image rm nomedaimagem``` (deletar imagem que ja foi baixada)

```sh docker system prune -a ``` (remove todas as imagens, containers parados)

```sh docker exec -ti nomeimagem sh ``` (abre o container usando exec e sh é o shell para rodar comando)


**Site interessante com algumas referências de comandos**

https://medium.com/xp-inc/principais-comandos-docker-f9b02e6944cd


## Estrutura de arquivos

**Pastas**

    ├── etl
    │    ├── app
    │    │   ├── app.py
    │    │   ├── requirements.txt
    └──  └── Dockerfile
    ├── json
    │    ├── app
    │    │   ├── app.py
    │    │   ├── requirements.txt
    └──  └── Dockerfile

## Criando e rodando imagem

1 - Baixar e rodar o container de uma imagem do MongoDB passando a váriavel de ambiente no parâmetro -e

**Parâmetros:**

- `-e` : Váriavel de ambiente
- `-v` : Volume para persistir os dados. Este será criado localmente na máquina hospedeira e após os : será criado dentro da imagem que ficarão vinculados.
- `--name` : Serve para dar um nome a este container
- `-dti` : A letra **d** permite executar o container em background. A letra **t** associa o terminal local ao terminal do container. A letra **i** permite interagir com o container.

```sh
docker run -dti --name mongodb -e MONGO_INITDB_ROOT_USERNAME='acme' -e MONGO_INITDB_ROOT_PASSWORD='!Abc123' -v /home/lucas/Projetos/mongo:/data/db 
```

2 - Acessar a pasta **etl** via terminar e rodar o comando abaixo para criar a imagem do etl. Como nesta pasta tem o Dockerfile, então irá criar a imagem de acordo com o arquivo Dockerfile.

**Parâmetros:**

- `-t` : A letra **t** associa o terminal local ao terminal do container.
- `. ` : O ponto serve para informar o contexto.
- `acme-etl` : Nome da imagem que a ser criada. Poderia ser qualquer outro nome.

```sh
docker build -t acme-etl .
```

3 - Acessar a pasta **json** via terminar e rodar o comando abaixo para criar a imagem do json. Como nesta pasta tem o Dockerfile, então irá criar a imagem de acordo com o arquivo Dockerfile.

**Parâmetros:**

- `-t` : A letra **t** associa o terminal local ao terminal do container.
- `. ` : O ponto serve para informar o contexto.
- `acme-json` : Nome da imagem que a ser criada. Poderia ser qualquer outro nome.

```sh
docker build -t acme-json .
```

4 - Via terminal (pode ser em qualquer pasta), rodar o comando abaixo para criar o container. Este container de acordo com o Dockerfile irá rodar o app.py da imagem. Osb.: O nome das varíaveis de ambiente são as mesmas que estão no arquivo app.py e a senha a mesma do mongo.
Ao criar este container, o status ficará como exited, pois ele só roda um script, insere no banco e acaba.

**Parâmetros:**

- `-dti` : A letra **d** permite executar o container em background. A letra **t** associa o terminal local ao terminal do container. A letra **i** permite interagir com o container.
- `-e` : Váriavel de ambiente
- `--name` : Nome customizado para este container
- `-acme-etl` : Nome da imagem que será usada para criar o container. Esta poderia ser qualquer outra imagem existente.

```sh
docker run -dti --name etl -e MONGO_HOST=172.17.0.2 -e MONGO_USER='acme' -e MONGO_PASS='!Abc123' acme-etl
```

5 - Via terminal (pode ser em qualquer pasta), rodar o comando abaixo para criar o container. Este container de acordo com o Dockerfile irá rodar o app.py da imagem. Osb.: O nome das varíaveis de ambiente são as mesmas que estão no arquivo app.py e a senha a mesma do mongo.

**Parâmetros:**

- `-dti` : A letra **d** permite executar o container em background. A letra **t** associa o terminal local ao terminal do container. A letra **i** permite interagir com o container.
- `-e` : Váriavel de ambiente
- `--name` : Nome customizado para este container
- `-p` : Mapeia a porta 5000 da maquina hospederia para a porta 5000 do container.
- `-acme-json` : Nome da imagem que será usada para criar o container. Esta poderia ser qualquer outra imagem existente.

```sh
docker run -dti --name flask -p 5000:5000 -e MONGO_HOST=172.17.0.2 -e MONGO_USER='acme' -e MONGO_PASS='!Abc123'  acme-json
```


## Execução

1 - Após a criação dos containers, acessar http://0.0.0.0/5000 e verá que retornou um json.

```json
[
{
"_id": 1,
"email": "bvoase0@ox.ac.uk",
"gender": "Male",
"name": "Batholomew Voase",
"salary": 4251
},
{
"_id": 2,
"email": "pboog1@acquirethisname.com",
"gender": "Female",
"name": "Perri Boog",
"salary": 3261
}
]
```
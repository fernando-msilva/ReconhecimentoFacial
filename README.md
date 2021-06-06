# SpyFace

## Descrição

O Spyface é um projeto desenvolvido para fins acadêmicos. Tem o objetivo de ser uma ferramenta para ajudar em operações de recuperação de fugitivos.

## Como executar localmente

Para utilizar o SpyFace localmente será necessário que você tenha algumas ferramentas instaladas em seu ambiente:

### Pré requisitos

* Python 3.8
* Virtualenv
* Docker
* Docker compose
* Minikube
* Postman (Ou similares, como insomnia. também pode ser utilizado wget ou curl. Por questões de praticidade usaremos o postman neste exemplo)

### Arquitetura da solução

Atualmente o projeto é composto basicamente pelo serviço de API Gateway utilizando o **Krakend**, o **MongoDB** como banco de dados para armazenar metadados, a **API** que recebe a imagem a ser comparada e retorna o *Score* construida em python com o **Fast API**, e o serviço de treino com o código de treinamento do **OpenCV** onde é gerado o artefato utilizado pela API. O diagrama abaixo exemplifica a interação entre os componentes.

![plot](./doc/diagram.png)

### Iniciando o ambiente com o Docker Compose

Primeiramente é necessário criar a imagem base utilizada pelo serviço de treino e pela api. Para isso execute o comando abaixo:

```sh
$ docker image build -t spyface:base imagem-base
```

Com a imagem base criada basta executar o comando abaixo:

```sh
$ docker-compose up -d && docker-compose logs -f
```

O comando irá subir os serviços, o treinamento do modelo irá iniciar automaticamente. Após finalizar o treinamento um arquivo .yml será gerado na pasta modelo, que vai ser compartilhado com a API para realizar a comparação das imagens. Após o serviço de treinamento ser encerrado a API pode começar a receber imagens para a comparação.

### Iniciando o ambiente com o Minikube

Para este exemplo será utilizado o minikube com o doker como driver, caso deseje utilizar outro driver o carregamento das imagens no cluster será feita de uma forma diferente. Fora isso não há difereça no deploy da suloção em relação ao tipo de driver utilizado.

 * Inicie o minikube com o comando `minikube start --driver docker`

 * Com o cluster já em execução digite o comando `eval $(minikube docker-env)` para configurar no terminal as variáveis necessárias para que o build das imagens seja direcionado ao cluster.

 * Agora para dar o build das imagens no cluster execute os comando `docker image build -t spyface:base imagem-base` para o build da imagem base, `docker image build -t api:0.1 api` para o build da imagem da API, `docker image build -t krakend:0.1 krakend` para build da imagem do API Gateway e `docker image build -t spyface:0.1 spyface` para build da imagem de treino

 * Com as imagens carregadas no cluster agora é necessário inicar os serviços. Primeiramente inicie o mongodb com o comando `kubectl apply -f kubernetes/mongodb.yml`. Com o mongodb em execução inicie os demais serviços com o comando `kubectl apply -f kubernetes`.

* A API vai ser publicada com um service load balancer no minikube. Para conseguir acessar externamente será necessário que, em um novo terminal, seja executado o comando `minikube tunnel`. Enquanto este comando estiver em execução o minikube fornecerá acesso ao service load balance. Assim que o comando estiver em execução volte ao primeiro terminal e digite `kubectl get svc`, a saida vai retornar um ip externo para o service **api-gateway-service**, esse ip é o que será utilizado para acessar a API.

### Enviando imagens via API

Caso esteja utilizando o Docker Compose substituia o **{{host}}** na url por **localhost**, caso esteja utilizando o deploy com o minikube substitua com o endereço do ip externo do service.

Para validar se a API está funcionando corretamente teste acessando a url http://{{host}}/spyface/v1/predict pelo seu navegador, ou envie uma requisição com a ferramenta que tiver acesso. O retorno deve ser similar ao json abaixo:

```json
{
    "status": "ok"
}
```

Com o serviço da API em execução abra o postman e crie uma requisição do tipo POST para a url http://localhost/predict. Na aba "Body" selecione "form-data", insira um campo chave nomeado "id" e adicione o valor 1, crie um novo campo e defina a chave como "file" e escolha o arquivo de imagem que será enviado para a API. A configuração deve ficar similar a seguinte:

![plot](./doc/postman.png)

Ao enviar a requisição será retornado o score relativo a confiança do fugitivo estar presente na imagem, como mostra o exemplo abaixo:

![plot](./doc/predict.png)
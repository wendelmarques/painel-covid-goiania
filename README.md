
<header> 
<h1 align="center">Painel COVID GYN</h1>
</header>

<h3 align="center">
Informações sobre a evolução dos casos confirmados em Goiânia
  <br>  <br>
painel-covid-goiania.herokuapp.com
 </p>
<p align="center">
<img src="https://media.giphy.com/media/RlMjsjnmtp8K5CkgRU/giphy.gif">
 </p>


<p align="center">
<img src="https://img.shields.io/github/repo-size/wendelmarques/mapeamento-medias-enem-folium?color=blueviolet">
<img src="https://img.shields.io/github/languages/count/wendelmarques/mapeamento-medias-enem-folium?color=blueviolet">
<img src="https://img.shields.io/github/followers/wendelmarques?color=blueviolet">

</p>

<h4 align="center"> 
FINALIZADO (CONSTANTE ATUALIZAÇÃO DOS DADOS)
</h4> 

<div align="center">

<p align="center">
  <a href="#about">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#objetivos">Objetivos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#features">Features</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#dados">Dados</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#get">Execução</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnicas">Técnicas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tech">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#fontes">Fontes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#creditos">Créditos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contribute">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#creator">Criador</a>
</p>
</div>

<a id="about"></a>
## Sobre o projeto
O projeto utiliza abordagens de ciência dos dados para desenvolver um painel de monitoramento dos dados da COVID-19 em relação a casos confirmados e óbitos. O painel contém gráficos e mapa com dados de Goiânia.

<a id="objetivos"></a>
## Objetivos
  - Coletar dados sobre a COVID-19 no âmbito municipal (por bairro)
  - Construir esquemas de visualização (mapas e gráficos) possuam interpretação simples e objetiva
  
<a id="features"></a>
## Features
*    Bubble Map - casos confirmados por bairro
*    Gráfico de barras e média móvel sobre casos ativos por data de notificação
*    Gráfico de barras e média móvel sobre casos confirmados por data de notificação 
*    Gráfico de barras e média móvel sobre óbitos confirmados por data de notificação 
*    Bar race - casos confirmados por bairro
*    Bar race - casos confirmados por região

<a id="dados"></a>
## Dados
Basicamente, algoritmos coletam dados do site da [Prefeitura de Goiânia](https://www.goiania.go.gov.br/) e realiza a plotagem por bairro e região. Para criação dos gráficos que contém dados da cidade como um todo (sem considerar os bairros individualmente), um dataset do [Brasil.IO](https://brasil.io/dataset/covid19/caso/?search=&date=&state=&city=&place_type=&is_last=&city_ibge_code=5208707&order_for_place=) foi utilizado. As informações isolados sobre recuperações, casos confirmados e óbitos são adicionados manualmente, elas são retiradas do site da Prefeitura de Goiânia e da plataforma [COVID Goiás - UFG](https://covidgoias.ufg.br/). Os CEPs dos bairros foram coletados do site [guiamaisCEP](https://cep.guiamais.com.br/) e, em seguida, para obter as coordenadas de cada um deles, a [Geocoding API - Google Maps Plataform](https://developers.google.com/maps/documentation/geocoding/) foi utilizada. 


<a id="get"></a>
## Execução

**Você pode acessar este projeto clicando [aqui](https://painel-covid-goiania.herokuapp.com/)**
### Antes de executar 
Crie uma conta em  ```www.mapbox.com```. Com a conta criada, gere um token em ```account.mapbox.com/access-tokens```. Copie o token e substitua _YOUR_KEY_ em ```config.ini```.

### Como executar

1. Utilizando um terminal, vá para a pasta que deseja copiar o projeto:


```console
$ cd suapasta
```

2. Copie este projeto para seu repositório local:

```console
$ git clone https://github.com/wendelmarques/painel-covid-goiania.git
```

3. Acesse seu repositório local:'

```console
$ cd painel-covid-goiania
```

4. Com o interpretador Python configurado, execute a instalação das bibliotecas:

```console
$ pip install -r requirements.txt
```
5. Acesse a pasta scripts:

```console
$ cd scripts
```
5. Ao dar esse comando, um arquivo pickle (_.p_) será gerado. Ele fica na pasta ../data/pickle/.

```console
$ cd cria_mapa_e_grafico.py
```

6. Volte para a pasta principal:

```console
$ cd ../
```
7. Rode o app
```
$ app.py
```
8. Por fim, acesse:
```
http://localhost:8050/
```

<a id="tecnicas"></a>
## Técnicas
- Data scraping
- Web scraping
- Manipulação de dataframes com Pandas e Python


<a id="tech"></a>
## Tecnologias

Painel COVID GYN usa as seguintes tecnologias:
* [Dash](https://plotly.com/dash/) - utilizado para construir o app.
* [Plotly](https://plotly.com/chart-studio/) - construção dos gráficos e mapa.
* [Numpy](https://numpy.org/) - plotagens de dados e gráficos
* [Pandas](https://pandas.pydata.org/) - execução de algoritmos de predição
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - extração de dados
* [Requests](https://requests.readthedocs.io/en/master/) - utilizada para fazer requisições HTTP pelo Python.
* [Datetime](https://docs.python.org/3/library/datetime.html) - manipulação de datas.
* [Configparser](https://docs.python.org/3/library/configparser.html) - acesso aos arquivos das pastas.
* [Gunicorn](https://gunicorn.org/) - servidor de produção.
* [Pickle](https://docs.python.org/3/library/pickle.html) - The pickle module implements binary protocols for serializing and de-serializing a Python object structure. 
* [os](https://docs.python.org/3/library/os.html) - manipulção de arquivos.
* [Geocoding API - Google Maps Plataform](https://developers.google.com/maps/documentation/geocoding/) - utilizada para obter coordenadas.
* [bar_chart_racer](https://github.com/dexplo/bar_chart_race) - criação de gráfico animados.
* [FFmpeg](https://github.com/dexplo/bar_chart_race) - conversão de arquivos.

<a id="fontes"></a>
## Fontes
*    [Prefeitura de Goiânia](https://www.goiania.go.gov.br/)
*    [Brasil.IO - O Brasil em dados libertos](https://brasil.io/dataset/covid19/caso/?search=&date=&state=&city=&place_type=&is_last=&city_ibge_code=5208707&order_for_place=)
*    [COVID Goiás - UFG](https://covidgoias.ufg.br/)
*    [Geocoding API - Google Maps Plataform](https://developers.google.com/maps/documentation/geocoding/)
*    [guiamaisCEP](https://cep.guiamais.com.br/)
*    [Wikipédia](https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Goi%C3%A2nia)

<a id="creditos"></a>
## Créditos
*    [Plotly - Repositório](https://github.com/plotly/dash-sample-apps/tree/master/apps)
*   [How to create outstanding animated scatter maps with Plotly and Dash (Medium) - Lamothe Thibaud ](https://towardsdatascience.com/how-to-create-animated-scatter-maps-with-plotly-and-dash-f10bb82d357a)
*    [Deploying Dash or Flask web application on Heroku. Easy CI/CD (Medium) - Lamothe Thibaud](https://towardsdatascience.com/deploying-dash-or-flask-web-application-on-heroku-easy-ci-cd-4111da3170b8)
*    [Official Release of bar_chart_race (Medium) - Ted Petrou
dexplo.org/bar_chart_race](https://medium.com/dunder-data/bar-chart-race-python-package-official-release-78a420e182a2)
*    [Gráfico de Corrida de Barras | Dica Pandas #7 - Programação Dinâmica (YouTube)](https://www.youtube.com/watch?v=rIwxjCnvdcY)
*    [Como utilizar a Google Geocoding API para obter endereços](https://www.devmedia.com.br/como-utilizar-a-google-geocoding-api-para-obter-enderecos/36751)
*    [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python)
* [Como fazer um Web Scraping com Python](https://goomore.com/blog/web-scraping-python/)
* [Official Release of bar_chart_race](https://medium.com/dunder-data/bar-chart-race-python-package-official-release-78a420e182a2)
* [Corrida de CASOS de COVID no Brasil | Gráfico de Corrida de Barras (Bar Chart Race) | Dica Pandas #7](https://www.youtube.com/watch?v=rIwxjCnvdcY)
* [ACESSANDO RECURSOS NA WEB COM PYTHON](https://pythonhelp.wordpress.com/2013/03/12/acessando-recursos-na-web-com-python/)
* [Como usar o R para escolher um lugar para morar (3) - Converter CEP em coordenadas geográficas](https://sillasgonzaga.github.io/2016-11-18-olx3/#:~:text=Obter%20endere%C3%A7o%20a%20partir%20do%20CEP&text=Sabemos%20que%20quanto%20mais%20dados,%2C%20bairro%2C%20cidade%20e%20estado.&text=%C3%89%20necess%C3%A1rio%20juntar%20todas%20as,de%20endere%C3%A7os%20em%20uma%20s%C3%B3)


<a id="contribute"></a>

## Como contribuir para o projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`



<a id="creator"></a>
## Criador


[![Linkedin Badge](https://img.shields.io/badge/-Wendel-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wendelmarques/)](https://www.linkedin.com/in/wendelmarques/) 
[![Gmail Badge](https://img.shields.io/badge/-wendelmarquesjs@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:wendelmarquesjs@gmail.com)](mailto:wendelmarquesjs)
=======


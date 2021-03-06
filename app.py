#########################################################################################
#########################################################################################
################################### PAINEL COVID GYN ####################################
#########################################################################################
#########################################################################################

# painel-covid-goiania.herokuapp.com
# github.com/wendelmarques/painel-covid-goiania

####################################### Objetivo #########################################
#  Criar vizualizações com os dados sobre os casos confirmados da COVID-19 em Goiânia.
# Os dados utilizados para geração do mapa e dos gráficos, foram retirados dos Informes Epidemiológicos 
# publicados (em PDFs) pela Prefeitura de Goiânia, por meio de uma técnica chamada Data Scraping 
# (algoritmos que realizam a tarefa de extração). São divulgadas apenas informações sobre alguns 
# bairros - os que possuem mais casos confirmados acumulados, por isso, foram extraídos dados de 114
# bairros. Para mais informações, acesse: saude.goiania.go.gov.br



# https://www.github.com/WendelMarques
# https://www.linkedin.com/in/wendelmarques/




#######################################Fontes/ créditos#######################################



# Plotly - Repositório
# How to create outstanding animated scatter maps with Plotly and Dash (Medium) - Lamothe Thibaud
# Deploying Dash or Flask web application on Heroku. Easy CI/CD (Medium) - Lamothe Thibaud
# Official Release of bar_chart_race (Medium) - Ted Petrou dexplo.org/bar_chart_race
# Gráfico de Corrida de Barras | Dica Pandas #7 - Programação Dinâmica (YouTube)
# Como utilizar a Google Geocoding API para obter endereços
# Python Client for Google Maps Services
# Como fazer um Web Scraping com Python
# Official Release of bar_chart_race
# Corrida de CASOS de COVID no Brasil | Gráfico de Corrida de Barras (Bar Chart Race) | Dica Pandas #7
# ACESSANDO RECURSOS NA WEB COM PYTHON
# Como usar o R para escolher um lugar para morar (3) - Converter CEP em coordenadas geográficas



#30 08 2020








############################################################################################
########################################## IMPORTS #########################################
############################################################################################

# Classic libraries
import os
import numpy as np
import pandas as pd

# Logging information
import logging
import logzero
from logzero import logger

# Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html

# Custom function
import scripts.utils_covid as f


############################################################################################
############################## PARAMETERS and PRE-COMPUTATION ##############################
############################################################################################

# Load pre computed data
world = f.load_pickle('world_info.p')
# world = save

# Deployment inforamtion
PORT = 8050

############################################################################################
########################################## APP #############################################
############################################################################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Creating app
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width initial-scale=1"}]
)

# Associating server
server = app.server
app.title = 'Painel COVID GYN - Informações sobre a evolução dos casos confirmados em Goiânia'
app.config.suppress_callback_exceptions = True

############################################################################################
######################################### LAYOUT ###########################################
############################################################################################



########################################################################
############################## alterar_manuamente ######################


total_confirmados_com_outros_bairros = "63.365"
obitos_confirmados = "1.585"
total_ativos = "648"
# https://saude.goiania.go.gov.br/goiania-contra-o-coronavirus/


############################## alterar_manuamente ######################
########################################################################

fontes_footer1 = html.Div(
    id='fontes_footer',
    children=[           
                   
        html.A(
            href='https://www.goiania.go.gov.br/',
            children=[
                html.Img(src=app.get_asset_url('prefeitura.png'), width=90, height=67),
            ]
        ),

        html.A(
            href='https://cep.guiamais.com.br/',
            children=[
                html.Img(src=app.get_asset_url('guiamais.png'), width=90, height= 31,),
            ],
        ),

         html.A(
            href='https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Goi%C3%A2nia',
            children=[
                html.Img(src=app.get_asset_url('wiki.png'), width=70, height=66,),
            ],
        ),      
    ],
)



fontes_footer2 = html.Div(
    id='fontes_footer2',
    children=[      
        html.A(
            href='https://covidgoias.ufg.br/',
            children=[
                html.Img(src=app.get_asset_url('ufg.png'), width=150, height=45,),
            ],
        ),
        html.A(
            href='https://brasil.io/dataset/covid19/caso/?search=&date=&state=&city=&place_type=&is_last=&city_ibge_code=5208707&order_for_place=',
            children=[
                html.Img(src=app.get_asset_url('brasil-io.jpg')),
                
            ],
        ),

        html.A(
            href='https://developers.google.com/maps/documentation/geocoding',
            children=[
                html.Img(src=app.get_asset_url('maps.png'), width=55, height=49),
            ]
        ),
        html.A(
            href='#',
            children=[
                html.Img(src=app.get_asset_url('estado.png'), width=300, height=103),
            ]
        ),
        
    ],
)

links_header = html.Div(
    id='platforms_links',
    children=[                   
        html.A(
            href='https://github.com/wendelmarques/painel-covid-goiania',
            children=[
                html.Img(src=app.get_asset_url('github.png'), width=20, height=20),
                html.Span("Código/Notebook")
            ]
        ),

        html.A(
            href='https://www.linkedin.com/in/wendelmarques/',
            children=[
                html.Img(src=app.get_asset_url('linkedin.svg'), width=20, height=20),
                html.Span("Desenvolvedor")
            ],
        ),

        html.A(
            href='https://towardsdatascience.com/how-to-create-animated-scatter-maps-with-plotly-and-dash-f10bb82d357a',
            children=[
                html.Img(src=app.get_asset_url('medium.png'), width=20, height=20),
                html.Span("How to create the map"),
            ]
        ),
    ],
)

links_creditos = html.Div(
    id='platforms_links2',
    children=[                   
    
        html.A(
            href='https://towardsdatascience.com/how-to-create-animated-scatter-maps-with-plotly-and-dash-f10bb82d357a',
            children=[
                html.Img(src=app.get_asset_url('medium.png'), width=20, height=20),
                html.Span("How to create outstanding animated scatter maps - Lamothe Thibaud")
            ]
        ),
        
    ],
)
 
brs = html.Div([
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
 ])

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                              [
                                html.H2(
                                    "PAINEL",
                                    style={"margin-bottom": "3px"},
                                ),

                                html.H1(
                                    "COVID GYN",
                                    style={"margin-bottom": "3px"},
                                ),

                                html.H4(
                                    "Informações sobre os casos confirmados e óbitos em Goiânia", 
                                    style={"margin-top": "10px"}
                                ),
                            ],
                        ),
                    ], 
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),

        html.Div(            
            [   
                html.H4("Aviso"),

                html.H5(
                    "Os dados utilizados para geração do mapa e dos gráficos 'casos acumulados por região' e 'casos acumulados por bairro' foram extraídos dos Informes Epidemiológicos publicados (em PDFs) pela Prefeitura de Goiânia, por meio de uma técnica chamada Data Scraping (algoritmos que realizam a tarefa de extração). ", 
                    style={"margin-top": "10px"}
                ),

                html.Br(),

                html.H5(
                    "Obtenha informações oficiais em:", 
                    style={"margin-top": "10px"}
                ),

                html.Div(
                    [
                        html.A(
                            html.Button("saude.go.gov.br", id="learn-more-button_estado"),
                            href="https://www.saude.go.gov.br/",
                        )
                    ],
                    id="button_estado",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("saude.goiania.go.gov.br", id="learn-more-button_cidade"),
                            href="https://saude.goiania.go.gov.br/goiania-contra-o-coronavirus/informe-epidemiologico-covid-19/",
                        )
                    ],
                    id="button_cidade",
                ),



                links_header,
                            
            ],
        ),

        brs,

        html.Div(
            [
                html.Div(
                    [                      
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                'Casos confirmados', html.Br(), total_confirmados_com_outros_bairros
                                            ],
                                            className="mini_container_confirmados one columns",
                                        ),
                                        
                                        html.Div(
                                            [
                                                'Óbitos confirmados', html.Br(), obitos_confirmados
                                            ], 
                                            className="mini_container_obitos one columns",
                                        ),

                                        html.Div(
                                            [
                                                'Casos ativos', html.Br(), total_ativos
                                            ],
                                            className="mini_container_ativos one columns",
                                        ),

                                        html.Div(
                                            [
                                                'Última atualização', html.Br(), '16-10-2020',
                                            ],
                                            className="mini_container_branco one columns",
                                        ),
                                        
                                    ],
                                    id="blocks-column",
                                ),   
                            ],
                            className="row flex-display",                                                                                                           
                        ),
                    ],
                    id="right-column",
                    # className="nine columns",
                 ),                
            ],
            className="row flex-display",
         ), 

        brs,
        html.Div(            
            [   
                html.P(
                        [
                            html.H2("Evolução dos casos acumulados por dia e por bairro"),
                            html.H5("(117 bairros)"),
                            html.H6("Fonte: Prefeitura de Goiânia"),
                        ],
                        className="control_label",
                ),
                dcc.Graph(id='mapa-goiania', figure=world['figure'], config={'scrollZoom': True}), 
                            
            ],
            className="pretty_container",
        ),
        brs,
        html.Div(            
            [   
                html.P(
                        [
                            html.H2("Casos ativos por data de notificação e média móvel"),
                            html.H6("Fonte: Secretaria Estadual de Saúde de Goiás"),

                        ],
                        className="control_label",
                ),
                
                dcc.Graph(id='grafico_casos_ativos_por_dia', figure=world['grafico_casos_ativos']),                              
            ], 
            className="pretty_container",
            style={"display": "flex", "flex-direction": "column", "justify-content": "center"},
        ),
        brs,
        html.Div(            
            [   
                html.P(
                        [
                            html.H2("Casos confirmados por data de notificação e média móvel"), 
                            html.H6("Fonte: Secretaria Estadual de Saúde de Goiás"),                                           
                        ],
                        className="control_label",
                ),
                
                dcc.Graph(id='grafico_casos_por_dia', figure=world['grafico_casos_por_dia']),                              
            ], 
            className="pretty_container",
            style={"display": "flex", "flex-direction": "column", "justify-content": "center"},
        ),


        brs,
        html.Div(            
            [   
                html.P(
                        [
                            html.H2("Óbitos por data de notificação e média móvel"),
                            html.H6("Fonte: Secretaria Estadual de Saúde de Goiás"),
                        ],
                        className="control_label",
                ),
                
                dcc.Graph(id='grafico_obitos_por_dia', figure=world['grafico_obitos_dia']),                              
            ], 
            className="pretty_container",
            style={"display": "flex", "flex-direction": "column", "justify-content": "center"},
        ),


       brs,

        html.Div(            
            [   
                html.P(
                        [
                            html.H2("Evolução dos casos acumulados por bairro"), html.H6("(alguns bairros)"),
                            html.H6("Fonte: Prefeitura de Goiânia"),
                        ],
                        className="control_label",
                ),

                html.Video(src=app.get_asset_url('bar_race_bairro.mp4'), controls=True, autoPlay=True, height = 300), 
                            
            ],
            className="pretty_container",
            style={"display": "flex", "flex-direction": "column", "justify-content": "center"},
        ),

        brs,

        html.Div(            
            [   
                html.P(
                        [
                            html.H2("Evolução dos casos acumulados por região"),
                            html.H6("Fonte: Prefeitura de Goiânia"),
                        ],
                        className="control_label",
                ),

                html.Video(src=app.get_asset_url('bar_race_regiao.mp4'), controls=True, autoPlay=True, height = 343),
                            
            ],className="pretty_container",
            style={"display": "flex", "flex-direction": "column", "justify-content": "center"},
        ),

        brs,
        html.Div(
            [
                html.Div(
                    [   
                        html.H2("Dados"),
                        html.H5("Secretaria Estadual de Saúde de Goiás"),
                        html.H5("Prefeitura de Goiânia - Informe Epidemiológico - COVID-19"),
                        # html.Img(src=app.get_asset_url('wordcloud.png')),

                    ],
                    # className="pretty_container",
                ),

            ],
            className="row flex-display",
        ),
        brs,

        html.Div(
            [
                html.Div(
                    [   
                        html.H2("Bairros"),
                        html.H5("(ordem alfabética)"),
                        html.H6(world['lista_bairros']),
                        # html.Img(src=app.get_asset_url('wordcloud.png')),

                    ],
                    # className="pretty_container",
                ),

            ],
            className="row flex-display",
        ),

        brs,

        html.Div(
            [
                html.Div(
                    [
                        html.H2("Fontes")
                    ],
                    style={"margin-bottom": "3px"},
                ),
                
                fontes_footer1, 

            ],
            className="row flex-display",
        ),
     
        html.Div(
            [
                fontes_footer2,                        
            ],
            className="row flex-display", 
        ),

        brs,

        html.Div(
            [
                html.Div(
                    [
                        html.H2("Créditos")
                    ],
                    style={"margin-bottom": "3px"},
                ),

                html.A(
                    href='https://towardsdatascience.com/how-to-create-animated-scatter-maps-with-plotly-and-dash-f10bb82d357a',
                    children=[
                        html.H5("How to create outstanding animated scatter maps with Plotly and Dash (Medium) - Lamothe Thibaud", className='head__text'),
                    ]
                ),

                html.A(
                    href='https://towardsdatascience.com/deploying-dash-or-flask-web-application-on-heroku-easy-ci-cd-4111da3170b8',
                    children=[
                        html.H5("Deploying Dash or Flask web application on Heroku. Easy CI/CD (Medium) - Lamothe Thibaud", className='head__text'),
                    ],
                ),

                html.A(
                    href='https://medium.com/dunder-data/bar-chart-race-python-package-official-release-78a420e182a2',
                    children=[
                        html.H5("Official Release of bar_chart_race (Medium) - Ted Petrou", className='head__text'),
                        html.H5("dexplo.org/bar_chart_race", className='head__text')
                    ],
                ),

                html.A(
                    href='https://www.youtube.com/watch?v=rIwxjCnvdcY',
                    children=[
                        html.H5("Gráfico de Corrida de Barras | Dica Pandas #7 - Programação Dinâmica (YouTube)", className='head__text'),
                    ],
                ),

                html.A(
                    href='https://github.com/plotly/dash-sample-apps/tree/master/apps',
                    children=[
                            html.H5("Plotly - Repositório", className='head__text'),
                    ],
                ),
            ]
        ),

        brs,

        html.Div([
                html.Div(
                    [   
                        html.H2("Quem contribuiu"),
                    ],style={"margin-bottom": "3px"},
                ),

                html.A(
                    href='https://linkedin.com/in/gabimenezesdev',
                    children=[
                        html.H5("Gabi Menezes", className='head__text'),
                    ]
                ),
            ],
        ),

        brs,

        html.Div(
            [
                html.Div(
                    [   
                        html.H5("Criado com muito cuidado por Wendel Marques"),
                        html.H6("github.com/wendelmarques/painel-covid-goiania"),
                        html.H6("linkedin.com/in/wendelmarques"),
                        html.H6("stay safe | ✊🏿"),
                    ],style={"margin-bottom": "3px"},                        
                ),  
            ],
        ),                      
        html.Br(),
        html.Br(),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column", "justify-content": "center"},
)



############################################################################################
######################################### RUNNING ##########################################
############################################################################################

if __name__ == "__main__":
    
    # Display app start
    logger.error('*' * 80)
    logger.error('Inicialização do aplicativo')
    logger.error('*' * 80)

    # Starting flask server
    app.run_server(debug=True, port=PORT)

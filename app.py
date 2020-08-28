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
############################## alterar_manuamente ##############################
############################################################################################


# word['total_confirmed'] #contem o total de casos que foram extraidos dos informes, ou seja, sem o valor de "outros bairros"
total_confirmados_com_outros_bairros = "30 954"  
obitos_confirmados = "848"
total_recuperados = "29.176"

############################################################################################
############################## alterar_manuamente ##############################
############################################################################################



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

# Creating app
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

# Associating server
server = app.server
app.title = 'Painel COVID GYN - Evolução dos casos confirmados na capital'
app.config.suppress_callback_exceptions = True

############################################################################################
######################################### LAYOUT ###########################################
############################################################################################

fontes_footer = html.Div(
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
        html.A(
            href='https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Goi%C3%A2nia',
            children=[
                html.Img(src=app.get_asset_url('ufg.png'), width=100, height=35,),
            ],
        ),
        html.A(
            href='https://developers.google.com/maps/documentation/geocoding/starta',
            children=[
                html.Img(src=app.get_asset_url('maps.png'), width=55, height=49),
            ]
        ),
        
    ],
)


links = html.Div(
    id='platforms_links',
    children=[                   
        html.A(
            href='medium.com/@wendelmarques',
            children=[
                html.Img(src=app.get_asset_url('medium.png'), width=20, height=20),
                html.Span("Criação do dataset")
            ]
        ),
        html.A(
            href='github.com/wendelmarques/painel-covid-goiania',
            children=[
                html.Img(src=app.get_asset_url('github.png'), width=20, height=20),
                # "Application code"
                html.Span("Código")
            ]
        ),
        html.A(
            href='https://www.linkedin.com/in/wendelmarques/',
            children=[
                html.Img(src=app.get_asset_url('linkedin.svg'), width=20, height=20),
                # "autor do painel gyn"
                html.Span("Autor")
            ],
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


app.layout = html.Div(
    children=[

        # HEADER
        html.Div(
            className="header",
            children=[
                html.H3("PAINEL", className="header__text"),
                html.H1("COVID GYN ", className="header__text"),
                html.H2("Evolução diária dos casos confirmados da COVID-19 em Goiânia", className="header__text"),
                
                html.H4("Por meio de uma técnica chamada Data Scraping, os dados utilizados para geração do mapa e do gráfico foram retirados dos Informes Epidemiológicos publicados pela Prefeitura da capital." , className="header__text"),
                html.H4("Para mais informações, acesse: saude.goiania.go.gov.br.", className="header__text"),
                html.Br(),
                html.H4("(*)O mapa contém apenas os bairros com os maiores números de casos, porque são publicados rankings de bairros - alguns deles são classificados como 'outros bairros').", className="header__text"),
                
                html.Br(),
                # html.Hr(),
            ],
        ),

        # CONTENT
        html.Section([
            
            html.Div(
                id='world_line_1',
                children = [ 
                    html.Div(children = ['Pessoas recuperadas', html.Br(), total_recuperados], id='total_recuperados', 
                    className='mini_container_recuperados'),

                    html.Div(children = ['Casos acumulados', html.Br(), total_confirmados_com_outros_bairros], id='confirmed_goiania_total_todos_bairros', className='mini_container_confirmados'),

                    html.Div(children = ['Óbitos acumulados', html.Br(), obitos_confirmados], id='obitos_confirmados', className='mini_container_obitos'),

                    html.Div(children = ['Última atualização', html.Br(), world['last_date']], id='ultima-atualizacao', className='mini_container_branco'),
      
                ],
            ),

            links,
            links_creditos,

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            html.H2("MAPA"),
            html.Div(
                id='world_line_2',

                children = [ 
                    dcc.Graph(id='world_map', figure=world['figure'], config={'scrollZoom': True,}, ),         
                ],
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            #GRAFICOS
            html.H2("ALGUNS BAIRROS"),
            html.Div(
                
                id='grafico_race_bairro',
                children = [
                    html.Video(src=app.get_asset_url('bar_race_bairro.mp4'), controls=True, autoPlay=True, height = 300),     

                ],
            ),
            html.Br(),
             html.Br(),
            html.H2("POR REGIÕES"),
            html.Div(
                id='grafico_race_regiao',
                children = [
                    html.Video(src=app.get_asset_url('bar_race_regiao.mp4'), controls=True, autoPlay=True, height = 343),     
                ],
            ),
            html.Br(),
            html.Br(),

            html.H2("CASOS CONFIRMADOS POR DIA EM GOIÂNIA"),
            html.Div(
                id='grafico',
                children = [ 
                    dcc.Graph(id='grafico_cidade', figure=world['grafico_bar']),         
                ],
            ),
        ]),
        html.Br(),
        html.Br(),
        
        # FOOTER
        html.H2("Fontes"),   
        html.Section([fontes_footer]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2("Créditos"),
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
                html.H5("github.com/ThibaudLamothe/dash-mapbox", className='head__text')
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
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            
            className="header",
            children=[
                html.H2("Desenvolvido por Wendel Marques", className="header__text"),
                html.H4("github.com/wendelmarques/painel-covid-goiania"),
                html.Br(),
            ],
        ),

    ],
)

############################################################################################
######################################### RUNNING ##########################################
############################################################################################

if __name__ == "__main__":
    
    # Display app start
    logger.error('*' * 80)
    logger.error('App initialisation')
    logger.error('*' * 80)

    # Starting flask server
    app.run_server(debug=True, port=PORT)
    

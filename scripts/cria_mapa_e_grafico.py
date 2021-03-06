import json
import numpy as np
import pandas as pd
from logzero import logger
from plotly import graph_objs as go
import plotly.express as px
import dash_html_components as html
import utils_covid as f
from datetime import date, datetime
pd.set_option('chained_assignment', None)





##############cria_grafico########################

def cria_grafico_casos_por_dia(casos_por_dia):
    fig = px.bar(casos_por_dia, x='data_notificacao', y='num_casos', labels={'num_casos':'N° de casos confirmados', 
                                                                         'data_notificacao': 'Data de notificação',})

    fig.add_trace(
        go.Scatter(
            x=casos_por_dia['data_notificacao'],
            y=casos_por_dia['MM_casos'],
            name='Média Móvel<br>(7 dias)',        
            hovertemplate= "Média Móvel: %{x}<br>Data: %{y}<extra></extra>",

        )
    )
    return fig.update()


def cria_grafico_casos_ativos(casos_ativos):
    fig = px.bar(casos_ativos, x='data_notificacao', y='num_casos', labels={'num_casos':'N° de casos ativos', 
                                                                                    'data_notificacao': 'Data de notificação'})

    fig.add_trace(
        go.Scatter(
            x=casos_ativos['data_notificacao'],
            y=casos_ativos['MM_casos'],
            name='Média Móvel<br>(7 dias)',        
            hovertemplate= "Média Móvel: %{x}<br>Data: %{y}<extra></extra>",
        )
    )

    return fig.update()

def cria_grafico_obitos_dia(obitos_por_dia):
    fig = px.bar(obitos_por_dia, x='data_notificacao', y='num_casos', labels={'num_casos':'N° de óbitos', 
                                                                            'data_notificacao': 'Data de notificação',})

    fig.add_trace(
        go.Scatter(
            x=obitos_por_dia['data_notificacao'],
            y=obitos_por_dia['MM_casos'],
            name='Média Móvel<br>(7 dias)',        
            hovertemplate= "Média Móvel: %{x}<br>Data: %{y}<extra></extra>",
        )
    )

    return fig.update()










################################################################################################
################################################################################################
###############################################

def process_pandemic_data(df):

    # Columns renaming
    df.columns = [col.lower() for col in df.columns]

    
    # Extracting latitute and longitude
    df['lat'] = df['location'].apply(lambda x: x.split(',')[0])
    df['lon'] = df['location'].apply(lambda x: x.split(',')[1])

    # Saving countries positions (latitude and longitude per subzones)
    bairros_position = df[['zone', 'lat', 'lon']].drop_duplicates(['zone']).set_index(['zone'])

    # Pivoting per category
    df = pd.pivot_table(df, values='count', index=['date', 'zone'], columns=['category'])
    df.columns = ['confirmed']

    # Merging locations after pivoting
    df = df.join(bairros_position)

    # Filling nan values with 0
    df = df.fillna(0)

    # Compute bubble sizes
    df['size'] = df['confirmed'].apply(lambda x: (np.sqrt(x/10) + 1) if x > 1 else (np.log(x) / 2 + 1)).replace(np.NINF, 0)
    
    # Compute bubble color
    # df['color'] = (df['confirmed']).fillna(0).replace(np.inf , 0)
    df['color'] = df['confirmed']
    
    return df


def create_world_fig(df, mapbox_access_token):

      days = np.unique(df_mapa['date'])
      frames = [{   
            'name':'frame_{}'.format(day),
            'data':[{
                  'type':'scattermapbox',
                  'lat':df.xs(day)['lat'],
                  'lon':df.xs(day)['lon'],
                  'marker':go.scattermapbox.Marker(
                        size=df.xs(day)['size']*4,
                        color=df.xs(day)['color'],
                        showscale=True,
                        # reversescale = True,
                        colorbar={'title':'Casos confirmados', 'titleside':'top', 'thickness':4},
                  ),
                  'customdata':np.stack((df.xs(day)['confirmed'], pd.Series(df.xs(day).index)), axis=-1),
                  'hovertemplate': "<extra></extra>%{customdata[1]} <br>%{customdata[0]}",
            }],           
      } for day in days]

      # Prepare the frame to display
      data = frames[-1]['data']     

      # And specify the adequate button postion    
      active_frame=len(days) - 1

      sliders = [{
            'transition':{'duration': 0},
            'x':0.08, 
            'len':0.88,
            'currentvalue':{'font':{'size':15}, 'prefix':'📅 ', 'visible':True, 'xanchor':'center'},  
            'steps':[{
                        'label':day,
                        'method':'animate',
                        'args':[
                        ['frame_{}'.format(day)],
                        {'mode':'immediate', 'frame':{'duration':100, 'redraw': True}, 'transition':{'duration':50}}
                        ],
            } for day in days]
      }]

    #   play_button = [{
    #         'type':'buttons',
    #         'showactive':True,
    #         'x':0.045, 'y':-0.08,
    #         'buttons':[{ 
    #               'label':'🎬', # Play
    #               'method':'animate',
    #               'args':[
    #                     None,
    #                     {
    #                     'frame':{'duration':100, 'redraw':True},
    #                     'transition':{'duration':50},
    #                     'fromcurrent':True,
    #                     'mode':'immediate',
    #                     }
    #               ]
    #         }]
    #   }],

      layout = go.Layout(
            height=600,
            autosize=True,
            hovermode='closest',
            paper_bgcolor='rgba(0,0,0,0)',
            mapbox={
                  'accesstoken':mapbox_access_token,
                  'bearing':0,
                  'center':{"lat": -16.6799, "lon":-49.255},
                  'pitch':0,
                  'zoom':10.4,
                  'style':'light',
                  
            },
            # updatemenus=play_bucd tton,
            sliders=sliders,
            margin={"r":0,"t":0,"l":0,"b":0}
      )


      return go.Figure(data=data, layout=layout, frames=frames)




def cria_lista_bairros(bairros):
    lista_bairros = " "
    tamanho_lista = len(bairros)
    for i in range(tamanho_lista):
        lista_bairros += bairros[i]

        if i != tamanho_lista-1:
            lista_bairros += '- '
            
    return lista_bairros
################################################################################################
################################################################################################
################################################################################################


if __name__ =="__main__":    

    # Carregando informações necessárias
    mapbox_access_token = f.config['mapbox']['secret_token']
    raw_dataset_path_dataset_covid_mapa = f.RAW_PATH + f.config['path']['mapa']
    raw_dataset_path_dataset_grafico_casos_por_dia = f.RAW_PATH + f.config['path']['grph_casos_por_dia']
    raw_dataset_path_dataset_grafico_obitos_dia = f.RAW_PATH + f.config['path']['grph_obitos_por_dia']
    raw_dataset_path_dataset_grafico_casos_ativos = f.RAW_PATH + f.config['path']['grph_casos_ativos']
    
    ####### MAPA #########
    df_mapa = pd.read_csv(raw_dataset_path_dataset_covid_mapa, sep=',')
    #cria lista de bairros 
    bairros = cria_lista_bairros(np.unique(df_mapa['Zone']))
    df_world = process_pandemic_data(df_mapa)
    df_total_kpi = df_world.groupby('date').sum().sort_index().iloc[-1]


    #########  GRAFICOS ###########
    #cria dataframe com o dados para o grafico
    df_casos_por_dia= pd.read_csv(raw_dataset_path_dataset_grafico_casos_por_dia, sep=',')
    df_obitos_dia = pd.read_csv(raw_dataset_path_dataset_grafico_obitos_dia, sep=',')
    df_casos_ativos = pd.read_csv(raw_dataset_path_dataset_grafico_casos_ativos, sep=',')
    #cria graficos
    grafico_casos_por_dia = cria_grafico_casos_por_dia(df_casos_por_dia)
    grafico_obitos_dia = cria_grafico_obitos_dia(df_obitos_dia)
    grafico_casos_ativos = cria_grafico_casos_ativos(df_casos_ativos)
    # preparando map
    fig_world = create_world_fig(df_world, mapbox_access_token=mapbox_access_token)

    
    #altera formato da data
    data = datetime.strptime(df_world.index[-1][0], '%Y-%m-%d').date()
    dataFormatada = data.strftime('%d/%m/%Y')

    # Armazenamento de todas as informações necessárias para o aplicativo
    save = {
        'figure':fig_world,
        'grafico_casos_ativos': grafico_casos_ativos,
        'grafico_casos_por_dia': grafico_casos_por_dia,
        'grafico_obitos_dia': grafico_obitos_dia,
        # 'grafico_bar_casos_por_dia': grafico_casos_por_dia,
        'last_date':dataFormatada,
        'lista_bairros': bairros,
        'total_confirmed': f.spacify_number(int(df_total_kpi['confirmed'])),
    }
    f.save_pickle(save, 'world_info.p')

    # mostra infos
    logger.info('O app foi atualizado.')
    logger.info('Dados armazenados.')
    logger.info('A última data no novo conjunto de dados é {}'.format(df_world.index[-1][0]))




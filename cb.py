from dash import Dash, html, dcc, Output, Input, dash_table
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.read('results.xlsx')
#tabela_partidas = df[['ano_campeonato', 'rodada', 'time_mandante','time_visitante', 'gols_mandante', 'gols_visitante', ]]


partidas_df = pd.read_excel('results.xlsx')

tabela_partidas = partidas_df[['ano_campeonato', 'rodada', 'time_mandante','time_visitante', 'gols_mandante', 'gols_visitante', ]]

#def historico_classificacao(ano):
 #   dtf = tabela_partidas.loc[(tabela_partidas['ano_campeonato'] == ano) & (tabela_partidas['rodada'] == 1) ]
  #  ef_2 = pd.DataFrame()
   # ef_2['times'] = pd.concat([dtf['time_mandante'], dtf['time_visitante']], ignore_index=True)
#
 #   anos = [str(ano) for ano in range(1, 39)]
#
 #   for ano in anos:
  #      ef_2[ano]= 0
#
 #   for i in range(1,39):
  ##     for p in cd:
    #    ef_2.loc[(ef_2['times']==)]
    #return

def update(ano, rodada):

    df = tabela_partidas.loc[(tabela_partidas['ano_campeonato'] == ano) & (tabela_partidas['rodada'] == rodada) ]
    df=df.reset_index(drop=True)
    
    df_2 = pd.DataFrame()
    df_2['times'] = pd.concat([df['time_mandante'], df['time_visitante']], ignore_index=True)
   
    df_2.loc[:,'pontos'] = 0
    df_2.loc[:,'jogos'] = 0
    df_2.loc[:,'vitorias'] = 0
    df_2.loc[:,'empates'] = 0
    df_2.loc[:,'derrotas'] = 0
    df_2.loc[:,'saldo_gols'] = 0
    df_2.loc[:,'gols'] = 0
    df_2.loc[:,'gols_tomados'] = 0
 
    for u in range(1,rodada+1):
        df = tabela_partidas.loc[(tabela_partidas['ano_campeonato'] == ano) & (tabela_partidas['rodada'] == u) ]
        df=df.reset_index(drop=True)
        for i in range(len(df)):
            if(df.loc[i,'gols_mandante'] > df.loc[i,'gols_visitante']):
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols'] += df.loc[i,'gols_mandante']
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols'] += df.loc[i,'gols_visitante']
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'pontos'] += 3
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'vitorias'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'derrotas'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'jogos'] +=1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'jogos'] +=1
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols_tomados'] += df.loc[i,'gols_visitante']
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols_tomados'] += df.loc[i,'gols_mandante']
                #df_2.loc[]
                
                #df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'saldo_gols'] = df.loc[i,'gols_mandante'] = df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols'] += df.loc[i,'gols_visitante'] - df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols_tomados']
                #df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'saldo_gols'] = df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols'] - df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols_tomados']
            if(df.loc[i,'gols_mandante'] == df.loc[i,'gols_visitante']):
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols'] += df.loc[i,'gols_mandante']
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols'] += df.loc[i,'gols_visitante']
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'empates'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'empates'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'pontos'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'pontos'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'jogos'] +=1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'jogos'] +=1
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols_tomados'] += df.loc[i,'gols_visitante']
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols_tomados'] += df.loc[i,'gols_mandante']
            if(df.loc[i,'gols_mandante'] < df.loc[i,'gols_visitante']):
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols'] += df.loc[i,'gols_mandante']
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols'] += df.loc[i,'gols_visitante']
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'derrotas'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'vitorias'] += 1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'pontos'] += 3
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'jogos'] +=1
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'jogos'] +=1
                df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols_tomados'] += df.loc[i,'gols_visitante']
                df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols_tomados'] += df.loc[i,'gols_mandante']
            df_2['saldo_gols'] = df_2['gols'] - df_2['gols_tomados']
                #df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'saldo_gols'] = df.loc[i,'gols_mandante'] = df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols'] += df.loc[i,'gols_visitante'] - df_2.loc[(df_2['times']==df.loc[i,'time_visitante']),'gols_tomados']
                #df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'saldo_gols'] = df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols'] - df_2.loc[(df_2['times']==df.loc[i,'time_mandante']),'gols_tomados']
            
    uf = df_2.sort_values(by=['pontos','vitorias', 'saldo_gols'], ascending=False)
    uf = uf.reset_index(drop=True)
    uf.index+=1

    #display(uf)
    return uf    

#update(2015,38)
op1 = list(range(2003,2024))
op2 = list(range(1,39))
anon=2003
rodadan=1
tabela = update(2003,1)


#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Campeonato Brasileiro'),
    html.H2(children='Tabela por ano e por rodada'),

    html.Div(children='''
        Este gráfico a classificação do campeonato brasileiro por ano e rodada.
    '''),
    
    dcc.Dropdown(op1, value=2003, id='ano'),
    dcc.Dropdown(op2, value=1, id='rodada'),

    #dash_table.DataTable(update(anon,rodadan).to_dict('records'), [{"name": i, "id": i} for i in update(2003,1).columns])
    dash_table.DataTable(
        id='classificacao',
        columns=[{'name': i,'id':i} for i in tabela.columns],
        data = tabela.to_dict('records')    
        
    )

    
   
])


@app.callback(
    Output('classificacao', 'data'),
    [Input('ano', 'value'), Input('rodada', 'value')]
)
def update_classificacao(input1, input2):
    # Lógica para calcular e retornar o resultado
    
    if(input1!=anon  or input2!=rodadan):
        data = update (input1,input2)
    else:
        data = update(2003,1)
    return data.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
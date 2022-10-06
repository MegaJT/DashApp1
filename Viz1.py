import dash
from dash import dcc, html,dash_table
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

logo=html.Img(src='assets/logo.jpg',width=100,height=75)
Title=html.H1("IDS MYSTERY SHOPPING",style={'text-align':'center'})

import Tables as T

def indicator_creator():
    figure=go.Figure(go.Indicator(
    mode = "gauge+number",
    gauge = {'axis': {'range': [None, 100], 'dtick':'20'},
            'bar': {'color': "#353437"},
            'bgcolor': "white",
            'steps': [{'range': [0, 20], 'color': '#FF0D0D'},
                      {'range': [20, 40], 'color': '#FF4E11'},
                      {'range': [40, 60], 'color': '#FF8E15'},
                      {'range': [60, 80], 'color': '#FAB733'},
                      {'range': [80, 100], 'color': '#ACB334'}]
            },
    domain = {'x': [0, 1], 'y': [0, 1]}))
    return figure



Dial1=indicator_creator()
Dial1.update_layout(height=200,modebar_remove=True,margin=dict(l=15, r=15, t=0, b=0),paper_bgcolor='#FF9C4A')
Dial1.update_traces(title = {'text': 'OVERALL'})    


Dial2=indicator_creator()
Dial2.update_layout(height=200,modebar_remove=True,margin=dict(l=15, r=15, t=0, b=0),paper_bgcolor='#FFBF93')
Dial2.update_traces(title = {'text': 'SIMPLE'})

Dial3=indicator_creator()
Dial3.update_layout(height=200,modebar_remove=True,margin=dict(l=15, r=15, t=0, b=0),paper_bgcolor='#FFBF93')
Dial3.update_traces(value=20,title = {'text': 'QUICK'})

Dial4=indicator_creator()
Dial4.update_layout(height=200,modebar_remove=True,margin=dict(l=15, r=15, t=0, b=0),paper_bgcolor='#FFBF93')
Dial4.update_traces(value=20,title = {'text': 'TRUST'})

Dial5=indicator_creator()
Dial5.update_layout(height=200,modebar_remove=True,margin=dict(l=15, r=15, t=0, b=0),paper_bgcolor='#FFBF93')
Dial5.update_traces(value=20,title = {'text': 'WORTH'})


fig1=html.Div(dcc.Graph(id='Overall',figure=Dial1),style={'border-radius': '25px','background-color':'#FF9C4A','padding':'10px 10px 10px 10px'})
fig2=html.Div(dcc.Graph(id='Simple',figure=Dial2),style={'border-radius': '25px','background-color':'#FFBF93','padding':'10px 10px 10px 10px'})
fig3=html.Div(dcc.Graph(id='Quick',figure=Dial3),style={'border-radius': '25px','background-color':'#FFBF93','padding':'10px 10px 10px 10px'})
fig4=html.Div(dcc.Graph(id='Trust',figure=Dial4),style={'border-radius': '25px','background-color':'#FFBF93','padding':'10px 10px 10px 10px'})
fig5=html.Div(dcc.Graph(id='Worth',figure=Dial5),style={'border-radius': '25px','background-color':'#FFBF93','padding':'10px 10px 10px 10px'})
#,'background-color':'#eab676'
#,'border':'solid'



Easy_to_Handle_Score1=html.Div(style={'color':'white','text-align': 'center','border-radius': '25px','background-color':'crimson','padding':'0px 0px 0px 0px'},id='Branch_meanscore')
Easy_to_Handle_Score2=html.Div(style={'text-align': 'center','border-radius': '25px','background-color':'lightslategrey','padding':'0px 0px 0px 0px'},id='Average_meanscore')
Easy_to_Handle_Text=html.Div([html.H6('Zajil made it easy to handle my transaction- Mean score',style={'text-align': 'center'}),Easy_to_Handle_Score1,Easy_to_Handle_Score2],style={'border-radius': '25px','background-color':'#FFBF93','padding':'10px 10px 10px 10px'})


#-------------------Branch Bar chart
Branch_Name=T.Branch_Name()


Branch_Selector=dcc.Dropdown(options=Branch_Name,value=Branch_Name[0],id='Branch_slector')

Branch_Score_Dict,Overall_Score_Overall=T.Score_Generator_Dict()
Branch_Name_BarChart=list(Branch_Score_Dict.keys())
Branch_Score_BarChart=list(Branch_Score_Dict.values())

Branch_Score_Adj_BarChart=[]
Branch_Score_Bar_color=[]
for items in Branch_Score_BarChart:
    if items>=Overall_Score_Overall:
        Branch_Score_Adj_BarChart.append(items)
    else:
        Branch_Score_Adj_BarChart.append(items*-1)    
    if (items-Overall_Score_Overall)>0:
        Branch_Score_Bar_color.append('lightslategray')
    else:
        Branch_Score_Bar_color.append('crimson')    

bar_chart=go.Figure()
bar_chart.add_trace(go.Bar(x=Branch_Name_BarChart, y=Branch_Score_Adj_BarChart,
                base=0,
                text=Branch_Score_BarChart,
                textposition='auto',
                marker_color=Branch_Score_Bar_color,
                name='Branch Scores'))
bar_chart.update_layout(title_text='Branch Performance',modebar_remove=True)


Bar_Chart_Graph=html.Div(dcc.Graph(id='Bar_chart',figure=bar_chart),style={'border-radius': '25px','background-color':'lightslategrey','padding':'10px 10px 10px 10px'})

#-----------------------------------------

Table_title=html.H3('Branch Visit Deep Dive')

#-----------Data Tables
dff=T.DataTables()
dff.rename({'index':'Branch'},axis=1,inplace=True)
Table=dash_table.DataTable(dff.to_dict('records'),
    page_size=15,
#    fixed_rows={'headers': True},
    style_table={'overflowX': 'auto',
                'height': '400px', 
                'overflowY': 'auto'
                },
    style_cell={
#         'padding': '5px',
#         'height': 'auto',
#         #'width': 'auto',
#         # all three widths are needed
#         #'minWidth': '100%', 'width': '100%', 'maxWidth': '100%',
#         'whiteSpace': 'normal',
         'textAlign': 'left'
     },
     style_header={
#        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'minWidth': '100%', 'width': '100%', 'maxWidth': '100%',
        'height': '50px',
        'padding': '5px'
    },
    style_data_conditional=(
    [{'if':{'row_index':[0,6,14,21,24]},
       'column_id': 'Branch',
       'backgroundColor':'purple',
       'color':'white',
       'fontWeight':'bold'
   }]+

    [{ 'if':{'filter_query':'{{{col}}}>70'.format(col=col),'column_id': col} ,
           'backgroundColor':'#2ecc40'
    }for col in dff.columns ]+

    [{ 'if':{'filter_query':'{{{col}}}<70 && {{{col}}}>40'.format(col=col),'column_id': col} ,
           'backgroundColor':'#ff851b'
    }for col in dff.columns ]+

    [{ 'if':{'filter_query':'{{{col}}}<40'.format(col=col),'column_id': col} ,
           'backgroundColor':'#b82e26'
    }for col in dff.columns ]


    )
    )




#----------------------



app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([logo],width=2),
        dbc.Col([Title],width=8),
        dbc.Col([],width=2)
    ]),
dbc.Row([html.Hr()]),    
dbc.Row([
        dbc.Col([html.H5('Select Branch'),Branch_Selector,html.Hr(),Easy_to_Handle_Text],width=2),    
        dbc.Col([fig1],width=2),
        dbc.Col([fig2],width=2),
        dbc.Col([fig3],width=2),
        dbc.Col([fig4],width=2),
        dbc.Col([fig5],width=2),
    ]),
dbc.Row([html.Hr()]),        
dbc.Row([Bar_Chart_Graph]),
dbc.Row([html.Hr()]), 
dbc.Row([Table_title]), 
dbc.Row([Table]),
dbc.Row([html.Hr()]), 




], fluid=True)



# Callback section: connecting the components
# ************************************************************************

@app.callback(
    Output('Overall', 'figure'),
    Output('Simple', 'figure'),    
    Output('Quick', 'figure'),    
    Output('Trust', 'figure'),    
    Output('Worth', 'figure'),                
    Output('Branch_meanscore', 'children'),                
    Output('Average_meanscore', 'children'),                
    Input('Branch_slector', 'value')
)
def update_graph(branch_selected):
    Overall,Simple,Quick,Trust,Worth=T.Score_Generator(branch_selected)
    Dial1.update_traces(value=Overall)
    Dial2.update_traces(value=Simple)    
    Dial3.update_traces(value=Quick)    
    Dial4.update_traces(value=Trust)    
    Dial5.update_traces(value=Worth)                
    Easy_to_Handle_Mean_Branch,Easy_to_Handle_Mean_Total=T.Easy_To_Handle_Score(branch_selected)
    Easy_to_Handle_Mean_to_Text=str(branch_selected)+" : "+str(Easy_to_Handle_Mean_Branch)
    Easy_to_Handle_Mean_Total_to_Text="Average : "+str(Easy_to_Handle_Mean_Total)
    return Dial1,Dial2,Dial3,Dial4,Dial5,Easy_to_Handle_Mean_to_Text,Easy_to_Handle_Mean_Total_to_Text





if __name__=='__main__':
    app.run_server(debug=True)

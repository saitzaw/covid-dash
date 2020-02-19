import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from .helper import Table, Date, Death, Case, Rate, Report

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

colors = {
    'background' : '#111111', 
    'text' : '#8B0000'
    }

app.layout = html.Div([
    html.H5(children='COVID-19 ဗိုင်းရပ်ဒေတာ',
        style={
            'textAlign': 'center',
            'color':colors['text']
        }),
    dcc.Tabs(id="covid19-data", value='covid-19 ဗိုင်းရပ်ဖြစ်စဉ်', children=[
        dcc.Tab(label='သေဆုံးနှုန်း', value='သေဆုံးနှုန်း'),
        dcc.Tab(label='ကူးစက်နှုန်း', value='ကူးစက်နှုန်း'),
        dcc.Tab(label='ကူးစက်သေဆုံးအချိုး', value="အချိုး"),
        dcc.Tab(label='အကျဉ်းချုပ်ဇယား', value="အကျဉ်းချုပ်"),
        dcc.Tab(label='ဖြစ်စဉ်ပြဇယား', value='ဇယား'),
    ]),
    html.Div(id='covid19-virus'),
])

@app.callback(Output('covid19-virus', 'children'),
                [Input('covid19-data','value')])

def render_content(tab):
    if tab == 'သေဆုံးနှုန်း':
        return html.Div([
            html.H3("သေဆုံးနှုန်း"),
            dcc.Graph(
            id = 'graph-death-tabs',
            figure={
                'data': [
                            {'x': Date.date_list ,'y': Death.death('linear')[0],'type': 'bar', 'name':'နေ့စဉ်သေဆုံနှုန်း'},
                            {'x': Date.date_list, 'y': Death.death('linear')[1], 'type': 'bar', 'name':'စုစုပေါင်းသေဆုံနှုန်း'},
                        ],
                'layout': {
                            'title': 'သေဆုံးမှုဖြစ်စဉ်ပြဂရပ်'
                        }
                }
            )
        ])
    if tab == 'အချိုး':
        return html.Div([
            html.H3("ကူးစက်သေဆုံနှုန်းကိုနှိင်းယှဉ်ပြသခြင်း"),
            dcc.Graph(
                id = 'graph-comparison-tabs',
                figure = {
                    'data': [
                            {'x': Date.date_list ,'y': Rate.rate('linear')[0], 'type': 'bar', 'name':'နေ့စဉ်သေဆုံနှုန်း'},
                            {'x': Date.date_list, 'y': Rate.rate('linear')[1], 'type': 'bar', 'name':'စုစုပေါင်းသေဆုံနှုန်း'},
                        ],
                    'layout': {
                            'title': 'ကူးစက်သေဆုံးဖြစ်စဉ်ပြဂရပ်'
                    }

                }
            )
        ])

    if tab == 'အကျဉ်းချုပ်': 
        return html.Div([
            html.H3("အကျဉ်းချုပ်ဖော်ပြချက်"),
            dt.DataTable(
                id = 'table', 
                columns = [{"name":i , "id": i} for i in Table.table_report.columns], 
                data = Table.table_report.to_dict('records'),
            )
        ])

    if tab == 'ဇယား': 
        return html.Div([
            html.H3("ဖြစ်စဉ်ပြဇယား"),
            dt.DataTable(
                id = 'table', 
                columns = [{"name":i , "id": i} for i in Table.table_data.columns], 
                data = Table.table_data.to_dict('records'),
            )
        ])
    
    return html.Div([
        html.H3("ကူးစက်နှုန်း"),
        dcc.Graph(
            id = 'graph-cases-tabs',
            figure={
                'data': [
                            {'x': Date.date_list ,'y': Case.case('linear')[0], 'type': 'bar', 'name':'နေ့စဉ်ကူးစက်နှုန်း'},
                            {'x': Date.date_list, 'y': Case.case('linear')[1], 'type': 'bar', 'name':'စုစုပေါင်းကူးစက်နှုန်း'},
                        ],
                'layout': {
                            'title': 'ဗိုင်းရပ်ကူးစက်နှုန်းပြဂရပ်'
                }
            }
         )
    ])
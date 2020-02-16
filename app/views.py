import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output 

from .helper import Date, Death, Case, Rate

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

colors = {
    'background' : '#111111', 
    'text' : '#7FDBFF'
    }

app.layout = html.Div([
    html.H5(children='ဝူဟန်ဗိုင်းရပ်ဒေတာ',
        style={
            'textAlign': 'center',
            'color':colors['text']
        }),
    dcc.Tabs(id="wuhan-data", value='ဝူဟန် ဗိုင်းရပ်ဖြစ်စဉ်', children=[
        dcc.Tab(label='သေဆုံနှုန်း', value='သေဆုံနှုန်း'),
        dcc.Tab(label="ကူးစက်နှုန်း", value='ကူးစက်နှုန်း'),
        dcc.Tab(label='ကူးစက်သေဆုံအချိုး', value="အချိုး")
    ]),
    html.Div(id='wuhan-virus'),

])

@app.callback(Output('wuhan-virus', 'children'),
                [Input('wuhan-data','value')])

def render_content(tab):
    if tab == 'သေဆုံနှုန်း':
        return html.Div([
            html.H3("သေဆုံနှုန်း"),
            dcc.Graph(
            id = 'graph-death-tabs',
            figure={
                'data': [
                            {'x': Date.date_list ,'y': Death.death('linear')[0],'type': 'bar', 'name':'နေ့စဉ်သေဆုံနှုန်း'},
                            {'x': Date.date_list, 'y': Death.death('linear')[1], 'type': 'bar', 'name':'စုစုပေါင်းသေဆုံနှုန်း'},
                        ],
                'layout': {
                            'title': 'သေဆုံမှုဖြစ်စဉ်ပြဂရပ်'
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
                            'title': 'ကူးစက်သေဆုံဖြစ်စဉ်ပြဂရပ်'
                    }

                }
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


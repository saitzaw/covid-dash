import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output

from .helper import Table, Date, Death, Case, Rate, Report
from .static import TabStyle, TabSelectedStyle

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

colors = {
    'background' : '#C0C0C0', 
    'text' : '#8B0000'
    }

app.layout = html.Div([
    html.H5(children='COVID-19 ဗိုင်းရပ်ဒေတာ',
        style={
            'textAlign': 'center',
            'color':colors['text']
        }),
    html.Br(),
    dcc.Tabs(id="covid19-data", value='covid-19 ဗိုင်းရပ်ဖြစ်စဉ်', children=[
        dcc.Tab(label='သေဆုံးနှုန်း', value='သေဆုံးနှုန်း', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
        dcc.Tab(label='ကူးစက်နှုန်း', value='ကူးစက်နှုန်း', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
        dcc.Tab(label='ကူးစက်သေဆုံးအချိုး', value='အချိုး', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
        dcc.Tab(label='ပျုံ့နှံ့နေသည့်နိုင်ငံများ', value='နိုင်ငံ', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
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
            html.H3("ကူးစက်သေဆုံးနှုန်းကိုနှိင်းယှဉ်ပြသခြင်း"),
            dcc.Graph(
                id = 'graph-comparison-tabs',
                figure = {
                    'data': [
                            {'x': Date.date_list ,'y': Rate.rate('linear')[0], 'type': 'bar', 'name':'နေ့စဉ်ကူးစက်နှုန်း'},
                            {'x': Date.date_list ,'y': Rate.rate('linear')[1], 'type': 'bar', 'name':'နေ့စဉ်သေဆုံနှုန်း'},
                        ],
                    'layout': {
                            'title': 'ကူးစက်သေဆုံးဖြစ်စဉ်ပြဂရပ်'
                    }

                }
            )
        ])

    if tab == 'နိုင်ငံ': 
        PAGE_SIZE = 10
        return html.Div([
            html.H3("covid-19 ပျုံ့နှံ့နေသည့်နိုင်ငံများ"),
            dt.DataTable(
                id = 'country-table',
                columns = [{"name":i, "id":i} for i in Table.table_countries.columns],
                page_current = 0, 
                page_size = PAGE_SIZE, 
                style_data_conditional=[
                    {
                        'if':{'row_index':'odd'},
                        'backgroundColor':'rgb(248,248,248)'
                    },
                    {
                        'if':{'column_id':'စုစုပေါင်းသေဆုံးမှု'},
                        'fontWeight':'bold'
                    },
                     {
                        'if':{'column_id':'ရောဂါပျောက်ကင်းမှု'},
                        'fontWeight':'bold'
                    }
                ],
                style_header={
                    'backgroundColor':'rgb(230,230,230',
                    'fontWeight':'bold'
                },
                data = Table.table_countries.to_dict('records'),
            ),
            html.Br(), 
            dcc.Checklist(
                id='datatable-use-page-count',
        options=[
            {'label': 'Use page_count', 'value': 'True'}
        ],
        value=['True']
            ), 
            'Page count: ',
    dcc.Input(
        id='datatable-page-count',
        type='number',
        min=1,
        max=7,
        value=1
    )
        ])

    return html.Div([
        html.H3("ကူးစက်နှုန်း"),
        dcc.Graph(
            id = 'graph-cases-tabs',
            figure={
                'data': [
                            {'x': Date.date_list, 'y': Case.case('log')[0], 'type': 'line', 'name':'နေ့စဉ်ကူးစက်နှုန်း'},
                            {'x': Date.date_list, 'y': Case.case('log')[1], 'type': 'line', 'name':'စုစုပေါင်းကူးစက်နှုန်း'},
                        ],
                'layout': {
                            'title': 'ဗိုင်းရပ်ကူးစက်နှုန်းပြဂရပ်'
                }
            }
         )
    ])

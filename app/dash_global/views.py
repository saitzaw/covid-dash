import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from . import config as cfg
from dash.dependencies import Input, Output

from .helper import Table, Date, Death, Case, Recovery, Rate, Report
from .static import TitleStyle, TabStyle, TabSelectedStyle, TabIframeStyle, TableHeaderStyle

def global_dash(server):
    external_stylesheet = cfg.css_url
    dash_app = dash.Dash(__name__,server=server, external_stylesheets=external_stylesheet, url_base_pathname='/dashapp/')

    dash_app.layout = html.Div([
        html.H3(children='COVID-19 ဗိုင်းရပ်ဒေတာ',
            style=TitleStyle.title_style),
        html.Br(),
        dcc.Tabs(id="covid19-data", value='covid-19 ဗိုင်းရပ်ဖြစ်စဉ်', children=[
            dcc.Tab(label='သေဆုံးနှုန်း', value='သေဆုံးနှုန်း', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='ကူးစက်နှုန်း', value='ကူးစက်နှုန်း', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='ပျောက်ကင်းနှုန်း',value='ပျောက်ကင်းနှုန်း',style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='လက်ရှိကူးစက်မှုဖြစ်စဉ်', value='လက်ရှိဖြစ်ပွားမှု', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='ကူးစက်သေဆုံးအချိုး', value='အချိုး', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='ပျုံ့နှံ့နေသည့်နိုင်ငံများ', value='နိုင်ငံ', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='မြေပုံ', value='မြေပုံ', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style)
        ]),
        html.Div(id='covid19-virus'),
    ]) 
    @dash_app.callback(Output('covid19-virus', 'children'),
                [Input('covid19-data','value')])

    def render_content(tab):
        if tab == 'သေဆုံးနှုန်း':
            return html.Div([
                html.H3("သေဆုံးနှုန်း"),
                dcc.Graph(
                id = 'graph-death-tabs',
                figure={
                    'data': [
                                {'x': Date.date_list ,'y': Death.death('log')[0],'type': 'bar', 'name':'နေ့စဉ်သေဆုံနှုန်း'},
                                {'x': Date.date_list, 'y': Death.death('log')[1], 'type': 'bar', 'name':'စုစုပေါင်းသေဆုံနှုန်း'},
                            ],
                    'layout': {
                                'title': 'သေဆုံးမှုဖြစ်စဉ်ပြဂရပ်'
                            }
                    }
                )
            ])

        if tab == 'ပျောက်ကင်းနှုန်း': 
            return html.Div([
                html.H3("covid-19 ကူးစက်မှုမှသက်သာလာသည့်လူဦးရေ"),
                dcc.Graph(
                id = 'graph-cured-tabs',
                figure={
                    'data': [
                                {'x': Date.date_list ,'y': Recovery.recovery('linear'),'type': 'line', 'name':'နေ့စဉ်ရောဂါပျောက်ကင်းနှုန်း'},
                            ],
                    'layout': {
                                'title': 'နေ့စဉ်ရောဂါပျောက်ကင်းသည့်ဦးရေ'
                            }
                    }
                )
            ])
        
        if tab == 'လက်ရှိဖြစ်ပွားမှု': 
            return html.Div([
                html.H3("covid-19 လက်ရှိကူးစက်ထားသည့်ဖြစ်စဉ်"),
                dcc.Graph(
                id = 'graph-active-tabs',
                figure={
                    'data': [
                                {'x': Date.date_report,'y': Report.report('active')[0],'type': 'bar', 'name':'လက်ရှိ covid 19 ကူးစက်ထားသည်ပမာဏ'},
                                {'x': Date.date_report,'y': Report.report('active')[1],'type': 'bar', 'name':'ကူးစက်ရောဂါဖြစ်ပွားနေသည့်ပမာဏ'},
                                {'x': Date.date_report,'y': Report.report('active')[2],'type': 'bar', 'name':'စိုးရိမ်ရသည့်အခြေအနေ'},
                            ],
                    'layout': {
                                'title': 'လက်ရှိရောဂါကူးစက်မှုအခြေအနေ'
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
                    style_header = TableHeaderStyle.header_style,
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
            max=9,
            value=1
        )
            ])

        if tab == 'မြေပုံ':
            return html.Iframe(src=cfg.url,style=TabIframeStyle.iframe_style)

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
    return dash_app.server

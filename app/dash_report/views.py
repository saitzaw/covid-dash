import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_table as dt
from . import config as cfg
from dash.dependencies import Input, Output
from .static import TitleStyle, TabStyle, TabSelectedStyle, TabIframeStyle, TableHeaderStyle

def report_dash(server): 

    external_stylesheet = cfg.css_url
    dash_report_app = dash.Dash(__name__,server=server, external_stylesheets=external_stylesheet, url_base_pathname='/dashreport/')

    dash_report_app.layout = html.Div([
        dbc.NavbarSimple(
            children=[dbc.NavLink("Home",href="http://localhost:5000/"),
            ],
        ),
        html.Br(),
        html.H3(children='COVID-19 ဗိုင်းရပ်ဒေတာ',
            style=TitleStyle.title_style),
        html.Br(),
        dcc.Tabs(id="covid19-data", value='covid-19 ဗိုင်းရပ်ဖြစ်စဉ်', children=[
            dcc.Tab(label='သေဆုံးနှုန်း', value='သေဆုံးနှုန်း', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='ကူးစက်နှုန်း', value='ကူးစက်နှုန်း', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='ပျောက်ကင်းနှုန်း',value='ပျောက်ကင်းနှုန်း',style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style),
            dcc.Tab(label='လက်ရှိကူးစက်မှုဖြစ်စဉ်', value='လက်ရှိဖြစ်ပွားမှု', style=TabStyle.tab_style, selected_style=TabSelectedStyle.tab_selected_style)
        ]),
        html.Div(id='covid19-virus'),
    ]) 
    
    @dash_report_app.callback(Output('covid19-virus', 'children'),
                [Input('covid19-data','value')])
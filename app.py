# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os

app = dash.Dash(__name__)
server = app.server

# read data for tables (one df per table)
df_fund_facts = pd.read_csv('https://plot.ly/~bdun9/2754.csv')
df_price_perf = pd.read_csv('https://plot.ly/~bdun9/2756.csv')
df_current_prices = pd.read_csv('https://plot.ly/~bdun9/2753.csv')
df_hist_prices = pd.read_csv('https://plot.ly/~bdun9/2765.csv')
df_avg_returns = pd.read_csv('https://plot.ly/~bdun9/2793.csv')
df_after_tax = pd.read_csv('https://plot.ly/~bdun9/2794.csv')
df_recent_returns = pd.read_csv('https://plot.ly/~bdun9/2795.csv')
df_equity_char = pd.read_csv('https://plot.ly/~bdun9/2796.csv')
df_equity_diver = pd.read_csv('https://plot.ly/~bdun9/2797.csv')
df_expenses = pd.read_csv('https://plot.ly/~bdun9/2798.csv')
df_minimums = pd.read_csv('https://plot.ly/~bdun9/2799.csv')
df_dividend = pd.read_csv('https://plot.ly/~bdun9/2800.csv')
df_realized = pd.read_csv('https://plot.ly/~bdun9/2801.csv')
df_unrealized = pd.read_csv('https://plot.ly/~bdun9/2802.csv')

df_graph = pd.read_csv("https://plot.ly/~bdun9/2804.csv")

# reusable componenets
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='data:image/png;base64,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', height='40', width='140')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Cutting Edge Insole Validation Software')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Arch Height   ', href='/overview', className="tab first"),

        dcc.Link('Foot Width   ', href='/price-performance', className="tab"),

        dcc.Link('Foot Metertarsel   ', href='/portfolio-management', className="tab"),

        #dcc.Link('Fees & Minimums   ', href='/fees', className="tab"),

        #dcc.Link('Distributions   ', href='/distributions', className="tab"),

        #dcc.Link('News & Reviews   ', href='/news-and-reviews', className="tab")

    ], className="row ")
    return menu

## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div(children=([
                    html.H6('Arch  Height ',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),
                    dcc.Input(id='archheight',value=5, type='text'),
                    html.Div(id='arch-height-h'),
                    html.Div(id='footWidth-h')




                ]), className="twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")



pricePerformance = html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row `1`

            html.Div([

                html.Div([
                    html.H6("Foot Width"),
                    html.Div(id='output-b'),
                    dcc.Input(id='footInput',value=0,type='text'),
                    html.Div(id='foot-width-bar'),

                ], className="twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")


portfolioManagement = html.Div([ # page 3

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Portfolio"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(["Stock style"]),
                    dcc.Graph(
                        id='graph-5',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["1"],
                                    y = ["1"],
                                    hoverinfo = "none",
                                    marker = {
                                        "color": ["transparent"]
                                    },
                                    mode = "markers",
                                    name = "B",
                                )
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                {
                                  "x": 0.990130093458,
                                  "y": 1.00181709504,
                                  "align": "left",
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Market<br>Cap</b>",
                                  "xref": "x",
                                  "yref": "y"
                                },
                                {
                                  "x": 1.00001816013,
                                  "y": 1.35907755794e-16,
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Style</b>",
                                  "xref": "x",
                                  "yanchor": "top",
                                  "yref": "y"
                                }
                              ],
                              autosize = False,
                              width = 200,
                              height = 150,
                              hovermode = "closest",
                              margin = {
                                "r": 30,
                                "t": 20,
                                "b": 20,
                                "l": 30
                              },
                              shapes = [
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "dash": "solid",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(255, 127, 14)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 1
                                  },
                                  "opacity": 0.9,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                }
                              ],
                              xaxis = {
                                "autorange": True,
                                "range": [0.989694747864, 1.00064057995],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              },
                              yaxis = {
                                "autorange": True,
                                "range": [-0.0358637178721, 1.06395696354],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )

                ], className="four columns"),

                html.Div([
                    html.P("Vanguard 500 Index Fund seeks to track the performance of\
                     a benchmark index that meaures the investment return of large-capitalization stocks."),
                    html.P("Learn more about this portfolio's investment strategy and policy.")
                ], className="eight columns middle-aligned"),

            ], className="row "),

            # Row 3

            html.Br([]),

            html.Div([

                html.Div([
                    html.H6(["Equity characteristics as of 01/31/2018"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_char), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["Equity sector diversification"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_diver), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")

feesMins = html.Div([  # page 4

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Expenses"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(),
                    html.Table(make_dash_table(df_expenses)),
                    html.H6(["Minimums"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_minimums))
                ], className="six columns"),

                html.Div([
                    html.Br([]),
                    html.Strong("Fees on $10,000 invested over 10 years"),
                    dcc.Graph(
                        id = 'graph-6',
                        figure = {
                            'data': [
                                go.Bar(
                                    x = ["Category Average", "This fund"],
                                    y = ["2242", "329"],
                                    marker = {"color": "rgb(53, 83, 255)"},
                                    name = "A"
                                ),
                                go.Bar(
                                    x = ["This fund"],
                                    y = ["1913"],
                                    marker = {"color": "#ADAAAA"},
                                    name = "B"
                                )
                            ],
                            'layout': go.Layout(
                                annotations = [
                                    {
                                      "x": -0.0111111111111,
                                      "y": 2381.92771084,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "$2,242",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.995555555556,
                                      "y": 509.638554217,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "$329",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.995551020408,
                                      "y": 1730.32432432,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "You save<br><b>$1,913</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 150,
                                  width = 340,
                                  bargap = 0.4,
                                  barmode = "stack",
                                  hovermode = "closest",
                                  margin = {
                                    "r": 40,
                                    "t": 20,
                                    "b": 20,
                                    "l": 40
                                  },
                                  showlegend = False,
                                  title = "",
                                  xaxis = {
                                    "autorange": True,
                                    "range": [-0.5, 1.5],
                                    "showline": True,
                                    "tickfont": {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    "title": "",
                                    "type": "category",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "mirror": False,
                                    "nticks": 3,
                                    "range": [0, 3000],
                                    "showgrid": True,
                                    "showline": True,
                                    "tickfont": {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    "tickprefix": "$",
                                    "title": "",
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Fees"],
                            className="gs-header gs-table-header padded"),

                    html.Br([]),

                    html.Div([

                        html.Div([
                            html.Strong(["Purchase fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")


                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Redemption fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["12b-1 fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Account service fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.Strong(["Nonretirement accounts, traditional IRAs, Roth IRAs, UGMAs/UTMAs, SEP-IRAs, and education savings accounts (ESAs)"]),
                            html.P(["We charge a $20 annual account service fee for each Vanguard Brokerage Account, as well as each individual Vanguard mutual fund holding with a balance of less than $10,000 in an account. This fee does not apply if you sign up for account access on vanguard.com and choose electronic delivery of statements, confirmations, and Vanguard fund reports and prospectuses. This fee also does not apply to members of Flagship Select™, Flagship®, Voyager Select®, and Voyager® Services."]),
                            html.Br([]),
                            html.Strong(["SIMPLE IRAs"]),
                            html.P(["We charge participants a $25 annual account service fee for each fund they hold in their Vanguard SIMPLE IRA. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
                            html.Br([]),
                            html.Strong(["403(b)(7) plans"]),
                            html.P(["We charge participants a $15 annual account service fee for each fund they hold in their Vanguard 403(b)(7) account. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
                            html.Br([]),
                            html.Strong(["Individual 401(k) plans"]),
                            html.P(["We charge participants a $20 annual account service fee for each fund they hold in their Vanguard Individual 401(k) account. This fee will be waived for all participants in the plan if at least 1 participant qualifies for Flagship Select, Flagship, Voyager Select, and Voyager Services"]),
                            html.Br([]),
                        ], className="nine columns")

                    ], className="row ")

                ], className="twelve columns")

            ], className="row "),

        ], className="subpage")

    ], className="page")

distributions = html.Div([  # page 5

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Distributions"],
                            className="gs-header gs-table-header padded"),
                    html.Strong(["Distributions for this fund are scheduled quaterly"])
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Br([]),
                    html.H6(["Dividend and capital gains distributions"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_dividend), className="tiny-header")
                ], className="twelve columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Realized/unrealized gains as of 01/31/2018"], className="gs-header gs-table-header tiny-header")
                ], className=" twelve columns")

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.Table(make_dash_table(df_realized))
                ], className="six columns"),

                html.Div([
                    html.Table(make_dash_table(df_unrealized))
                ], className="six columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")

newsReviews = html.Div([  # page 6

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6('Vanguard News',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    html.P('10/25/16    The rise of indexing and the fall of costs'),
                    html.Br([]),
                    html.P("08/31/16    It's the index mutual fund's 40th anniversary: Let the low-cost, passive party begin")
                ], className="six columns"),

                html.Div([
                    html.H6("Reviews",
                            className="gs-header gs-table-header padded"),
                    html.Br([]),
                    html.Li('Launched in 1976.'),
                    html.Li('On average, has historically produced returns that have far outpaced the rate of inflation.*'),
                    html.Li("Vanguard Quantitative Equity Group, the fund's advisor, is among the world's largest equity index managers."),
                    html.Br([]),
                    html.P("Did you know? The fund launched in 1976 as Vanguard First Index Investment Trust—the nation's first index fund available to individual investors."),
                    html.Br([]),
                    html.P("* The performance of an index is not an exact representation of any particular investment, as you cannot invest directly in an index."),
                    html.Br([]),
                    html.P("Past performance is no guarantee of future returns. See performance data current to the most recent month-end.")
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Input(id='footWidth'),
    dcc.Input(id='archheight'),
    dcc.Input(id='footInput'),
    html.Div(id='footWidth-h'),
    html.Div(id='output-a'),
    html.Div(id='output-b'),
    html.Div(id='arch-height-h'),
    html.Div(id='foot-width-bar'),
    



])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview
    elif pathname == '/price-performance':
        return pricePerformance
    elif pathname == '/portfolio-management':
        return portfolioManagement
    elif pathname == '/fees':
        return feesMins
    elif pathname == '/distributions':
        return distributions
    elif pathname == '/news-and-reviews':
        return newsReviews
    elif pathname == '/full-view':
        return overview,pricePerformance,portfolioManagement,feesMins,distributions,newsReviews
    else:
        return noPage


lowerBound,upperBound = 6,10
#Footwidth response data
@app.callback(
  dash.dependencies.Output(component_id='foot-width-bar',component_property='children'),
  [dash.dependencies.Input('footInput','value')]
  )
def update_output_div(archheight):
    footWidth = int(archheight)
    
    if footWidth < lowerBound: 
      color = 'rgba(255,0,0,1)'
    elif footWidth > upperBound: 
      color = 'rgba(255,0,0,1)'
    else: 
      color = 'rgba(50,171,96,0.7)' 

    print(footWidth)
    trace1 = go.Bar(
      y = ['Certification','Foot Width'],
      x = [lowerBound,0],
      name = 'Correct Plot',
      orientation = 'h',
      marker = dict(
        color = 'rgba(1,1,1,0)'
        )
      )

    trace2 = go.Bar(
      y=['Certification','Foot Width'],
      x=[upperBound,footWidth],
      orientation = 'h',
      name = 'Foot Width',
      marker = dict(
        color = color 
        )
      )
    layout = go.Layout(barmode='stack', title="Ruby Certification | Foot Width")
    traces = [trace1,trace2]
    return dcc.Graph(
      id = 's-bar',
      figure={
      'data':traces, 
      'layout':layout,
      }
      )

 #forefoot response data
@app.callback(
    dash.dependencies.Output(component_id='arch-height-h', component_property='children'),
    [dash.dependencies.Input('archheight','value')]
)
def update_output_div(archheight):
    footWidth = int(archheight)
    
    if footWidth < lowerBound: 
      color = 'rgba(255,0,0,1)'
    elif footWidth > upperBound: 
      color = 'rgba(255,0,0,1)'
    else: 
      color = 'rgba(50,171,96,0.7)' 

    print(footWidth)
    trace1 = go.Bar(
      y = ['Certification','Arch Height'],
      x = [lowerBound,0],
      name = 'Correct Plot',
      orientation = 'h',
      marker = dict(
        color = 'rgba(1,1,1,0)'
        )
      )

    trace2 = go.Bar(
      y=['Certification','Arch Height'],
      x=[upperBound,footWidth],
      orientation = 'h',
      name = 'Arch Height',
      marker = dict(
        color = color 
        )
      )
    layout = go.Layout(barmode='stack', title="Ruby Certification | Arch Height")
    traces = [trace1,trace2]
    return dcc.Graph(
      id = 's-bar',
      figure={
      'data':traces, 
      'layout':layout,
      }
      )
    #return 'You\'ve entered "{}"'.format(footWidth)

 #forefoot response data
@app.callback(
    dash.dependencies.Output(component_id='footWidth-h', component_property='children'),
    [dash.dependencies.Input('archheight','value')]
)

def update_output_div(footWidth):
    footWidth = int(footWidth)
    difference = 0 

    if footWidth < lowerBound: 
      difference = lowerBound - footWidth
      return "You need to add ", difference, " to foot parameter"
    elif footWidth > upperBound: 
      difference = upperBound - footWidth
      return "You need to reduce ", difference, " to foot parameter"
    else: 
      return 'Your foot parameter is valid!'
    #return 'You\'ve entered "{}"'.format(difference)

#forefoot bargraph data response 
@app.callback(
  dash.dependencies.Output('output-a','children'),
  [dash.dependencies.Input('footWidth','value')]
  )
def callback(foot_value):
  foot_value = int(foot_value)

  #Base
  trace1 = go.Bar(
    y = ['validation','Foot Meta.'],
    x = [4,0],
    name='Correct Plot',
    orientation='h',
    marker = dict(
      color = 'rgba(1,1,1,0)',
      )
    )

  #Input Data
  trace2 = go.Bar(
    y = ['validation','Foot Meta.'],
    x = [3,foot_value],
    name='Data plot',
    orientation = 'h',
    marker = dict(
      color = 'rgba(50, 171, 96, 0.7)'
      )
    )
  layout = go.Layout(barmode='stack',autosize='False',
    height=200,width=350, margin = {"r": 10, "t": 25, "b": 30,"l": 80},
    bargap = 0.35,title="Foot Validation")
  traces = [trace1,trace2]
  return dcc.Graph(
    id='h-bar',
    figure={
    'data':traces,
    'layout':layout,
    }
    )

  @app.callback(
    dash.dependencies.Output('output-b','children')
    )
  def callback_b(foot_value):
    foot_value = int(foot_value)
    print(foot_value)

    #Base
    trace1 = go.Bar(
      y = ['validation','Foot Meta.'],
      x = [4,0],
      name='Correct Plot',
      orientation='h',
      marker = dict(
        color = 'rgba(1,1,1,0)',
        )
      )
    trace = [trace1]
    return dcc.Graph(
      id = 'footWidth-bar',
      figure={
      'data':traces
      }
      )


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)

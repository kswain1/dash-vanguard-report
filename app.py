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

#Create object to contain input parameters of client (Brand) foot insole parameters
insole = {"fw":int, "rfw":int, "fml":int, "fthml":int, "ah":int, "hhfm":int, "fl":int, }
foot_insole_difference = {"fw":int, "rfw":int, "fml":int, "fthml":int, "ah":int, "hhfm":int, "fl":int, }

foot_parameter_key_dictionary = {"fw":"Foot Meterasel", "rfw":"Rear Foot Width", "fml":"First Metatarsel Length",
                                 "fthml":"Fifth Metarsel Length", "ah":"Arch Height",
                                 "hhfm":"Heel to head of First Metatarsel Phalangeal Joint",  "fl":"Foot Length"}

app.layout = html.Div([
    
    html.Div(html.H1("Foot Parameter Validator"),),
    html.Label(" Foot Metarsel Validator  "),
    dcc.Input(
        id='dropdown-a',
        #options=[{'label': i, 'value': i} for i in ['Canada', 'USA', 'Mexico']],
        value='0',
        type ='text'),
    html.Div(id='output-a'),
    html.Div(" ------------------------------------ "),

    html.Label(" Rear Foot Width  "),
    dcc.Input(
        id='dropdown-b',
        value='0',
        type='text'
    ),
    html.Div(id='output-b'),
    html.Div(" ------------------------------------ "),


    html.Label(" First Metatarsel Length  "),
     dcc.Input(
        id='dropdown-c',
        value='0',
        type='text'
    ),
    html.Div(id='output-c'),
    html.Div(" --------------------------------------- "), 

    html.Label(" Fifth Metarsel Length "),

     dcc.Input(
        id='dropdown-d',
        value='0',
        type='text'
    ),
    html.Div(id='output-d'),
    html.Div(" --------------------------------------- "), 

    html.Label(" Arch Height "),

     dcc.Input(
        id='dropdown-e',
        value='0',
        type='text'
    ),
    html.Div(id='output-e'),
    html.Div(" --------------------------------------- "), 

    html.Label(" Foot length "),
    dcc.Input(
        id='dropdown-f',
        value='0',
        type='text'
    ),
    html.Div(id='output-f'),
    ], style={'width': '100%',})
upperBound = 10
lowerBound = 5

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]
colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']


# @app.callback(dash.dependencies.Output('blam'))
# def callback():
#     return {'data' : [ go.Pie(labels=labels, values=values,
#                hoverinfo='label+percent', textinfo='value', 
#                textfont=dict(size=20),
#                marker=dict(colors=colors, 
#                            line=dict(color='#000000', width=2)))]
#     }

@app.callback(
    dash.dependencies.Output('output-a', 'children'),
    [dash.dependencies.Input('dropdown-a', 'value')])
def callback_a(dropdown_value):
    #data = str(float(dropdown_value)*2)
    difference = 0 
    print(float(dropdown_value)>5)
    if float(dropdown_value) < lowerBound or float(dropdown_value) > upperBound:
        if float(dropdown_value) < lowerBound:
             difference = lowerBound - float(dropdown_value)
             print("data is lower")
             print(difference)
             return 'Foot Metarsel Add by"{}"'.format(difference)
        if float(dropdown_value) > upperBound:
            difference = upperBound - float(dropdown_value)
            print("data is higher")
            return 'Foot Metarsel Reduce by"{}"'.format(difference)
    print("data is validated")
    return 'Your Measurement is Validate'



@app.callback(
    dash.dependencies.Output('output-b', 'children'),
    [dash.dependencies.Input('dropdown-b', 'value')])
def callback_b(dropdown_value):
    difference = 0 
    print(float(dropdown_value)>5)
    if float(dropdown_value) < lowerBound or float(dropdown_value) > upperBound:
        if float(dropdown_value) < lowerBound:
             difference = lowerBound - float(dropdown_value)
             print("data is lower")
             print(difference)
             return 'Rear Foot Width Add by"{}"'.format(difference)
        if float(dropdown_value) > upperBound:
            difference = upperBound - float(dropdown_value)
            print("data is higher")
            return 'Rear Foot Width Reduce by"{}"'.format(difference)
    print("data is validated")
    return 'Your Measurement is Validate'

@app.callback(
    dash.dependencies.Output('output-c', 'children'),
    [dash.dependencies.Input('dropdown-c', 'value')])
def callback_c(dropdown_value):
    difference = 0 
    print(float(dropdown_value)>5)
    if float(dropdown_value) < lowerBound or float(dropdown_value) > upperBound:
        if float(dropdown_value) < lowerBound:
             difference = lowerBound - float(dropdown_value)
             print("data is lower")
             print(difference)
             return 'First Metatarsel Length Add by"{}"'.format(difference)
        if float(dropdown_value) > upperBound:
            difference = upperBound - float(dropdown_value)
            print("data is higher")
            return 'First Metatarsel Length Reduce by"{}"'.format(difference)
    print("data is validated")
    return 'Your Measurement is Validate'

@app.callback(
    dash.dependencies.Output('output-d', 'children'),
    [dash.dependencies.Input('dropdown-d', 'value')])
def callback_b(dropdown_value):
    difference = 0 
    print(float(dropdown_value)>5)
    if float(dropdown_value) < lowerBound or float(dropdown_value) > upperBound:
        if float(dropdown_value) < lowerBound:
             difference = lowerBound - float(dropdown_value)
             print("data is lower")
             print(difference)
             return 'Fifth Metatarsel Length Add by"{}"'.format(difference)
        if float(dropdown_value) > upperBound:
            difference = upperBound - float(dropdown_value)
            print("data is higher")
            return 'Fifth Metatarsel Length Reduce by"{}"'.format(difference)
    print("data is validated")
    return 'Your Measurement is Validate'

@app.callback(
    dash.dependencies.Output('output-e', 'children'),
    [dash.dependencies.Input('dropdown-e', 'value')])
def callback_b(dropdown_value):
    difference = 0 
    print(float(dropdown_value)>5)
    if float(dropdown_value) < lowerBound or float(dropdown_value) > upperBound:
        if float(dropdown_value) < lowerBound:
             difference = lowerBound - float(dropdown_value)
             print("data is lower")
             print(difference)
             return 'Arch Height Add by"{}"'.format(difference)
        if float(dropdown_value) > upperBound:
            difference = upperBound - float(dropdown_value)
            print("data is higher")
            return 'Arch Height Reduce by"{}"'.format(difference)
    print("data is validated")
    return 'Your Measurement is Validate'

@app.callback(
    dash.dependencies.Output('output-f', 'children'),
    [dash.dependencies.Input('dropdown-f', 'value')])
def callback_b(dropdown_value):
    rdifference = 0 
    print(float(dropdown_value)>5)
    if float(dropdown_value) < lowerBound or float(dropdown_value) > upperBound:
        if float(dropdown_value) < lowerBound:
             difference = lowerBound - float(dropdown_value)
             print("data is lower")
             print(difference)
             return 'Foot Length Add by"{}"'.format(difference)
        if float(dropdown_value) > upperBound:
            difference = upperBound - float(dropdown_value)
            print("data is higher")
            return 'Foot Length Reduce by"{}"'.format(difference)
    print("data is validated")
    return 'Your Measurement is Validate'


if __name__ == '__main__':
    app.run_server(debug=True)
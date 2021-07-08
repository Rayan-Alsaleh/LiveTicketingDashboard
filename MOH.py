import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import requests
import datetime
from dash_extensions import Lottie


external_stylesheets = [dbc.themes.BOOTSTRAP, {'https://codepen.io/chriddyp/pen/bWLwgP.css'}]

# df = pd.read_excel (r'C:\Users\AlSalehRayan(Ascend)\PycharmProjects\COD\TheData.xlsx')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# datetime_obj = datetime.datetime.now()

# app = dash.Dash(external_stylesheets=external_stylesheets,suppress_callback_exceptions= True)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#



#
#
# print(df.Region.unique())
# print(df.Status.unique())
# # print(df.Priority.unique())




#
# raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
# my_dict = raw.json()






# /////////////         NUMBERS CALL FROM API        //////////////



#


def time():
    raw = requests.get('https://worldtimeapi.org/api/timezone/Asia/Riyadh')
    datetime = raw.json()['datetime']
    # print(datetime)
    return "Last Update : {:.20}".format(datetime)






def live_All_tickets():
    raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
    All_tickets = raw.json()['All Tickets']
    # print(All_tickets)
    return "{:,}".format(All_tickets)

def live_opend_tickets():
    raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
    opend_tickets = raw.json()['Opened Tickets']
    # print(opend_tickets)
    return "{:,}".format(opend_tickets)


def live_solved_tickets():
    raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
    solved_tickets = raw.json()['Solved Tickets']
    # print(solved_tickets)
    return "{:,}".format(solved_tickets)

def live_closed_tickets():
    raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
    closed_tickets = raw.json()['CLosed Tickets']
    # print(closed_tickets)
    return "{:,}".format(closed_tickets)


def live_total_teams():

    raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
    total_teams = raw.json()['Total Teams']
    # print(total_teams)
    return "{:,}".format(total_teams)


def live_total_users():
    raw = requests.get('https://nhcc.digitum.com.sa/api/totalDetail')
    total_users = raw.json()['Total Users']
    # print(total_users)
    return "{:,}".format(total_users)







# //////////   CHARTS CALL FROM API    //////////








def live_fig_bar1():
    raw = requests.get('https://nhcc.digitum.com.sa/api/tickets')
    Index = raw.json()
    df = pd.DataFrame(Index)
    ss = df.sort_values(by=['region',"status_id"],na_position='first', ascending=True)
    # print(df.region.unique())
    # print(df.sub_teams.unique())
    # print(df.status_id.unique())
    # print(ss[:20])
    fig_bar1=px.histogram(ss,y="region",histfunc='sum',cumulative=True, color='status_id',orientation='h', color_discrete_map = {
        'closed': '#008755',
        'opened': '#ee4447',
        'solved': '#F2CD00',
        'reopened': '#00ffff',
    },
                            category_orders={
                                "status_id": ["closed", "opened", "solved", "reopened"],
                                "region": ['Eastern Health Cluster', 'Riyadh Health Affairs',
                                          'Qunfotha Health Affairs', 'Jazan Health Affairs', 'Taif Health Affairs',
                                          'Riyadh Second Health Cluster', 'Northern Borders Health Affairs',
                                          'Hafer AlBatin Health Affairs', 'Al-Jouf', 'Asir Health Affairs',
                                          'Tabuk Health Affairs', 'Riyadh Third Health Cluster',
                                          'Jeddah Health Affairs', 'Bisha Health Affairs', 'Qassim Health Cluster',
                                          'Madinah Health Cluster', 'Baha Health Affairs',
                                          'Riyadh First Health Cluster', 'Hail Health Cluster',
                                          'Makkah Health Cluster', 'Al Ahsa Health Cluster',
                                          'Najran Health Affairs',
                                          'Qurayat', 'MOWH', 'Hafer Albatin Health Affairs', 'KSMC']}
    )


    # fig_bar1.update_traces(texttemplate='%{text}', textposition='auto')
    fig_bar1.update_layout(template= "none")
    fig_bar1.update_layout(
        #
        # # autosize=True,
        # width=430,
        height=977,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],

    )
    return (fig_bar1)




#
def live_fig_bar2():
    raw = requests.get('https://nhcc.digitum.com.sa/api/tickets')
    Index = raw.json()
    df = pd.DataFrame(Index)
    ss = df.sort_values(by=['teams','status_id'], ascending=True)
    # print(df.region.unique())
    # print(df[:20])
    fig_bar2=px.histogram(ss,y="teams",histfunc='sum',cumulative=True, color='status_id', orientation='h',color_discrete_map={
        'closed': '#008755',
        'opened': '#ee4447',
        'solved': '#F2CD00',
        'reopened': '#00ffff',

                                                                                                                                 })
    fig_bar2.update_layout(template= "none")
    fig_bar2.update_layout(
        # barmode='stack',
        #
        # # autosize=True,
        # width=430,
        height=977,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],

    )
    return (fig_bar2)




def live_fig_pie():
    raw = requests.get('https://nhcc.digitum.com.sa/api/tickets')
    Index = raw.json()
    df = pd.DataFrame(Index)
    # print(df.region.unique())
    # print(df[:20])
    fig_pie=px.pie(df, names='status_id', color='status_id',hole=.5 ,color_discrete_map={
        'closed': '#008755',
        'opened': '#ee4447',
        'solved': '#F2CD00',
        'reopened': '#00ffff',
                                                                                                                                 })
    fig_pie.update_layout(uniformtext_minsize=5,plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],)
    fig_pie.update_traces(
        textposition='outside',
        textinfo='percent+value+label'

    )
    return (fig_pie)




def live_fig_pie1():
    raw = requests.get('https://nhcc.digitum.com.sa/api/tickets')
    Index = raw.json()
    df = pd.DataFrame(Index)
    # print(df.region.unique())
    # print(df[:20])
    fig_pie1 = px.pie(df, names='priority_id', color='priority_id', hole=.5, color_discrete_map={
        'high': '#ee4447',
        'medium': '#008755',
        'critical': '#F2CD00',
        'low': '#00ffff',
    })
    fig_pie1.update_layout(uniformtext_minsize=5,
                          plot_bgcolor=colors['background'],
                          paper_bgcolor=colors['background'],
                          font_color=colors['text'], )
    fig_pie1.update_traces(
        # texttemplate='{labels}',
        textposition='outside',
        textinfo = 'percent+value+label'

    )
    return (fig_pie1)






# //////////     THE ANIMATIONS PIC     //////////////


url_All_tickets = "https://assets5.lottiefiles.com/packages/lf20_PAYdMt.json"
url_opend_tickets = "https://assets2.lottiefiles.com/private_files/lf30_fZOnb4.json"
url_solved_tickets = "https://assets9.lottiefiles.com/packages/lf20_ajgfzwrc.json"
url_closed_tickets = "https://assets2.lottiefiles.com/datafiles/n0JPfYPBtPNeONY/data.json"
url_total_teams= "https://assets8.lottiefiles.com/packages/lf20_2ZvKfd.json"
url_total_users = "https://assets4.lottiefiles.com/packages/lf20_fgs0c0ni.json"
# url_total_users = "https://assets3.lottiefiles.com/packages/lf20_v43587.json"
# url_datetime="https://assets10.lottiefiles.com/packages/lf20_syoyrvic.json"


options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))



colors = {
    'background': '#333333',
    'text': '#FFFFFF',
    'Div':'#1a1a1a',
  }

#
# fig_bar = px.bar(data_frame=df, y='OrderDate', x='Rep', color='Region', color_discrete_map={
#                                                                           'East': '#239123',
#                                                                           'Central': '#df1752',
#                                                                           'West': '#e6ad00'})

#
#
# fig_bar1 = px.bar(df, y="Rep", x="ID", orientation='h', text='Rep', color='Item',color_discrete_map={
#                                                                           'Pencil': '#239123',
#                                                                           'Binder': '#eb3e71',
#                                                                           'Pen': '#630061',
#                                                                           'Pen Set' : '#008284',
#                                                                           'Desk':'#e6ad00',})

#
#
# fig_bar = px.bar(df, y="Region", x='Status', orientation='h', color='Status',color_discrete_map={
#                                                                           'closed': '#239123',
#                                                                           'opened': '#e6ad00',
#                                                                           'solved': '#630061',
#                                                                           'reopened' : '#008284',
#                                                                                     })
#
# fig_bar.update_traces(texttemplate='%{text}', textposition='auto')

# fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')





#
# fig_pie = px.pie(data_frame=my_dict, names='All Tickets', values='Solved Ticketst', color='Solved Tickets', hole=.5, color_discrete_map={
#                                                                           'Pencil': '#239123',
#                                                                           'Binder': '#eb3e71',
#                                                                           'Pen': '#630061',
#                                                                           'Pen Set' : '#008284',
#                                                                           'Desk':'#e6ad00',})



#
# fig_pie = px.pie(data_frame=df, names='Priority', values='Ticket_Number', color='Priority', hole=.5, color_discrete_map={
#                                                                                                         'high': '#239123',
#                                                                                                         'low': '#e6ad00',
#                                                                                                         'critical': '#630061',
#                                                                                                         'medium': '#008284',
#
#                                                                                                                          })


#
# fig_pie = px.pie(data_frame=df, names='Item', values='Unit Cost', color='Item', hole=.5, color_discrete_map={
#                                                                           'Pencil': '#239123',
#                                                                           'Binder': '#eb3e71',
#                                                                           'Pen': '#630061',
#                                                                           'Pen Set' : '#008284',
#                                                                           'Desk':'#e6ad00',})
#
# fig_sunburst = px.sunburst(data_frame=df, path=['Status', 'Priority'],color='Status', color_discrete_map={
#                                                                           'closed': '#239123',
#                                                                           'opened': '#e6ad00',
#                                                                           'solved': '#630061',
#                                                                           'reopened' :'#008284',
#                                                                           })

#
#
# fig_sunburst = px.sunburst(data_frame=df, path=['Item', 'Rep'], values='Unit Cost',color='Item', color_discrete_map={
#                                                                           'Pencil': '#239123',
#                                                                           'Binder': '#eb3e71',
#                                                                           'Pen': '#630061',
#                                                                           'Pen Set' :'#008284',
#                                                                           'Desk':'#e6ad00',})


#
# fig_pie.update_layout(
#     # autosize=False,
#     # width=400,
#     # height=350,
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
#
# )

#
# fig_sunburst.update_layout(
#     # autosize=False,
#     # width=400,
#     # height=350,
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
#
# )




app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#

# html.Img(src="https://fans.deminasi.com/wp-content/uploads/2020/11/1200px-Saudi_Ministry_of_Health_Logo.svg_-1.png",
#                       style={'width':'126px',
#                              'height':'44px',
#                              'float' : 'right',
# #
#                              }),

# 'NHCC Ticketing Dashboard',style={ 'font-size': '30px',
# 'font-family': 'Times New Roman',
#                     'margin-right': '150px',
#                     'margin-left': '30px',
#
#                     'color': 'White', },






app.layout = dbc.Container([


    #Row 1         (    HEADER     )         ++++++++++++++++++

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H1('NHCC Ticketing Dashboard', style={
                                                        'font-size': '30px',
                                                        'font-family': 'Times New Roman',  },),
                    dcc.Interval(
                        id='time_interval',

                        interval=18*10000,
                        n_intervals=0,
                    ),

                 html.Div(id='time',children=time(), style={'text-align': 'left',
                                                               "color": "#ffbf00",
                                                               "font-weight":"bold",
                                                               "font-size":"17px"}),

html.Img(src="data:image/png;base64,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",
                      style={'width':'178px',
                             'height':'84px',
                             'float' : 'right',
                             'margin-top': '-76px',
                             }),


                ])
            ]),
        ], width=12),
    ],className='mb-3'),









    # Row 2  (      NUMBERS     1 MIN UPDATED ) ++++++++++++++++++









    dbc.Row([

        dbc.Col([
            dbc.Card([



                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_All_tickets)),

                dbc.CardBody([

                    dcc.Interval(
                        id='All_interval',

                        interval=18*10000,
                        n_intervals=0,
                    ),

                    html.H5('All Tickets', style={
                                                          'font-family': 'Arial',
                                                          'text-align':'center',}),

                    html.H2(id='All', children=live_All_tickets(), style={'text-align':'center',})
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([

                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_opend_tickets)),

                dbc.CardBody([
                    dcc.Interval(
                        id='Opened_interval',

                        interval=18*10000,
                        n_intervals=0,
                    ),

                    html.H5('Opened Tickets', style={
                        'font-family': 'Arial',
                        'text-align': 'center', }),

                    html.H2(id='Opened', children=live_opend_tickets(), style={'text-align': 'center', })



                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([

                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_solved_tickets)),

                dbc.CardBody([

                    dcc.Interval(
                        id='Solved_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),

                    html.H6('Solved Tickets', style={
                        'font-family': 'Arial',
                        'text-align': 'center', }),

                    html.H2(id='Solved', children=live_solved_tickets(), style={'text-align': 'center', })


                ])
            ]),
        ], width=2),

        dbc.Col([
            dbc.Card([

                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_closed_tickets)),

                dbc.CardBody([
                    dcc.Interval(
                        id='Closed_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),

                    html.H6('Closed Tickets', style={
                        'font-family': 'Arial',
                        'text-align': 'center', }),

                    html.H2(id='Closed', children=live_closed_tickets(), style={'text-align': 'center', })

                ])
            ]),
        ], width=2),

        dbc.Col([
            dbc.Card([

                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_total_teams)),

                dbc.CardBody([
                    dcc.Interval(
                        id='Teams_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),

                    html.H6('Total Teams', style={
                        'font-family': 'Arial',
                        'text-align': 'center', }),

                    html.H2(id='Teams', children=live_total_teams(), style={'text-align': 'center', })

                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([

                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_total_users)),

                dbc.CardBody([
                    dcc.Interval(
                        id='Users_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),

                    html.H6('Total Users', style={
                        'font-family': 'Arial',
                        'text-align': 'center', }),

                    html.H2(id='Users', children=live_total_users(), style={'text-align': 'center', })

                ])
            ]),
        ], width=2),
    ],className='mb-2'),






    # Row 3 (      CHARTS   3min UPDATED  )++++++++++++++++++






    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                    html.H4('Tickets per Region', style={
                        'font-family': 'Arial',
                         }),

                    dcc.Interval(
                        id='bar1_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),

                    dcc.Graph(

                        id='bar1',
                        figure=live_fig_bar1()
                    ),

                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                    html.H4('Tickets By Teams', style={
                        'font-family': 'Arial',
                    }),

                    dcc.Interval(
                        id='bar2_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),

                    dcc.Graph(

                        id='bar2',
                        figure=live_fig_bar2()
                    ),


                ])
            ]),
        ], width=4),
        dbc.Col([

            dbc.Card([
                dbc.CardBody([
                    html.H4('Tickets Status', style={
                            'font-family': 'Arial',
                    }),
                    dcc.Interval(
                        id='pie_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),


                    dcc.Graph(

                        id='pie',
                        figure=live_fig_pie()
                    ),

                ]),

                dbc.CardBody([
                    html.H4('Tickets Priority', style={
                        'font-family': 'Arial',
                    }),
                    dcc.Interval(
                        id='pie1_interval',
                        interval=18*10000,
                        n_intervals=0,
                    ),
                    dcc.Graph(


                        id='pie1',
                        figure=live_fig_pie1()
                    ),
])

            ]),
        ], width=4),
    ],className='mb-1'),
], fluid=True)










# ////////// CALLBACK NUMBERS DATA //////////////










@app.callback(Output("All","children")
    , [Input("All_interval", "n_intervals")])

def update_n(n_intervals):

    return live_All_tickets()

@app.callback(Output("Opened","children")
    , [Input("Opened_interval", "n_intervals")])

def update_n(n_intervals):

    return live_opend_tickets()


@app.callback(Output("Solved","children")
    , [Input("Solved_interval", "n_intervals")])

def update_n(n_intervals):

    return live_solved_tickets()


@app.callback(Output("Closed","children")
    , [Input("Closed_interval", "n_intervals")])

def update_n(n_intervals):

    return live_closed_tickets()

@app.callback(Output("Teams","children")
    , [Input("Teams_interval", "n_intervals")])

def update_n(n_intervals):

    return live_total_teams()


@app.callback(Output("Users","children")
    , [Input("Users_interval", "n_intervals")])

def update_n(n_intervals):

    return live_total_users()





# ////////// CALLBACK CHARTS DATA //////////////





@app.callback(Output("bar1","figure")
    , [Input("bar1_interval", "n_intervals")])

def update_n(n_intervals):

    return live_fig_bar1()





@app.callback(Output("bar2","figure")
    , [Input("bar2_interval", "n_intervals")])

def update_n(n_intervals):

    return live_fig_bar2()




@app.callback(Output("pie","figure")
    , [Input("pie_interval", "n_intervals")])

def update_n(n_intervals):

    return live_fig_pie()




@app.callback(Output("pie1","figure")
    , [Input("pie1_interval", "n_intervals")])

def update_n(n_intervals):

    return live_fig_pie1()


@app.callback(Output("time","children")
    , [Input("time_interval", "n_intervals")])

def update_n(n_intervals):

    return time()












if __name__ == '__main__':
    app.run_server(debug=True)

import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import pandas as pd

app = Dash(__name__)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Explore Games with BERT embeddings", style={'text-align': 'center'}),

    dcc.Input(
        id="input_number",
        type="number",
        min=3,
        max=14,
        value=8,
        placeholder="Input Number of Clusters",
    ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='input_number', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = pd.read_csv("./dataset/cluster_{}.csv".format(option_slctd))
    dff["cluster"] = dff["cluster"].astype(str)
    container = "You chose {} clusters".format(option_slctd)
    
    # cluster_type = dff["cluster"].astype("category")
    fig = px.scatter(dff, x='x', y='y', color='cluster', 
                color_discrete_sequence=px.colors.qualitative.Pastel,
                hover_data=['Title', 'Genre(s)', 'Publisher(s)'])
    fig.update_xaxes(visible=False, showticklabels=False, showgrid=False, range =[-10, 100])
    fig.update_yaxes(visible=False, showticklabels=False, showgrid=False, range=[-20, 160])

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
# Dash se utiliza para crear una visualización HTML y poder mostrar múltiples gráficos a la vez
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
# Pandas permite leer información de distintos tipos de archivos y manipular la información
import pandas as pd

# Utilizado para inicializar la aplicación
app = Dash(__name__)

# Lee el archivo "1.-Employee Sample Data.xlsx" que debe estar en la misma carpeta que este archivo
df = pd.read_excel(r"./global_superstore_2016.xlsx")

# Se filtran los datos para solo considerar edades mayores a 40
#df=df[df['Age'] > 40]

# Se configura la visualización HTML, por defecto Dash importa todos los archivos CSS que estén en la carpeta "assets", esa carpeta incluye 2 clases row y col
app.layout = html.Div(
    children = [
        # Título, existen distintos niveles de "header" (H1, H2, H3 ... H5)
        html.H1("Informacion de empresas de muebles"),
        # La clase col está definida para que los elementos hijo, estén posicionados uno arriba del otro
        html.Div(
            className="col",
            children=[
                # La clase row está definida para que los elementos hijo, estén posicionados uno al lado del otro
                html.Div(
                    className="row",
                    children=[
                        # La clase card tiene un borde
                        html.Div(
                            className="card"
                        ), html.Div(
                            className="card"
                        ), html.Div(
                            className="card"
                        ), html.Div(
                            className="card"
                        )
                    ]
                ),
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="card",
                                    # En los hijos de un Div de clase card, pueden agregar los gráficos de plotly la siguiente forma
                                    children=[
                                        dcc.Graph(
                                            id='State and Order Date"',
                                            figure=px.scatter(df, 
                                                x="Order Date", 
                                                y="City", 
                                                color="Market"
                                            ),
                                            # El alto es opcional
                                            style={"height": "1000px"}
                                        )
                                    ]
                                )
                            ]
                        ), html.Div(
                            className="col",
                            children=[
                                html.Div(
                                    className="row",
                                    children=[
                                        html.Div(
                                            className="card"
                                        ), html.Div(
                                            className="card"
                                        )
                                    ]
                                ), html.Div(
                                    className="row",
                                    children=[
                                        html.Div(
                                            className="card"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

# Corre un servidor si se ejecuta, el servidor trata de detectar automáticamente los cambios del archivo para actualizarse. 
app.run_server(debug=True)
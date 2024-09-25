import dash
import dash_leaflet as dl
import dash_html_components as html  # Importar componentes HTML para Dash
import geopandas as gpd

# Leer archivo shapefile
gdf = gpd.read_file('FormatoShp/DEPARTAMENTOS_inei_geogpsperu_suyopomalia.shp')

# Reproyectar al sistema de coordenadas EPSG:4326 (WGS 84) si es necesario
if gdf.crs != 'EPSG:4326':
    gdf = gdf.to_crs(epsg=4326)

# Crear GeoJSON a partir del GeoDataFrame
geojson_data = gdf.to_json()

# Inicializar la app de Dash
app = dash.Dash(__name__)

# Crear layout del mapa con Dash Leaflet y otras secciones
app.layout = html.Div([
    html.Div(className='header', children=[
        html.H1("Mapa de Departamentos de Perú", style={'textAlign': 'center'}),
        html.Nav(children=[
            html.Ul(children=[
                html.Li(html.A("Inicio", href="#")),
                html.Li(html.A("Quiénes somos", href="#quienes-somos")),
                html.Li(html.A("Servicios", href="#servicios")),
                html.Li(html.A("Contacto", href="#contacto")),
            ])
        ])
    ]),
    
    html.Div(id='quienes-somos', className='section', children=[
        html.H2("Quiénes somos", style={'textAlign': 'center'}),
        html.P("Somos una empresa dedicada a la visualización de datos geográficos y análisis espacial.")
    ]),
    
    html.Div(id='servicios', className='section', children=[
        html.H2("Servicios", style={'textAlign': 'center'}),
        html.Ul(children=[
            html.Li("Visualización de mapas interactivos."),
            html.Li("Análisis de datos geoespaciales."),
            html.Li("Consultoría en SIG."),
        ])
    ]),
    
    html.Div(id='contacto', className='section', children=[
        html.H2("Contacto", style={'textAlign': 'center'}),
        html.P("Puedes contactarnos a través de nuestro correo electrónico: contacto@empresa.com")
    ]),
    
    dl.Map(center=[-9.19, -75.0152],  # Coordenadas centradas en Perú
           zoom=6,  # Nivel de zoom
           children=[
               dl.TileLayer(),  # Añadir capa de mosaicos (base del mapa)
               dl.GeoJSON(data=geojson_data,  # Añadir GeoJSON al mapa
                          zoomToBounds=True,  # Ajustar el zoom a los límites del GeoJSON
                          hoverStyle={"weight": 5, "color": "red", "dashArray": "5,5"})  # Cambiar estilo al pasar el mouse
           ],
           style={'width': '80%', 'height': '600px', 'margin': 'auto'})  # Cambiar tamaño del mapa
], className='container')  # Añadir clase para el contenedor principal

# Ejecutar servidor de Dash
if __name__ == '__main__':
    app.run_server(debug=True)

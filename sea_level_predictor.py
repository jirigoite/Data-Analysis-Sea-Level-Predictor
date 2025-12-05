import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Leer los datos
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crear Scatter Plot (Diagrama de dispersión)
    # Usamos Year como eje X y CSIRO Adjusted Sea Level como eje Y
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data', s=10)

    # 3. Primera Línea de Regresión (Usando todos los datos: 1880 - Reciente)
    # Calculamos la regresión
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Creamos un rango de años desde el inicio (1880) hasta el 2050 (inclusive)
    # range(start, stop) el stop no se incluye, por eso ponemos 2051
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    # Calculamos los valores de Y usando la fórmula de la recta: y = mx + b
    # res.slope es la pendiente (m), res.intercept es la intersección (b)
    sea_level_pred = res.slope * years_extended + res.intercept
    
    # Dibujamos la línea sobre el scatter plot
    plt.plot(years_extended, sea_level_pred, 'r', label='Best Fit Line (1880-2050)')

    # 4. Segunda Línea de Regresión (Usando solo datos desde el año 2000)
    # Filtramos el DataFrame para obtener solo años >= 2000
    df_recent = df[df['Year'] >= 2000]
    
    # Calculamos la nueva regresión con estos datos recientes
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Creamos un rango de años desde el 2000 hasta el 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    
    # Calculamos la predicción
    sea_level_pred_recent = res_recent.slope * years_recent + res_recent.intercept
    
    # Dibujamos la segunda línea (usualmente muestra una subida más acelerada)
    plt.plot(years_recent, sea_level_pred_recent, 'green', label='Best Fit Line (2000-2050)')

    # 5. Etiquetas y Título (Deben ser exactos para pasar los tests)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # (Opcional) Añadir leyenda para ver qué es cada línea
    plt.legend()

    # Guardar y retornar la figura (requerido por el boilerplate)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
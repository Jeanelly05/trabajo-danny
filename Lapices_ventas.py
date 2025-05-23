import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

#3.Raking de populaidad de boligrafos.
#Tarea:Identificar el tipo de boligrafo que se compra con mas frecuencia.
#Pasos:
#.Cuente el numero de compras por articulo.
#.Orednar en orden descendente
#. Traza un grafico de barras para mayor claridad
#.Visualizacion graficas de barras horizotales (boligarfos mas vendidos)

conteo_de_productos = df_pen_sales["Item"].value_counts()
#print(conteo_de_productos)
plt.figure(figsize = (10,5))
conteo_de_productos.plot(kind="barh", color="green")
plt.title("Ranking de popularidad de productos")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tipo de producto")
plt.gca().invert_yaxis()
plt.show()

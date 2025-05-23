import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

#1.	Rendimiento de las ventas a lo largo del tiempo
#Tarea: Analizar cómo varían las ventas de los diferentes tipos de bolígrafos a lo largo del tiempo.
#Pasos:
#•	Convierta la fecha de compra a un formato de fecha y hora.
#•	Cuenta el número de ventas por mes.
#•	Traza un gráfico de líneas de series temporales para visualizar las tendencias de ventas.
#•	Visualización: 📈 Gráfico de líneas (ventas a lo largo del tiempo – por mes)

df_pen_sales["Purchase Date"] = pd.to_datetime (df_pen_sales["Delivery Date"])
df_pen_sales['Purchase Date'] = pd.to_datetime(df_pen_sales['Purchase Date'], errors='coerce')
df_pen_sales['mes_año'] = df_pen_sales['Purchase Date'].dt.to_period('M').astype(str)
ventas_mes_producto = df_pen_sales.groupby(['mes_año', 'Item']).size().unstack(fill_value=0)

#gráfico de líneas
plt.figure(figsize=(12, 6))
ventas_mes_producto.plot(marker='o')
plt.title("Tendencia de ventas por tipo de bolígrafo a lo largo del tiempo")
plt.xlabel("Mes")
plt.ylabel("Cantidad de ventas")
plt.grid(True)
plt.xticks(rotation=45)
plt.legend(title="Tipo de bolígrafo")
plt.tight_layout()
plt.show()


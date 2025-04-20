import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos CSV
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda1.head()

print(tienda1.head())

# Análisis de facturación
fact_tienda1 = tienda1['Precio'].sum()
fact_tienda2 = tienda2['Precio'].sum()
fact_tienda3 = tienda3['Precio'].sum()
fact_tienda4 = tienda4['Precio'].sum()

facturacion_total_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Ingreso Total': [fact_tienda1, fact_tienda2, fact_tienda3, fact_tienda4]
})

# print(facturacion_total_df.head())

# Visualiza los ingresos totales en gráfico de barras
plt.figure(figsize=(8, 6))  # Establecemos el tamaño de la figura
plt.bar(facturacion_total_df['Tienda'], facturacion_total_df['Ingreso Total'])  # Creamos las barras
plt.xlabel('Tienda')  # Etiquetamos el eje x
plt.ylabel('Ingreso Total')  # Etiquetamos y
plt.title('Ingreso Total por Tienda')  # Tíítulo del gráfico
plt.xticks(rotation=45, ha="right")  # Rotamos las etiquetas del eje x para mejor legibilidad
plt.tight_layout()  # Ajustamos el diseño para evitar que las etiquetas se superpongan
plt.show()  # Mostramos el gráfico

# Imprimir los resultados ---
print("Análisis de Ingresos Totales:")
print(facturacion_total_df)

# Análisis de categorías más vendidas
tienda1 = pd.read_csv(url)
ingresos_categoria_tienda1 = tienda1.groupby('Categoría del producto')['Precio'].sum()
ingresos_categoria_tienda2 = tienda2.groupby('Categoría del producto')['Precio'].sum()
ingresos_categoria_tienda3 = tienda3.groupby('Categoría del producto')['Precio'].sum()
ingresos_categoria_tienda4 = tienda4.groupby('Categoría del producto')['Precio'].sum()

ingresos_por_categoria_df = pd.DataFrame({
    'Tienda 1': ingresos_categoria_tienda1,
    'Tienda 2': ingresos_categoria_tienda2,
    'Tienda 3': ingresos_categoria_tienda3,
    'Tienda 4': ingresos_categoria_tienda4,
}).fillna(0) # Reemplazo con 0 los NaN

num_top_categorias = 3
top_categorias_tienda1 = ingresos_categoria_tienda1.nlargest(num_top_categorias)
top_categorias_tienda2 = ingresos_categoria_tienda2.nlargest(num_top_categorias)
top_categorias_tienda3 = ingresos_categoria_tienda3.nlargest(num_top_categorias)
top_categorias_tienda4 = ingresos_categoria_tienda4.nlargest(num_top_categorias)

top_categorias_tienda1_df = pd.DataFrame({'Categoria': top_categorias_tienda1.index, 'Ingresos': top_categorias_tienda1.values})
top_categorias_tienda2_df = pd.DataFrame({'Categoria': top_categorias_tienda2.index, 'Ingresos': top_categorias_tienda2.values})
top_categorias_tienda3_df = pd.DataFrame({'Categoria': top_categorias_tienda3.index, 'Ingresos': top_categorias_tienda3.values})
top_categorias_tienda4_df = pd.DataFrame({'Categoria': top_categorias_tienda4.index, 'Ingresos': top_categorias_tienda4.values})

print("Análisis de Categorías Más Vendidas:")
print("\nIngresos por Categoría (Comparación entre Tiendas):\n", ingresos_por_categoria_df)

print("\nTop", num_top_categorias, "Categorías - Tienda 1:\n", top_categorias_tienda1_df)
print("\nTop", num_top_categorias, "Categorías - Tienda 2:\n", top_categorias_tienda2_df)
print("\nTop", num_top_categorias, "Categorías - Tienda 3:\n", top_categorias_tienda3_df)
print("\nTop", num_top_categorias, "Categorías - Tienda 4:\n", top_categorias_tienda4_df)

# Análisis de reseñas
calificacion_promedio_tienda1 = tienda1['Calificación'].mean()
calificacion_promedio_tienda2 = tienda2['Calificación'].mean()
calificacion_promedio_tienda3 = tienda3['Calificación'].mean()
calificacion_promedio_tienda4 = tienda4['Calificación'].mean()

calificacion_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Calificación Promedio': [
        calificacion_promedio_tienda1, 
        calificacion_promedio_tienda2, 
        calificacion_promedio_tienda3, 
        calificacion_promedio_tienda4
        ]
})

# Análisis de productos más vendidos
ingresos_por_producto_tienda1 = tienda1.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda2 = tienda2.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda3 = tienda3.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda4 = tienda4.groupby('Producto')['Precio'].sum()

num_top_productos = 5
top_productos_tienda1 = ingresos_categoria_tienda1.nlargest(num_top_productos)
top_productos_tienda2 = ingresos_categoria_tienda2.nlargest(num_top_productos)
top_productos_tienda3 = ingresos_categoria_tienda3.nlargest(num_top_productos)
top_productos_tienda4 = ingresos_categoria_tienda4.nlargest(num_top_productos)

top_productos_tienda1_df = pd.DataFrame({'Producto': top_categorias_tienda1.index, 'Ingresos': top_productos_tienda1.values})
top_productos_tienda2_df = pd.DataFrame({'Producto': top_categorias_tienda2.index, 'Ingresos': top_productos_tienda2.values})
top_productos_tienda3_df = pd.DataFrame({'Producto': top_categorias_tienda3.index, 'Ingresos': top_productos_tienda3.values})
top_productos_tienda4_df = pd.DataFrame({'Producto': top_categorias_tienda4.index, 'Ingresos': top_productos_tienda4.values})

# Análisis de envío promedio
costo_envio_promedio_tienda1 = tienda1['Costo de envío'].mean()
costo_envio_promedio_tienda2 = tienda2['Costo de envío'].mean()
costo_envio_promedio_tienda3 = tienda3['Costo de envío'].mean()
costo_envio_promedio_tienda4 = tienda4['Costo de envío'].mean()

costo_envio_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Costo de envío promedio': [
        costo_envio_promedio_tienda1, 
        costo_envio_promedio_tienda2, 
        costo_envio_promedio_tienda3, 
        costo_envio_promedio_tienda4
        ]
})

# --- 7. Imprimir todos los resultados ---
print("\n--- Análisis Consolidado de Alura Store ---")

print("\n1. Análisis de Ingresos:")
print(facturacion_total_df)

print("\n2. Análisis de Categorías Más Vendidas:")
print("\nIngresos por Categoría (Comparación entre Tiendas):\n", ingresos_por_categoria_df)
print("\nTop 3 Categorías - Tienda 1:\n", top_categorias_tienda1_df)
print("\nTop 3 Categorías - Tienda 2:\n", top_categorias_tienda2_df)
print("\nTop 3 Categorías - Tienda 3:\n", top_categorias_tienda3_df)
print("\nTop 3 Categorías - Tienda 4:\n", top_categorias_tienda4_df)

print("\n3. Análisis de Reseñas de Clientes:")
print("\nCalificación Promedio por Tienda:\n", calificacion_promedio_df)

print("\n4. Análisis de Productos Más Vendidos (por Ingresos):")
print("\nTop 5 Productos - Tienda 1:\n", top_productos_tienda1_df)
print("\nTop 5 Productos - Tienda 2:\n", top_productos_tienda2_df)
print("\nTop 5 Productos - Tienda 3:\n", top_productos_tienda3_df)
print("\nTop 5 Productos - Tienda 4:\n", top_productos_tienda4_df)

print("\n5. Análisis del Envío Promedio:")
print(costo_envio_promedio_df)
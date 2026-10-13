import pandas as pd
import matplotlib.pyplot as plt

# 1. Simular datos extraídos (como si vinieran de tu base de datos)
data = {
    'Categoria': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Ventas': [30, 50, 20, 45]
}
df = pd.DataFrame(data)

print("--- Datos cargados correctamente con Pandas ---")
print(df)

# 2. Generar gráfica de barras
plt.figure(figsize=(6, 4))
df.plot(kind='bar', x='Categoria', y='Ventas', color='skyblue', title='Gráfica de Barras - Ventas')
plt.xlabel('Categoría')
plt.ylabel('Valores')
plt.tight_layout()
plt.savefig('grafica_barras.png')
plt.close()

# 3. Generar gráfica de pastel
plt.figure(figsize=(5, 5))
df.set_index('Categoria')['Ventas'].plot(kind='pie', autopct='%1.1f%%', title='Gráfica de Pastel')
plt.ylabel('') # Ocultar etiqueta extra
plt.tight_layout()
plt.savefig('grafica_pastel.png')
plt.close()

print("¡Gráficas de barras y pastel generadas y guardadas con éxito!")


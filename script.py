# Importación de librerías para manipulación y visualización de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Ingesta y Exploración Estructurada ---
students = pd.read_csv('students.csv')
print(students.head())
print(students.describe())

# --- 2. Cálculo de Métricas Estadísticas (Variable: math_grade) ---
math_mean = students.math_grade.mean()
math_median = students.math_grade.median()
math_mode = students.math_grade.mode()[0]
math_range = students.math_grade.max() - students.math_grade.min()
math_std = students.math_grade.std()

print(f"Media: {math_mean} | Mediana: {math_median} | Moda: {math_mode}")
print(f"Rango Absoluto: {math_range} | Desviación Estándar: {math_std}")

# --- 3. Pipeline de Visualización Numérica ---
# Histograma de frecuencias
sns.histplot(x="math_grade", data=students)
plt.title("Distribución de Calificaciones de Matemáticas")
plt.savefig("histograma_calificaciones.png")  # Exportación de gráfico
plt.close()

# Diagrama de Caja (Box Plot) para detección de cuartiles y outliers
sns.boxplot(x="math_grade", data=students)
plt.title("Diagrama de Caja de Calificaciones")
plt.savefig("boxplot_calificaciones.png")
plt.close()

# --- 4. Análisis de Variables Categóricas (Variable: Mjob) ---
mjob_count = students.Mjob.value_counts()
mjob_count_n = students.Mjob.value_counts(normalize=True)

# Gráfico de Barras de frecuencias categóricas
sns.countplot(x="Mjob", data=students)
plt.title("Distribución de Ocupaciones Maternas")
plt.savefig("barras_ocupacion.png")
plt.close()

# Gráfico de Torta (Pie Chart) de proporciones
students.Mjob.value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Proporción de Trabajos de Madres")
plt.ylabel("")  # Remueve la etiqueta vertical por defecto
plt.savefig("torta_proporciones.png")
plt.close()

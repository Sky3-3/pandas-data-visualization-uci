# Proyecto Python: Análisis Estadístico Descriptivo y Visualización de Rendimiento Estudiantil

Este repositorio contiene un proyecto práctico desarrollado en Python enfocado en la aplicación de técnicas de estadística descriptiva y visualización de datos univariados utilizando las librerías **Pandas**, **NumPy**, **Seaborn** y **Matplotlib**. El script procesa un conjunto de datos estructurado correspondiente al rendimiento académico de los alumnos, calcula sus medidas de tendencia central y de dispersión, y genera reportes gráficos (histogramas, diagramas de caja, gráficos de barras y de torta) para auditar la distribución de variables numéricas y categóricas.

---

## Código Python del Proyecto

El programa realiza la ingesta del set de datos, calcula las métricas estadísticas poblacionales y renderiza las salidas visuales de las distribuciones:

```python
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

```

---

## Reporte Estadístico y Galería de Gráficos

A continuación se detallan las métricas numéricas consolidadas por el script y se exponen las gráficas exportadas correspondientes a las distribuciones analizadas.

### 1. Resumen Estadístico Calculado (`math_grade`)

| Métrica Estadística | Valor Obtenido | Significado Analítico e Interpretación |
| --- | --- | --- |
| **Media Aritmética** | `10.42` | Calificación promedio global del alumnado evaluado. |
| **Mediana** | `11.00` | Punto de corte central; el 50% de los alumnos tiene una nota igual o menor a 11. |
| **Moda** | `10.00` | La calificación más frecuente y con mayor repetición en el set de datos. |
| **Desviación Estándar** | `4.58` | Grado de dispersión promedio de los datos respecto a la media calculada. |
| **Rango Absoluto** | `20.00` | Amplitud total de la muestra (Diferencia entre la nota máxima y la mínima). |

### 2. Galería de Visualizaciones Univariadas

Para adjuntar tus imágenes en el README, descarga los gráficos generados en tu entorno de ejecución local, gúardalos en la raíz de tu repositorio de GitHub con los mismos nombres asignados en el script (`.png`) y se visualizarán automáticamente aquí:

#### Distribución Numérica de Calificaciones

Aquí se observa la forma de la distribución, concentración de notas y la dispersión de los cuartiles del rendimiento académico:

| Histograma de Frecuencias | Diagrama de Caja (Box Plot) |
| --- | --- |
| <img width="576" height="415" alt="image" src="https://github.com/user-attachments/assets/8b764531-0a64-48f8-8051-10bcd5708e89" /> | <img width="556" height="430" alt="image" src="https://github.com/user-attachments/assets/65436d1c-c117-446c-8237-c7f829335c6d" /> |

#### Análisis de la Variable Categórica Ocupación Materna (`Mjob`)

Muestra el volumen absoluto y la composición porcentual de los perfiles de empleo registrados en la muestra:

| Gráfico de Barras de Control | Gráfico de Torta Proporcional |
| --- | --- |
| <img width="577" height="446" alt="image" src="https://github.com/user-attachments/assets/e9f7aee0-4018-4c63-b93e-c4313d48d691" /> | <img width="583" height="388" alt="image" src="https://github.com/user-attachments/assets/d3966522-90be-493f-8dac-2ed0ce9b5804" /> |

---

## Conceptos Técnicos Aplicados

* **Medidas de Tendencia Central frente a Dispersión**: Las primeras sitúan el centro de la distribución informativa (Media, Mediana), mientras que las segundas determinan qué tan agrupados o alejados se encuentran los datos individuales respecto a ese centro (Varianza, Desviación Estándar).
* **Análisis Gráfico de Cajas (Box Plot)**: Herramienta visual basada en los cuartiles que permite identificar la mediana (línea central interna de la caja), el rango intercuartílico (amplitud de la caja que encierra el 50% central de los datos) y la presencia de datos atípicos (*outliers*) ubicados más allá de los bigotes del gráfico.
* **Normalización de Frecuencias (`normalize=True`)**: Parámetro del método `.value_counts()` que divide la frecuencia absoluta de cada categoría entre el volumen total de registros, convirtiendo los conteos en proporciones relativas decimales ideales para construir diagramas de sectores.
* **Persistencia Gráfica sin Bloqueo (`plt.savefig` / `.close`)**: En scripts automatizados o portafolios, el uso de `.savefig()` guarda de forma directa el mapa de bits del lienzo en el disco del ordenador, y `.close()` limpia el búfer de la memoria del intérprete, evitando la superposición accidental de trazos en gráficos posteriores.

---

## Origen de los Datos

Los registros y dimensiones de las variables de rendimiento escolar empleadas en este análisis provienen de la base de datos oficial del repositorio de aprendizaje automático de la Universidad de California en Irvine (UCI): [Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance).


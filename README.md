#  Punto limpio, punto sesgo

##  Descripción
Este proyecto analiza el acceso a los **Puntos Limpios en Madrid** con especial atención a su distribución socioespacial.  
El objetivo es identificar posibles sesgos en la planificación que afecten la equidad en el acceso a estas infraestructuras ambientales.

---

##  Hipótesis
- La distribución de los puntos limpios podría reflejar sesgos sociales o territoriales.  
- Los barrios más ricos estarían más alejados de los puntos limpios fijos.  
- La ubicación no seguiría necesariamente niveles de renta o educación.  
- Las personas que podrían necesitar residuos de alto valor como fuente de ingresos tienen menos acceso a los puntos limpios que los reciben.  

---

##  Datasets
```python
ds_puntos_limpios = "Localización de puntos limpios fijos (Ayuntamiento de Madrid)"
ds_renta = "Renta media de los hogares por barrio (INE / Ayuntamiento de Madrid)"
ds_demografia = "Características demográficas por barrio (INE)"
ds_malla_espacial = "Cartografía barrios y distritos (Geoportal Madrid)"
```

---

##  Estructura del proyecto
```
PuntoLimpioProyecto/
├─ README.md                 ← descripción general del proyecto
├─ definicion_EDA.md         ← documento con la definición del análisis exploratorio
├─ data/
│  └─ raw/                   ← datos brutos (CSV, shapefiles, etc.)
├─ memoria/
│  └─ presentacion.pptx      ← presentación del proyecto
├─ graficos/                 ← mapas, curvas y visualizaciones exportadas
├─ notebooks/
│  └─ eda.py                 ← script de Python con el análisis exploratorio
```

---

## Metodología
1. Recolección y limpieza de datos espaciales y socioeconómicos.  
2. Cálculo de distancias a puntos limpios fijos.  
3. Análisis comparativo con renta media y características demográficas.  
4. Visualización de resultados en mapas y gráficos.  

---

##  Limitaciones
- Duración corta del proyecto.  
- Datos incompletos y necesidad de estimaciones.  
- Estudio centrado en **puntos limpios fijos**, sin incluir móviles o de proximidad.  

---

##  Resultados esperados
- Identificación de desigualdades socioespaciales en el acceso.  
- Comprobación de si barrios ricos o vulnerables están más alejados de los puntos limpios.  
- Discusión del riesgo de **exclusión social ligada a residuos de valor**.  

---

##  Cómo reproducir el análisis
1. Clonar el repositorio o descargar el proyecto.  
2. Instalar dependencias principales:  
   ```bash
   pip install pandas geopandas matplotlib seaborn
   ```  
3. Ejecutar el script en `notebooks/eda.py`.  

---

## Autor
Pierre - Michel Joassaint
mi primer proyecto EDA 



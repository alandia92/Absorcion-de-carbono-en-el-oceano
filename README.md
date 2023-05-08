# Predicción de la absorción de carbono  y puntos de muestreo en el oceano
## Proyecto de machine learning para el bootcamp de data science

El dataset se puede encontrar en https://www.kaggle.com/datasets/nosmax/glodapv2-ocean-data y hay más información en https://cdiac.ess-dive.lbl.gov/ftp/oceans/GLODAPv2/Data_Products/

El dataset GLODAPv2 Ocean Data es una colección de mediciones y estimaciones relacionadas con la química del océano, obtenidas de diferentes expediciones de investigación realizadas entre los años 1972 y 2013. Estos datos incluyen mediciones de temperatura, salinidad, oxígeno disuelto, dióxido de carbono y otros parámetros relacionados con la química del agua de mar, en diferentes profundidades del océano en todo el mundo.

El dataset consta de 101 columnas y 15260 filas,, incluyendo mediciones en el Atlántico, el Pacífico, el Índico, el Antártico y el Ártico. Los datos se han sometido a procesos de calidad y control, para asegurar que sean lo más precisos y precisos posible.

Este dataset es una herramienta útil para la investigación y el análisis de la dinámica oceánica y la química del agua de mar en diferentes regiones y profundidades del océano. Además, puede ser utilizado en la construcción de modelos y simulaciones para entender mejor el impacto del cambio climático en el océano y en el planeta en general.

## Predicción de CO2 
La concentración de CO2 total en el agua del océano es importante para comprender el ciclo del carbono en el océano y cómo afecta al clima global. Los estudios oceanográficos pueden medir la concentración de CO2 total en diferentes ubicaciones geográficas y profundidades en el océano para comprender cómo varía a lo largo del tiempo y el espacio. Esta información es útil para modelar el ciclo del carbono en el océano y para predecir cómo puede cambiar en el futuro debido al aumento de la concentración de CO2 en la atmósfera.

### Selección de columnas
    • "tco2" concentración de CO2 total en el agua del océano. Este va a ser el dato a predecir
    • "phosphate": los niveles de fosfato en el agua pueden ser un factor importante en la proliferación de algas.
    • "nitrate": los niveles de nitrato en el agua también pueden influir en el crecimiento de las algas.
    • "silicate": los niveles de silicato pueden ser importantes para ciertas especies de algas que requieren silicio para su crecimiento.
    • "oxygen": los niveles de oxígeno disuelto en el agua pueden ser importantes para la supervivencia de las algas y otros organismos acuáticos.
    • "salinity": la salinidad del agua puede afectar la composición de las comunidades de algas.
    • "temperature": la temperatura del agua puede influir en la tasa de crecimiento de las algas y en la composición de la comunidad de algas.
    • "depth": la profundidad del agua puede influir en la cantidad y tipo de luz disponible para las algas, lo que puede afectar su crecimiento y composición.
    • "pressure": la presión del agua puede influir en la disponibilidad de nutrientes y otros factores que afectan el crecimiento de las algas.
    • "phts25p0":  está relacionado con el equilibrio químico del sistema carbonato en el agua de mar. El pH afecta la concentración de iones de carbonato y bicarbonato, que a su vez afecta la concentración de dióxido de carbono disuelto en el agua. Además, el pH también influye en la solubilidad de otros elementos químicos.

Se realizan varias pruebas con distintos modelos de machine learning
> Linear regression

> Regularización

> RandomForestRegressor

> GradientBoostingRegressor

El modelo con mejores resultados es RandomForestRegressor\
MSE 197.72\
R2 0.98

## Predicción de puntos de muestreo

Conocer los puntos de muestreo es esencial en cualquier estudio científico relacionado con el medio ambiente, y en particular en el estudio de los océanos. Los puntos de muestreo son los lugares en los que se han tomado las mediciones de las variables estudiadas, como en el anterior caso el tco2 en el agua.

Conocer los puntos de muestreo permite tener una idea más precisa de la distribución geográfica del tco2 en el océano y, por lo tanto, de las condiciones de absorción de CO2 en el agua. Además, los puntos de muestreo pueden ayudar a identificar posibles patrones en la distribución del tco2, lo que a su vez puede ser útil para predecir su comportamiento en otras áreas del océano.

Dentro del dataset se encuentran más mediciones que el tco2. Se podrían hacer varias predicciones como el análisis de la circulación oceánica. El conjunto de datos puede ser utilizado para estudiar la circulación oceánica, que es un factor clave en la distribución de nutrientes, la distribución de especies y la regulación del clima global.

Por lo tanto, los puntos de muestreo son una pieza clave en la investigación y el estudio en los océanos.

### Selección de columnas
En este modelo se hans eleccionado las anteriores columnas y se han añadido las de 'longitude' y 'latitude', que van a ser las columnas a predecir.

### Modelo ML
Para esta prediccion se ha utilizado RandomForestRegressor utilizando GridSearchCV para evaluar diferentes parametros.\
R2 media 0.86\
R2 longitud 0.75\
MSE longitud 2475.84\
R2 latitud 0.97\
MSE latitud 51.41\

## Conclusiones
El modelo de prediccion de co2 es bastente preciso y el modelo de predicción de los puntos de muestreo hace falta pulirlo más, ya que hay bastabte fallo.
Si el modelo es preciso y confiable, puede tener importantes aplicaciones prácticas.  
Este dataset puede ser utilizado para ayudar a predecir los efectos del cambio climático en los ecosistemas oceánicos y cómo afectará la vida humana.

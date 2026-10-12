## Laboratorio 3: Sistema de Búsqueda

## 1. El problema

Una institución educativa necesita construir un sistema para administrar la información de sus estudiantes.

Se dispone de un conjunto de registros de estudiantes. Cada registro contiene, como mínimo:

- ID: número único de matrícula.

- Nombre: nombre del estudiante.

- Edad: edad del estudiante.

- Promedio: promedio académico.

El sistema debe permitir realizar las siguientes operaciones:

- 1. Buscar un estudiante a partir de su ID.

- 2. Insertar un nuevo estudiante.

- 3. Listar todos los estudiantes en orden ascendente de ID.

## Pregunta central del taller

Realizar estudios estadísticos sobre las distintas implementaciones, y mostrar como escala la solución del problema a medida que la complejidad y dificultad cambia. Las propuestas metodológicas y estadísticas son parte de la evaluación.

## Objetivo

El objetivo principal es estudiar experimentalmente cómo diferentes estrategias de almacenamiento y búsqueda afectan el tiempo de ejecución del programa a medida que aumenta el tamaño de los datos. Las conclusiones deberán estar sustentadas en mediciones experimentales y análisis estadístico.

Importante: Implemente el sistema utilizando al menos tres estrategias diferentes de almacenamiento y búsqueda: Listas, ABB y B+

El repositorio debe incluir

- Códigos

- Gráficas (debe estar en el repositorio, sin necesidad de correr todos los experimentos para reproducirlas)

- Readme

- Código de honor

- Material de apoyo que permita al estudiante sustentar su trabajo


## Sugerencias a tener en cuenta:

- El orden en que se insertan los estudiantes puede afectar considerablemente el comportamiento de un árbol binario de búsqueda.

- IDs aleatorios, Los estudiantes se insertan utilizando IDs distribuidos de manera aleatoria.

- IDs ordenados, Los estudiantes se insertan siguiendo un orden creciente ID.

- No se debe evaluar únicamente el caso de 10.000 estudiantes. El objetivo es estudiar cómo escala el tiempo de ejecución cuando aumenta N.

- Para estudiar la operación de búsqueda:

- 1. Genere un conjunto de IDs de búsqueda.

- 2. Realice M búsquedas aleatorias, M también es un parámetro

## Para tener en cuenta en el entregable:

Deberán realizar un estudio estadístico de los resultados que permita determinar cómo cambia el rendimiento de las diferentes implementaciones.

Como mínimo, el informe deberá incluir:

- número de ejecuciones;

- promedio;

- desviación estándar;

- tamaño de entrada N, M; otros parámetros?

- tiempo de ejecución;

- gráficas de los resultados;

- interpretación de las tendencias observadas.

Las propuestas metodológicas y estadísticas forman parte de la evaluación.

Las gráficas deberán permitir comparar las diferentes implementaciones, deben incluir:

- título;

- nombres de los ejes;

- unidades;

- leyenda;

- descripción clara de qué representa cada curva;

- suficientes datos para interpretar el comportamiento.

La responsabilidad sobre la veracidad de las gráficas y su interpretación es del estudiante.

El análisis deberá responder preguntas como:

- ¿Los resultados se comportan como predice la complejidad teórica?

- ¿En qué situaciones el árbol binario deja de comportarse como O(log⁡N)?

- ¿Qué relación existe entre la altura del árbol y el tiempo de búsqueda?

- ¿Qué ocurre cuando los datos se insertan ordenadamente?


- ¿Qué diferencias aparecen entre los casos aleatorios y ordenados?

- ¿A partir de qué tamaño de entrada comienzan a ser claramente visibles las diferencias?

- ¿Existen costos constantes que hagan que dos algoritmos con diferente complejidad tengan tiempos similares para entradas pequeñas?

## Sustentación

El estudiante debe poder:

- Describir el problema y objetivo del experimento.

- Describir las estructuras de datos y algoritmos utilizados.

- Descripción detallada de:

- hardware;

- software;

- tamaños de entrada;

- número de repeticiones;

- generación de los datos;

- generación de las búsquedas;

- método utilizado para medir los tiempos;

- tratamiento de valores atípicos;

- estadísticas utilizadas.

- Tablas y gráficas de los experimentos.

- Interpretación de los resultados y comparación con las predicciones teóricas.

- Principales hallazgos del experimento.

- Instrucciones suficientes para que otra persona pueda repetir los experimentos.

## Evaluación

La evaluación tendrá en cuenta tanto la implementación como la calidad del estudio experimental.

Se considerarán, entre otros aspectos:

- Implementaciones Correctas.

- Correcta utilización de las estructuras de datos.

- Diseño de los experimentos.

- Selección y justificación de los tamaños de entrada.

- Calidad de las mediciones.

- Análisis estadístico.

- Calidad y veracidad de las gráficas.

- Relación entre resultados experimentales y complejidad teórica.

- Capacidad para explicar los resultados.

- Calidad de las conclusiones.

- Reproducibilidad del experimento.

- Se evaluará la capacidad del estudiante para explicar qué representan los datos, qué limitaciones tiene el experimento y qué conclusiones pueden o no pueden obtenerse de ellos.


# Nota: Uso de herramientas de IA

Se permite el uso de herramientas de inteligencia artificial durante el desarrollo del taller. Recuerde agregar al repositorio la información del uso de herramientas de IA, según el código de honor enviado previamente. Sin embargo, utilizar una herramienta de IA no exime

al estudiante de verificar que:

- 1. los datos utilizados sean reales;

- 2. los cálculos sean correctos;

- 3. las gráficas representan correctamente los datos;

- 4. las conclusiones correspondan a los resultados obtenidos.

La IA puede utilizarse, por ejemplo, para:

- consultar conceptos;

- generar o corregir código;

- sugerir métodos estadísticos;

- automatizar la generación de datos;

- producir gráficas;

- ayudar a redactar el informe.

## Sin embargo, el estudiante es responsable del resultado final.

En particular, no se aceptará como justificación:

"La IA generó la gráfica/conclusión."

El estudiante debe poder explicar:

- de dónde provienen los datos;

- qué se está midiendo;

- qué significa cada gráfica;

- por qué se eligió determinada metodología;

- qué significan las estadísticas calculadas;

- si las conclusiones están respaldadas por los datos.

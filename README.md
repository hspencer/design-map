# Mapa del Diseño

Este es un mapa construido a partir de las materias y sus relaciones en el campo del Diseño en el contexto formativo de la Escuela de Arquitectura y Diseño PUCV.

### Datos
Los datos están estructurados en una [planilla compartida](https://docs.google.com/spreadsheets/d/1qheFYhrfnUIKpc87ENJQO1ezpZ_3XYXOw20wP6GpaNU/edit?usp=sharing) que se publica en formato [CSV](https://docs.google.com/spreadsheets/d/e/2PACX-1vQZQVwSSUsyoYEA6Wj8bYtDbgzKVf8I1ewmnp8697gks7-WnawxLjqwgGX51L1Sk_8Qex3CSezVVYzm/pub?gid=1147217014&single=true&output=csv) y es consumida por la visualización. La estructura de los datos se ordena de la siguiente manera:

| **Materia** | **EAD** | **Relación 1** | **Relación 2** | **Relación 3** | **...** | **Relación 10** |
|-------------|---------|----------------|----------------|----------------|---------|-----------------|
| Tipografía  | sí      | Observación    | Dibujo         | Presentación   |         |                 |

1. La primera columna (Materia) nombra una materia y define un nodo del grafo
2. La segunta columna (EAD) define si esa materia existe, no existe o potencialmente puede existir en el currículum. Los valores permitidos son: _sí_, _no_, _potencial_
3. Desde la tercera columna (Relación N) se nombran las materias relacionadas, o aquellas materias necesarias para definir la Materia (Columna 1). El conteo de relaciones (veces que una materia es requerida) determinará el tamaño del nodo.

**&rarr; [ver mapa](http://hspencer.github.io/design-map)**
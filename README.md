# Mapa del Diseño

Este es un mapa construido a partir de las materias y sus relaciones en el campo del Diseño en el contexto formativo de la Escuela de Arquitectura y Diseño PUCV.

### Datos
Los datos están estructurados en una [planilla compartida](https://docs.google.com/spreadsheets/d/10Y4lf12X5LMDLnnClRoYhbfUiy7_N78HIkFqIY2VtmY/edit?usp=sharing) que se publica en formato [CSV](https://docs.google.com/spreadsheets/d/e/2PACX-1vRH7srxOeUb950beVHfXg6RckjZL1axbyHBfoR6oXbGhpdX2F2-1bUpN6a64LqmHd01QsHEH_c0Kawa/pub?gid=1339882215&single=true&output=csv) y es consumida por la visualización. La estructura de los datos se ordena de la siguiente manera:

| **Materia** | **Escuela** | **Relación 1** | **Relación 2** | **Relación 3** | **...** | **Relación 10** |
|-------------|---------|----------------|----------------|----------------|---------|-----------------|
| Tipografía  | 1      | Observación    | Dibujo         | Presentación   |         |                 |

1. La primera columna (Materia) nombra una materia y define un nodo del grafo
2. La segunta columna (Escuela) define si esa materia existe, no existe o potencialmente puede existir en el currículum. Los valores permitidos son: _1_ o _0_ (podríamos incorporar algo "potencial")
3. Desde la tercera columna (Relación N) se nombran las materias relacionadas, o aquellas materias necesarias para definir la Materia (Columna 1). El conteo de relaciones (veces que una materia es requerida) determinará el tamaño del nodo.

**&rarr; [ver mapa](http://hspencer.github.io/design-map)**

### Controles

- La vista 3D permite orbitar, hacer _zoom_ y hacer _pan_.
- _Rollover_ sobre una materia (cambia a rojo) y doble click la centra
- Los temas en color café claro corresponden a aquellas materias que no se imparten en la Escuela


### Variaciones
- [01](/01/): versión 2D con nodos y tooltips y exportación de SVG
- [02](/02/): versión 3D con nodos y tooltips
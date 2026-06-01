# Guion para Video del Proyecto 3

Duracion objetivo: 4:30 a 5:00 minutos. No te pases de 5 minutos porque el enunciado dice que resta puntos.

## Preparacion

Antes de grabar, abri estas ventanas:

- Terminal en la raiz del proyecto.
- `docs/informe.pdf` abierto.
- `src/project_activities.py` abierto en el editor.
- Repositorio de GitHub abierto: `https://github.com/Jonialen/proyecto3`.

Comandos que vas a ejecutar:

```bash
uv run pytest
uv run python -m src.main --project-activities
```

## Estructura del Video

| Tiempo | Que mostrar | Que decir |
| --- | --- | --- |
| 0:00-0:25 | Portada del PDF | "Soy Jonathan Diaz, carne 23837. Este es el Proyecto 3 de Analisis de Algoritmos, sobre Move-To-Front, IMTF, analisis amortizado y algoritmos on-line." |
| 0:25-0:55 | GitHub repo | "El proyecto esta en este repositorio publico. La implementacion es propia y esta organizada en `src/`, con pruebas en `tests/` y el reporte en `docs/`." |
| 0:55-1:35 | `src/project_activities.py` | "La parte principal del enunciado esta implementada aqui. `run_mtf_access_cost` calcula el costo de acceso por posicion y luego mueve el elemento al frente. `run_imtf_access_cost` implementa IMTF usando mirada hacia adelante." |
| 1:35-2:10 | Terminal: `uv run pytest` | "Primero verifico que todo pase con pruebas automatizadas. Uso `uv` para ejecutar el entorno. Las pruebas validan las secuencias oficiales, minimo, peor caso, repeticiones e IMTF." |
| 2:10-3:25 | Terminal: `uv run python -m src.main --project-activities` | "Este comando imprime las respuestas solicitadas por el enunciado: configuracion, solicitud, costo y resultado por cada paso. Los totales son: actividad 1 igual a 90, actividad 2 igual a 67, minimo 20, peor caso 100, repeticion de 2 igual a 22, repeticion de 3 igual a 23, IMTF sobre minimo 20 e IMTF sobre peor caso 60." |
| 3:25-4:15 | Seccion `Actividades solicitadas` del PDF | "En el reporte estan resumidas las respuestas. El minimo se logra pidiendo siempre el elemento al frente, por eso cuesta 20. El peor caso pide siempre el ultimo elemento, por eso cada solicitud cuesta 5 y el total es 100." |
| 4:15-4:45 | Seccion de IMTF o codigo IMTF | "IMTF mejora el peor caso de MTF porque no mueve elementos al frente si no vuelven a aparecer dentro de la ventana de mirada hacia adelante. Por eso en la secuencia peor de MTF baja de 100 a 60." |
| 4:45-5:00 | Conclusiones del PDF | "La conclusion es que MTF aprovecha localidad de referencia, pero puede ser castigado por secuencias adversariales. IMTF evita algunos movimientos innecesarios usando informacion futura limitada." |

## Texto Sugerido Completo

Hola, soy Jonathan Diaz, carne 23837. En este video voy a mostrar brevemente mi implementacion del Proyecto 3 de Analisis de Algoritmos.

El proyecto trabaja con el algoritmo Move-To-Front, o MTF, y con una variante mejorada llamada IMTF. El objetivo es calcular costos de acceso sobre listas autoorganizables y observar como cambia la configuracion de la lista despues de cada solicitud.

Primero muestro el repositorio. El codigo esta organizado en `src/`, las pruebas estan en `tests/` y el reporte esta en `docs/`. La parte especifica del enunciado esta en `src/project_activities.py`.

En `run_mtf_access_cost`, para cada solicitud se toma la posicion actual del elemento como costo de acceso. Luego se mueve ese elemento al frente de la lista. Por eso el programa guarda la configuracion antes del acceso, la solicitud, el costo y la configuracion resultante.

Tambien implemente `run_imtf_access_cost`. En IMTF, despues de acceder al elemento en posicion `i`, solo se mueve al frente si ese mismo elemento aparece en las proximas `i - 1` solicitudes. Esa es la parte de look-ahead del algoritmo.

Ahora ejecuto las pruebas con `uv run pytest`. Estas pruebas validan las secuencias oficiales del enunciado, el minimo, el peor caso, las repeticiones de 2 y 3, y el comportamiento de IMTF. Todas pasan correctamente.

Ahora ejecuto `uv run python -m src.main --project-activities`. Este comando imprime las respuestas solicitadas. Para la primera secuencia, el costo total de acceso con MTF es 90. Para la segunda secuencia, el costo total es 67.

Para el minimo de 20 solicitudes, la mejor secuencia es pedir siempre 0, porque 0 ya esta al frente en la configuracion inicial. Entonces cada acceso cuesta 1 y el total es 20.

Para el peor caso, se pide siempre el ultimo elemento de la configuracion actual. Con la lista de cinco elementos, cada acceso cuesta 5. Una secuencia que logra esto es repetir cuatro veces `[4, 3, 2, 1, 0]`, con costo total 100.

Para la repeticion del elemento 2 veinte veces, el primer acceso cuesta 3 porque 2 esta en la tercera posicion. Despues queda al frente y los otros 19 accesos cuestan 1. El total es 22. Para repetir el elemento 3, el primer acceso cuesta 4 y luego 19 accesos cuestan 1, entonces el total es 23. El patron general es posicion inicial mas 19.

Finalmente, para IMTF, sobre la secuencia minima de MTF el costo sigue siendo 20. Sobre la secuencia peor de MTF, IMTF obtiene 60 porque evita mover elementos al frente cuando no vuelven a aparecer pronto. Asi conserva mejor la configuracion y reduce el costo.

Como conclusion, MTF es util cuando hay localidad de referencia, porque los elementos repetidos quedan al frente. Pero puede ser malo ante secuencias adversariales. IMTF intenta corregir eso usando una mirada hacia adelante limitada para evitar movimientos innecesarios.

## Checklist Antes de Subir

- [ ] El video dura menos de 5 minutos.
- [ ] Se ve el repositorio de GitHub.
- [ ] Se ve el comando `uv run pytest` pasando.
- [ ] Se ve el comando `uv run python -m src.main --project-activities`.
- [ ] Se mencionan los costos: 90, 67, 20, 100, 22, 23, 20 y 60.
- [ ] Se muestra el PDF o el reporte con las respuestas.
- [ ] El video se sube a YouTube como no listado.
- [ ] El enlace del video se pega en `docs/informe.md` y se regenera `docs/informe.pdf`.

# Diseno del Proyecto

Este proyecto implementa y evalua algoritmos on-line para el problema de actualizacion de listas. El foco no es solo ejecutar algoritmos, sino mostrar como el analisis competitivo y el metodo del potencial explican el comportamiento de estrategias como `Move-to-Front` y `BIT` frente a una referencia offline.

## Objetivo

Construir una simulacion reproducible del problema del diccionario/lista que permita comparar algoritmos on-line bajo distintas secuencias de solicitudes.

El proyecto debe evidenciar:

- Como opera un algoritmo on-line cuando no conoce el futuro.
- Como se calcula el costo real de acceso, insercion, eliminacion e intercambio.
- Como `Move-to-Front` usa localidad de referencia para reducir costos futuros.
- Como el metodo del potencial permite comparar `MTF` contra una referencia optima o arbitraria.
- Como se interpreta la proporcion competitiva en datos experimentales.

## Alcance

El proyecto se limita al problema de listas lineales descrito en el material del curso.

Operaciones soportadas:

- `access(x)`: buscar el elemento `x`.
- `insert(x)`: insertar un nuevo elemento.
- `delete(x)`: buscar y eliminar el elemento `x`.
- `swap(i, i + 1)`: intercambio adyacente usado internamente para mover elementos.

Algoritmos incluidos:

- `StaticList`: mantiene el orden original y sirve como linea base simple.
- `MoveToFront`: mueve el elemento accedido o insertado al inicio de la lista.
- `Bit`: alterna un bit por elemento y mueve al frente solo cuando el bit queda en `1`.
- `OfflineOptimalReference`: referencia offline para secuencias pequenas, usada para comparar resultados y explicar el concepto de adversario/optimo.

Fuera de alcance:

- Probar optimalidad formal general del algoritmo offline.
- Implementar estructuras avanzadas no relacionadas con listas autoorganizables.
- Optimizar rendimiento de bajo nivel por encima de claridad del analisis.

## Modelo de Costos

El simulador debe usar el mismo modelo del material.

| Operacion | Costo |
| --- | --- |
| Acceder elemento en posicion `i` | `i` |
| Eliminar elemento en posicion `i` | `i` |
| Insertar en lista de tamano `n` | `n + 1` |
| Intercambio adyacente | `1` |

Las posiciones son 1-indexadas para coincidir con el analisis del curso.

Para `MTF`, acceder un elemento en posicion `k` cuesta:

```text
costo_acceso + costo_movimiento = k + (k - 1) = 2k - 1
```

## Potencial

La funcion de potencial compara dos configuraciones de lista.

```text
Phi(L_alg, L_ref) = numero de inversiones entre L_alg y L_ref
```

Una inversion es un par `(x, y)` donde `x` aparece antes que `y` en una lista, pero despues en la otra.

Esta funcion permite calcular el costo amortizado:

```text
a_i = t_i + Delta Phi
```

Donde:

- `a_i` es el costo amortizado del evento.
- `t_i` es el costo real del algoritmo analizado.
- `Delta Phi` es el cambio de potencial despues de procesar la solicitud.

## Arquitectura Propuesta

```text
proyecto3/
  README.md
  docs/
    _ADA__Analisis_amortizado__cont_-1-1.pdf
    diseno-proyecto.md
  src/
    main.py
    algorithms/
      base.py
      static_list.py
      move_to_front.py
      bit.py
      offline_optimal.py
    analysis/
      costs.py
      potential.py
      competitive.py
    experiments/
      generators.py
      runner.py
      report.py
  tests/
    test_costs.py
    test_potential.py
    test_algorithms.py
  data/
    examples/
      repeated_accesses.json
      adversarial_sequence.json
```

## Responsabilidades

| Modulo | Responsabilidad |
| --- | --- |
| `algorithms/base.py` | Define la interfaz comun de los algoritmos. |
| `algorithms/static_list.py` | Implementa lista sin reorganizacion. |
| `algorithms/move_to_front.py` | Implementa la heuristica `MTF`. |
| `algorithms/bit.py` | Implementa la variante `BIT` con bits por elemento. |
| `algorithms/offline_optimal.py` | Calcula una referencia offline exacta para secuencias pequenas de solo accesos. |
| `analysis/costs.py` | Centraliza el modelo de costos. |
| `analysis/potential.py` | Calcula inversiones y cambios de potencial. |
| `analysis/competitive.py` | Calcula razones competitivas empiricas. |
| `experiments/generators.py` | Genera secuencias de prueba. |
| `experiments/runner.py` | Ejecuta algoritmos sobre las mismas solicitudes. |
| `experiments/report.py` | Produce tablas/resumen para el informe. |

## Flujo de Ejecucion

1. Cargar una lista inicial y una secuencia de solicitudes.
2. Ejecutar cada algoritmo sobre una copia independiente de la lista.
3. Registrar por evento el costo real, la lista resultante y las operaciones internas.
4. Calcular potencial entre `MTF` y la referencia seleccionada.
5. Calcular costo amortizado de `MTF`.
6. Comparar costos totales y razones competitivas empiricas.
7. Generar un reporte legible con tablas y conclusiones.

El CLI actual ejecuta este flujo con archivos JSON:

```bash
uv run python -m src.main data/examples/repeated_accesses.json --bit-seed 1
```

Para incluir la referencia offline:

```bash
uv run python -m src.main data/examples/repeated_accesses.json --bit-seed 1 --include-offline --reference OfflineOptimalReference
```

La referencia offline usa programacion dinamica sobre todas las permutaciones de la lista. Por eso se limita a listas pequenas y a operaciones `access`; esta restriccion evita que el costo factorial opaque el objetivo pedagogico del proyecto.

## Experimentos Minimos

| Experimento | Proposito |
| --- | --- |
| Accesos repetidos al mismo elemento | Mostrar localidad de referencia favorable para `MTF`. |
| Accesos uniformes aleatorios | Comparar comportamiento promedio de `StaticList`, `MTF` y `BIT`. |
| Secuencia adversarial | Mostrar que un algoritmo on-line puede ser forzado a pagar mas. |
| Secuencia con inserciones y eliminaciones | Validar que el modelo del diccionario completo funciona. |
| Secuencia pequena con optimo offline | Ilustrar analisis competitivo contra referencia con conocimiento del futuro. |

## Criterios de Aceptacion

- El simulador ejecuta al menos `StaticList`, `MTF` y `BIT` sobre la misma secuencia.
- Cada operacion reporta costo real usando posiciones 1-indexadas.
- `MTF` reporta costo de movimiento al frente mediante intercambios adyacentes.
- El potencial por inversiones se calcula correctamente entre dos listas con los mismos elementos.
- El reporte muestra costo total por algoritmo y razon contra la referencia.
- Hay pruebas unitarias para costos, potencial y comportamiento basico de los algoritmos.
- El informe final conecta los resultados experimentales con la teoria del material.

## Riesgos y Decisiones

| Tema | Decision |
| --- | --- |
| Lenguaje | Python, por claridad para simulacion, pruebas y reportes. |
| Herramienta | `uv` para gestion del entorno, dependencias y ejecucion. |
| Optimo offline | DP sobre permutaciones, acotado a secuencias pequenas de solo accesos para evitar complejidad factorial. |
| Aleatoriedad de `BIT` | Permitir semilla fija para resultados reproducibles. |
| Reportes | Generar tablas simples antes que visualizaciones complejas. |
| Enfoque | Priorizar trazabilidad del analisis sobre micro-optimizaciones. |

## Entregables

- Codigo fuente del simulador.
- Pruebas unitarias.
- Secuencias de ejemplo.
- Reporte experimental con resultados.
- Explicacion teorica breve del metodo del potencial y analisis competitivo.

## Plan de Implementacion

1. Implementar modelo de operaciones y costos.
2. Implementar `StaticList` y pruebas basicas.
3. Implementar `MoveToFront` y validar costos `2k - 1`.
4. Implementar calculo de inversiones/potencial.
5. Implementar `BIT` con semilla reproducible.
6. Implementar runner de experimentos.
7. Agregar referencia offline limitada para secuencias pequenas.
8. Generar reportes y ejemplos.
9. Escribir informe final conectando teoria y resultados.

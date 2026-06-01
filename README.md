# Proyecto 3: Algoritmos On-line

Proyecto de simulacion y analisis para algoritmos on-line aplicados al problema de actualizacion de listas.

## Proposito

El objetivo es aplicar conceptos de analisis amortizado, metodo del potencial y analisis competitivo mediante la implementacion de algoritmos como `Move-to-Front` y `BIT`.

## Enfoque

El proyecto compara algoritmos que procesan solicitudes sin conocer el futuro contra una referencia offline o linea base. La comparacion se realiza con costos reales, costos amortizados y razones competitivas empiricas.

## Algoritmos Propuestos

| Algoritmo | Idea principal |
| --- | --- |
| `StaticList` | Mantiene el orden inicial de la lista. |
| `MoveToFront` | Mueve al frente cada elemento accedido o insertado. |
| `Bit` | Usa un bit por elemento para decidir si moverlo al frente. |
| `OfflineOptimalReference` | Referencia con conocimiento de la secuencia, acotada a casos pequenos. |

## Documentacion

- `docs/_ADA__Análisis_amortizado__cont_-1-1.pdf`: material base del curso.
- `docs/diseno-proyecto.md`: diseno completo propuesto para implementacion.
- `docs/informe.md`: informe del proyecto en Markdown.
- `docs/informe.pdf`: informe generado con `pandoc`.
- `docs/guion-video.md`: guia breve para grabar el video de entrega.
- `docs/resultados/`: salidas CLI usadas como respaldo del informe.

## Uso con uv

Instalar dependencias de desarrollo:

```bash
uv sync --dev
```

Ejecutar la simulacion de ejemplo:

```bash
uv run python -m src.main
```

Ejecutar un experimento especifico:

```bash
uv run python -m src.main data/examples/adversarial_sequence.json --bit-seed 1
```

Incluir la referencia offline exacta para experimentos pequenos de solo accesos:

```bash
uv run python -m src.main data/examples/repeated_accesses.json --bit-seed 1 --include-offline --reference OfflineOptimalReference
```

Imprimir las respuestas del enunciado oficial del Proyecto 3:

```bash
uv run python -m src.main --project-activities
```

Ejecutar pruebas:

```bash
uv run pytest
```

Generar el informe PDF con `pandoc`:

```bash
pandoc docs/informe.md -o docs/informe.pdf --pdf-engine=xelatex
```

## Estado

Diseno inicial creado e implementacion base iniciada en `src/` con pruebas en `tests/`. El CLI ya carga experimentos JSON y genera un reporte con costos, razones competitivas empiricas, analisis de potencial para `MoveToFront` y una referencia offline exacta para secuencias pequenas de solo accesos.

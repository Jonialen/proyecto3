# Resultados: actividades oficiales Proyecto 3

Comando ejecutado:

```bash
uv run python -m src.main --project-activities
```

Resumen de respuestas:

| Actividad | Secuencia / caso | Costo total |
| --- | --- | ---: |
| 1 | `[0, 1, 2, 3, 4]` repetido 4 veces | 90 |
| 2 | `[4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]` | 67 |
| 3 | Minimo: `[0]` repetido 20 veces | 20 |
| 4 | Peor caso: `[4, 3, 2, 1, 0]` repetido 4 veces | 100 |
| 5 | `[2]` repetido 20 veces | 22 |
| 5 | `[3]` repetido 20 veces | 23 |
| 6 | IMTF sobre minimo de MTF | 20 |
| 6 | IMTF sobre peor caso de MTF | 60 |

Patron de repeticion:

```text
costo = posicion_inicial + 19
```

La salida completa por solicitud se imprime con el comando anterior e incluye configuracion antes del acceso, solicitud, costo y configuracion resultante.

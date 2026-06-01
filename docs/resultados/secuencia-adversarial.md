# Resultado: secuencia adversarial

Comando ejecutado:

```bash
uv run python -m src.main data/examples/adversarial_sequence.json --bit-seed 1 --include-offline --reference OfflineOptimalReference
```

Salida:

```text
Reference: OfflineOptimalReference

Summary:
Algorithm | Total cost | Ratio | Final state
--- | ---: | ---: | ---
StaticList | 10 | 1.00 | ['A', 'B', 'C', 'D']
MoveToFront | 28 | 2.80 | ['A', 'B', 'C', 'D']
Bit | 21 | 2.10 | ['A', 'B', 'D', 'C']
OfflineOptimalReference | 10 | 1.00 | ['A', 'B', 'C', 'D']

MoveToFront potential analysis:
Step | Item | Real cost | Phi | Delta Phi | Amortized cost
---: | --- | ---: | ---: | ---: | ---:
1 | D | 7 | 3 | 3 | 10
2 | C | 7 | 4 | 1 | 8
3 | B | 7 | 3 | -1 | 6
4 | A | 7 | 0 | -3 | 4
```

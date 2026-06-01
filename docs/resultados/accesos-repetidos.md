# Resultado: accesos repetidos

Comando ejecutado:

```bash
uv run python -m src.main data/examples/repeated_accesses.json --bit-seed 1 --include-offline --reference OfflineOptimalReference
```

Salida:

```text
Reference: OfflineOptimalReference

Summary:
Algorithm | Total cost | Ratio | Final state
--- | ---: | ---: | ---
StaticList | 16 | 2.29 | ['A', 'B', 'C', 'D']
MoveToFront | 10 | 1.43 | ['D', 'A', 'B', 'C']
Bit | 10 | 1.43 | ['D', 'A', 'B', 'C']
OfflineOptimalReference | 7 | 1.00 | ['D', 'A', 'B', 'C']

MoveToFront potential analysis:
Step | Item | Real cost | Phi | Delta Phi | Amortized cost
---: | --- | ---: | ---: | ---: | ---:
1 | D | 7 | 0 | 0 | 7
2 | D | 1 | 0 | 0 | 1
3 | D | 1 | 0 | 0 | 1
4 | D | 1 | 0 | 0 | 1
```

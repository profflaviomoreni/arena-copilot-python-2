# Arena Copilot – FIAP Next 2025 – TDS

**Tempo total:** 20 min (5 leitura + 15 execução com Copilot)  
**Stack:** VS Code + GitHub Copilot + Python + Pytest  
**Branch:** `master` (commit e push ao final)

## Objetivo
Resolver 3 funções com problemas em `src/desafios.py` utilizando **GitHub Copilot** para diagnosticar, refatorar e validar via testes automatizados.

## Funções
1. `eh_palindromo(texto)` – Deve considerar normalização: minúsculas, remoção de espaços, pontuação e **acentos**.
2. `intersecao_unica(lista1, lista2)` – Interseção **sem duplicatas** e **ordenada**.
3. `soma_intervalos(intervalos)` – Soma do comprimento de **intervalos unidos** em [início, fim). Intervalos que **se tocam** devem ser mesclados.

## Como rodar
```bash
python src/app.py
python -m src.app
python -m pytest -q
python -m unittest discover
```

## Como finalizar (commit & push)
```bash
git add .
git commit -m "fix: arena-copilot <seu_nome>"
git push origin master
```

> Você pode pedir ao Copilot: *"Liste os comandos git para commitar e fazer push na branch master."*

## Critérios de avaliação
- **Correção (40%)** – Passa nos testes
- **Eficiência (30%)** – Evita O(n²) desnecessário; usa estruturas adequadas
- **Clareza (20%)** – Código limpo e legível
- **Uso do Copilot (10%)** – Prompts inteligentes e iterativos

© FIAP Next 2025 – Arena Copilot TDS

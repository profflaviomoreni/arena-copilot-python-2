# ATENÇÃO: ESTE ARQUIVO CONTÉM PROBLEMAS INTENCIONAIS.
# Use o Copilot para diagnosticar e corrigir.

import unicodedata

def eh_palindromo(texto: str) -> bool:
    if not isinstance(texto, str):
        return False
    # PROBLEMA: não normaliza adequadamente, não remove não alfanumérico
    t = texto.lower().replace(" ", "")
    return t == t[::-1]

def intersecao_unica(lista1, lista2):
    inter = []
    for x in lista1:
        for y in lista2:
            if x == y:
                inter.append(x)
    return inter  # sem deduplicar/ordenar

def soma_intervalos(intervalos):
    if not intervalos:
        return 0
    intervalos = sorted(intervalos, key=lambda x: x[1])
    total = 0
    atual_ini, atual_fim = intervalos[0]
    for ini, fim in intervalos[1:]:
        if ini < atual_fim:  # não considera toque ini == atual_fim
            atual_fim = max(atual_fim, fim)
        else:
            total += (atual_fim - atual_ini)
            atual_ini, atual_fim = ini, fim
    total += (atual_fim - atual_ini)
    return total

import unicodedata
import re
from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")

def _remover_acentos(s: str) -> str:
   
    if not isinstance(s, str):
        return ""

    nf = unicodedata.normalize("NFD", s)
    sem_acentos = "".join(ch for ch in nf if unicodedata.category(ch) != "Mn")

    # minusculiza e remove quaisquer caracteres que não sejam a-z ou 0-9
    sem_acentos = sem_acentos.lower()
    return re.sub(r"[^a-z0-9]", "", sem_acentos)

def eh_palindromo(texto: str) -> bool:

    if not isinstance(texto, str):
        return False

    # prepara o texto: _remover_acentos já faz lower() e limpa
    s = _remover_acentos(texto)

    return s == s[::-1]

def intersecao_unica(lista1: Iterable[T], lista2: Iterable[T]) -> List[T]:
  
    set1, set2 = set(lista1), set(lista2)
    inter = set1 & set2
    try:
        return sorted(inter)
    except TypeError:
        # fallback determinístico para elementos não comparáveis diretamente
        return sorted(inter, key=lambda x: (str(type(x)), str(x)))

def soma_intervalos(intervalos: Iterable[Tuple[int,int]]) -> int:
    """Soma o comprimento da união de vários intervalos.

    Cada intervalo é um par (inicio, fim). A função aceita que inicio > fim
    e normaliza trocando quando necessário. Intervalos que se tocam
    (fim == inicio) são mesclados. Retorna a soma dos comprimentos
    (fim - inicio) dos intervalos mesclados.
    """
    iv = [tuple(i) for i in intervalos]
    if not iv:
        return 0

    # normalize cada intervalo para (ini, fim) com ini <= fim
    iv = [(a, b) if a <= b else (b, a) for (a, b) in iv]
    # ordenar por início
    iv.sort(key=lambda x: x[0])

    total = 0
    cur_ini, cur_fim = iv[0]

    for ini, fim in iv[1:]:
        # ini, fim já normalizados
        if ini <= cur_fim:  # mescla se toca (fim == ini) ou sobrepõe
            if fim > cur_fim:
                cur_fim = fim
        else:
            total += (cur_fim - cur_ini)
            cur_ini, cur_fim = ini, fim

    total += (cur_fim - cur_ini)
    return total

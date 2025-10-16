import sys
from src.desafios import eh_palindromo, intersecao_unica, soma_intervalos

def main():
    print("== Arena Copilot - Demo ==\n")

    exemplos = [
        ("eh_palindromo", eh_palindromo, ["À sogra má e amargosa"]),
        ("intersecao_unica", intersecao_unica, [[1,2,2,3], [2,2,4]]),
        ("soma_intervalos", soma_intervalos, [[(1,5),(3,7),(10,11)]]),
    ]

    for nome, fn, args in exemplos:
        try:
            resultado = fn(*args) if isinstance(args, list) else fn(args)
            print(f"{nome}({args}) => {resultado}")
        except Exception as e:
            print(f"{nome} falhou com {args}: {e}")

if __name__ == "__main__":
    sys.exit(main())

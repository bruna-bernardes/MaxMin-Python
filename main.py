from typing import List, Tuple

def maxmin_recursivo(array: List[float], inicio: int, fim: int) -> Tuple[float, float, int]:

    n = fim - inicio + 1

    # 1 elemento
    if n == 1:
        return array[inicio], array[inicio], 0

    # 2 elementos
    if n == 2:
        if array[inicio] < array[fim]:
            return array[inicio], array[fim], 1
        else:
            return array[fim], array[inicio], 1

    # n >= 3: divide e conquista
    meio = (inicio + fim) // 2
    menor_esquerda, maior_esquerda, comparacoes_esquerda = maxmin_recursivo(array, inicio, meio)
    menor_direita, maior_direita, comparacoes_direita  = maxmin_recursivo(array, meio + 1, fim)

    # Combinação com 2 comparações
    total_comparacoes = comparacoes_esquerda + comparacoes_direita
    
    total_comparacoes += 1  # compara menores
    menor_global = menor_esquerda if menor_esquerda < menor_direita else menor_direita
    
    total_comparacoes += 1  # compara maiores
    maior_global = maior_esquerda if maior_esquerda > maior_direita else maior_direita

    return menor_global, maior_global, total_comparacoes

def maxmin(array: List[float]) -> Tuple[float, float, int]:
    
    if not array:
        raise ValueError("A sequência não pode ser vazia.")
    return maxmin_recursivo(array, 0, len(array) - 1)

def formata_num(valor):
    return int(valor) if valor.is_integer() else valor

if __name__ == "__main__":
    import sys

    def converter_entrada(valor):
        if '.' in valor or ',' in valor:
            return float(valor.replace(',', '.'))
        return int(valor)

    if len(sys.argv) > 1:
        try:
            nums = [converter_entrada(x) for x in sys.argv[1:]]
        except ValueError:
            print("Erro: todos os argumentos devem ser números.")
            sys.exit(1)
    else:
        linha = input("\nInforme os números separados por espaço: ").strip()
        try:
            nums = [converter_entrada(x) for x in linha.split()]
        except ValueError:
            print("Erro: todos os valores devem ser números.")
            sys.exit(1)

    menor, maior, comparacoes = maxmin(nums)
    print(f"Menor = {menor}")
    print(f"Maior = {maior}")
    print(f"Comparações = {comparacoes}")

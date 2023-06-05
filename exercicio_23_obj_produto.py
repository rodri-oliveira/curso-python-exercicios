# copy, sorted, produtos.sort
# Exercícios


import copy

from dados import produtos

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos_dez_porcento = [
    {**p, 'preco': round(p['preco'] * 1.10, 2)} 
    for p in copy.deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
novos_produtos_ordenados = sorted(
    copy.deepcopy(produtos), key=lambda p: p['nome']
)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
novos_produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos), key=lambda p: p['preco']
)

novos_produtos_ordenados = sorted(
    copy.deepcopy(produtos), key=lambda p: p['nome'],
    reverse=True
)

print()

print('Ordenado por nome(maior para menor)',*novos_produtos_ordenados, sep='\n')

print()

print('Ordenado por preco(menor para maior)',*novos_produtos_ordenados_preco, sep='\n')

print()

print('Preço aumentado em 10 %',*novos_produtos_dez_porcento, sep='\n')








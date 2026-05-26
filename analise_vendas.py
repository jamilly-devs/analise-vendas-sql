import pandas as pd

produtos = pd.DataFrame({
    'id_produto': [1, 2, 3, 4, 5],
    'produto': ['Notebook', 'Smartphone', 'Cadeira Gamer', 'Monitor', 'Teclado Mecânico'],
    'categoria': ['Eletrônicos', 'Eletrônicos', 'Móveis', 'Eletrônicos', 'Periféricos'],
    'preco': [3500, 1800, 1200, 900, 350]
})

clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nome': ['Ana Silva', 'Carlos Souza', 'Mariana Lima', 'Pedro Alves', 'Fernanda Costa'],
    'cidade': ['São Paulo', 'Belo Horizonte', 'Curitiba', 'Salvador', 'Fortaleza'],
    'estado': ['SP', 'MG', 'PR', 'BA', 'CE']
})

vendas = pd.DataFrame({
    'id_venda': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'id_cliente': [1, 3, 5, 2, 1, 4, 3, 2, 5, 4],
    'id_produto': [2, 1, 3, 4, 1, 2, 5, 3, 4, 1],
    'quantidade': [1, 1, 2, 1, 1, 2, 3, 1, 2, 1],
    'data_venda': ['2024-01-15', '2024-02-10', '2024-03-05', '2024-03-20',
                   '2024-04-01', '2024-05-15', '2024-06-10', '2024-07-22',
                   '2024-08-30', '2024-09-12']
})

print('Produtos:')
print(produtos)
print('\nClientes:')
print(clientes)
print('\nVendas:')
print(vendas)

vendas_completas = vendas.merge(produtos, on='id_produto')
print(vendas_completas)

vendas_completas['receita'] = vendas_completas['quantidade'] * vendas_completas['preco']
print(vendas_completas[['id_venda', 'produto', 'quantidade', 'preco', 'receita']])

receita_categoria = vendas_completas.groupby('categoria')['receita'].sum()
print(receita_categoria)

vendas_completas.to_csv('vendas_completas.csv', index=False)
print('Arquivo salvo com sucesso!')
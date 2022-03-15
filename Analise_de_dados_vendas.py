import pandas as pd

df = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/Vendas.xlsx")
df.head()

faturamento_total = df["Valor Final"].sum()
faturamento_total

# Descobrir faturamento por loja
faturamento_por_loja = df[["ID Loja","Valor Final"]]
faturamento_por_loja.head()

#agrupar as lojas e aplicar a soma  no valor final
faturamento_por_loja.groupby("ID Loja").sum()

faturamento_por_produto = df[['ID Loja',"Produto","Valor Final"]]
faturamento_por_produto.groupby(["ID Loja","Produto"]).sum()

# com base no dataframe faturamento_por_produto podemos notar que a venda de bermuda lisa no Iguatemi campinas
# teve um "boom" de vendas e parece ser exlusivo da loja(entrar em contato com a loja para ter certeza)
#sendo assim um modo de aumentar o faturamento nao somente dessa loja em questao mas de todas
# seria produzir mais bermudas lisas e vender em todas
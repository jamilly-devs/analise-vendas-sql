# 📊 Análise de Vendas com SQL

Projeto de análise de dados utilizando SQL para responder perguntas reais de negócio sobre o desempenho de vendas de uma loja de tecnologia.

---

## 🎯 Objetivo

Explorar um banco de dados de vendas e extrair insights estratégicos usando consultas SQL, desde agregações básicas até subqueries avançadas.

---

## 🗃️ Estrutura do Banco de Dados

O banco é composto por 3 tabelas relacionadas:

```
clientes (id_cliente, nome, cidade, estado)
produtos (id_produto, nome, categoria, preco)
vendas   (id_venda, id_cliente, id_produto, quantidade, data_venda)
```

**35 registros de vendas** · **10 clientes** · **10 produtos** · **3 categorias** · **12 meses (2024)**

---

## 🔍 Análises Realizadas

### 1. Receita total por produto
> Qual produto gerou mais receita no ano?

**Resultado:** Notebook liderou com R$ 21.000 — quase o dobro do segundo colocado (Smartphone, R$ 12.600).

```sql
SELECT 
  p.nome AS produto,
  SUM(v.quantidade * p.preco) AS receita_total
FROM vendas v
JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY p.nome
ORDER BY receita_total DESC;
```

---

### 2. Receita mensal
> Como as vendas evoluíram ao longo de 2024?

**Resultado:** Junho foi o melhor mês (R$ 8.000). Fevereiro e Julho os piores (R$ 1.910 e R$ 1.600), indicando sazonalidade e oportunidade para ações promocionais.

```sql
SELECT
  strftime('%m/%Y', data_venda) AS mes,
  SUM(v.quantidade * p.preco) AS receita_total
FROM vendas v
JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY mes
ORDER BY data_venda;
```

---

### 3. Ticket médio por categoria
> Qual categoria tem maior valor médio por venda?

**Resultado:** Eletrônicos lideram com ticket médio de R$ 2.540 e 15 vendas — categoria mais lucrativa. Periféricos têm alto volume (13 vendas) mas ticket baixo (R$ 476).

```sql
SELECT
  p.categoria,
  ROUND(AVG(v.quantidade * p.preco), 2) AS ticket_medio,
  COUNT(v.id_venda) AS total_vendas
FROM vendas v
JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY p.categoria
ORDER BY ticket_medio DESC;
```

---

### 4. Top 5 clientes por valor gasto
> Quais clientes mais contribuíram para a receita?

**Resultado:** Mariana Lima (Curitiba) lidera com R$ 8.700 em 4 compras. Pedro Alves tem o maior ticket médio por visita — candidatos a programa de fidelidade.

```sql
SELECT
  c.nome AS cliente,
  c.cidade,
  COUNT(v.id_venda) AS total_compras,
  SUM(v.quantidade * p.preco) AS total_gasto
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY c.nome, c.cidade
ORDER BY total_gasto DESC
LIMIT 5;
```

---

### 5. Produtos acima da média de receita (Subquery)
> Quais produtos performam acima da média geral?

**Resultado:** Apenas Notebook e Smartphone superam a média de R$ 5.115 — alta concentração de receita em 2 de 10 produtos, o que representa um risco estratégico para a loja.

```sql
SELECT
  p.nome AS produto,
  SUM(v.quantidade * p.preco) AS receita_total
FROM vendas v
JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY p.nome
HAVING SUM(v.quantidade * p.preco) > (
  SELECT AVG(receita_por_produto)
  FROM (
    SELECT SUM(v2.quantidade * p2.preco) AS receita_por_produto
    FROM vendas v2
    JOIN produtos p2 ON v2.id_produto = p2.id_produto
    GROUP BY p2.nome
  )
)
ORDER BY receita_total DESC;
```

---

## 💡 Principais Insights

- 📦 **Notebook e Smartphone** respondem pela maior parte da receita — diversificação é necessária
- 📅 **Junho** foi o mês de pico — vale investigar o que impulsionou as vendas nesse período
- 👤 **Top 5 clientes** concentram grande parte do faturamento — programa de fidelidade seria estratégico
- 🏷️ **Eletrônicos** têm o maior ticket médio, mas **Periféricos** têm maior frequência de compra

---

## 🛠️ Tecnologias utilizadas

- **SQL** (SQLite)
- **SQLiteOnline** — para execução das queries

---

## 📚 Conceitos aplicados

`SELECT` · `FROM` · `JOIN` · `GROUP BY` · `ORDER BY` · `HAVING` · `LIMIT`  
`SUM` · `COUNT` · `AVG` · `ROUND` · `strftime` · **Subqueries**

---

## 👩‍💻 Autora
Jamilly Oliveira

**Jamilly Oliveira**  
Analista de Dados em formação · Python · SQL · Power BI  
[LinkedIn](https://www.linkedin.com/in/jamilly-oliveira) · [GitHub](https://github.com/jamilly-devs)

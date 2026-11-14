
SELECT categoria, SUM(valor_total) AS faturamento
FROM vendas
GROUP BY categoria
ORDER BY faturamento DESC;

SELECT cliente, SUM(valor_total) AS total_gasto
FROM vendas
GROUP BY cliente
ORDER BY total_gasto DESC;

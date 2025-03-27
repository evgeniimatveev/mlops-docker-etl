SELECT category, COUNT(*) AS total_orders,
       ROUND(SUM(total)::numeric, 2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC
LIMIT 5;
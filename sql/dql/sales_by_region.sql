SELECT
    region,
    COUNT(*) AS total_orders,
    ROUND(SUM(total)::numeric, 2) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
 
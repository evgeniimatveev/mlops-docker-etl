SELECT
    DATE_TRUNC('week', date::date) AS week_start,
    COUNT(*) AS total_orders,
    ROUND(SUM(total)::numeric, 2) AS total_revenue
FROM sales
GROUP BY week_start
ORDER BY week_start;

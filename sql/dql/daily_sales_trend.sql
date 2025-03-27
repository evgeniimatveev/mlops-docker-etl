SELECT
    date AS sale_date,
    COUNT(*) AS orders,
    ROUND(SUM(total)::numeric, 2) AS total_revenue
FROM sales
GROUP BY date
ORDER BY date;

SELECT
    ROUND(AVG(discount)::numeric, 3) AS avg_discount,
    ROUND(AVG(total)::numeric, 2) AS avg_total
FROM sales;

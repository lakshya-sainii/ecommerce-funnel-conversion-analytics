CREATE DATABASE Ecommerce_Funnel_Analytics_DB;
GO

USE Ecommerce_Funnel_Analytics_DB;
GO

-- Funnel Stage Counts

SELECT
    event_type,
    COUNT(*) AS total_events
FROM ecommerce_funnel_50k
GROUP BY event_type
ORDER BY total_events DESC;


--Top Product Categories by Purchases

SELECT TOP 10
    category,
    COUNT(*) AS total_purchases
FROM ecommerce_funnel_50k
WHERE event_type = 'purchase'
GROUP BY category
ORDER BY total_purchases DESC;


--Top Brands by Revenue

SELECT TOP 10
    brand,
    ROUND(SUM(price), 2) AS total_revenue
FROM ecommerce_funnel_50k
WHERE event_type = 'purchase'
GROUP BY brand
ORDER BY total_revenue DESC;


-- Device-wise Purchase Performance

SELECT
    device,
    COUNT(*) AS total_purchases,
    ROUND(SUM(price), 2) AS total_revenue
FROM ecommerce_funnel_50k
WHERE event_type = 'purchase'
GROUP BY device
ORDER BY total_revenue DESC;



-- Traffic Source Performance


SELECT
    traffic_source,
    COUNT(*) AS total_purchases,
    ROUND(SUM(price), 2) AS total_revenue
FROM ecommerce_funnel_50k
WHERE event_type = 'purchase'
GROUP BY traffic_source
ORDER BY total_revenue DESC;
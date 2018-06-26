-- MySql script that displays top 3 cities, temperature between July and Aug
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month >= 7 AND month <= 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

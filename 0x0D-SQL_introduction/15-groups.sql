-- MySql script to list numbers of record with same value
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;

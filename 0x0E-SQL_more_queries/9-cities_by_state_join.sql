-- MySQL script that list all cities
SELECT cities.id, cities.name, states.name
FROM states, cities WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

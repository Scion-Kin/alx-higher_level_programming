-- lists all cities in a table
SELECT cities.id, cities.name, states.name FROM cities WHERE cities.state_id = states.id;

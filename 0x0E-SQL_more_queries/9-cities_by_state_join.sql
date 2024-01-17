-- lists all cities in a table
SELECT cities.id, cities.name, states.name WHERE cities.state_id = states.id;

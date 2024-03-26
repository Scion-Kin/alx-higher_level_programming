#!/usr/bin/node

const request = require('request');

const films = 'https://swapi-api.alx-tools.com/api/films/';
request.get(films, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const resJson = JSON.parse(body);
  let count = 0;
  for (const i of resJson.results) {
    if (i.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});

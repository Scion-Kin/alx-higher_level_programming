#!/usr/bin/node

const request = require('request');

const person = 'https://swapi-api.alx-tools.com/api/people/18';
request.get(person, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const resJson = JSON.parse(body);
  console.log(resJson.films.length);
});

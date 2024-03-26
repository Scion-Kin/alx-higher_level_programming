#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const resJson = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < resJson.results.length; i++) {
    if (resJson.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
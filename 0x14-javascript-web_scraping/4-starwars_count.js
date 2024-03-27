#!/usr/bin/node

const request = require('request');

if (process.argv[2]) {
  request(process.argv[2], function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      const resJson = JSON.parse(body);
      let count = 0;
      for (const i of resJson.results) {
        if (i.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    }
  });
}

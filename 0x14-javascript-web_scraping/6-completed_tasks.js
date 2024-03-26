#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resJson = JSON.parse(body);

    const users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const dict = {};
    for (const i of users) {
      let count = 0;
      for (const j of resJson) {
        if (i === j.userId && j.completed === true) {
          count++;
        }
      }
      dict[i] = count;
    }
    console.log(dict);
  }
});

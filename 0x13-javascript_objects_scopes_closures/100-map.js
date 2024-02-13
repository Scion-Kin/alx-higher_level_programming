#!/usr/bin/node
const { list } = require('./100-data');

const newLi = list.map((x) => x * 2);

console.log(list);
console.log(newLi);

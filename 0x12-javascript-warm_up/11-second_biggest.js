#!/usr/bin/node

if (isNaN(process.argv[2]) || !process.argv[2] || process.argv.length < 4) {
  console.log('0');
} else {
  let i = 2;
  const arr = [];

  while (process.argv[i]) {
    arr.push(Number(process.argv[i]));
    i++;
  }
  console.log(Math.max(...arr));
}

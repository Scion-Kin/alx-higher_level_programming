#!/usr/bin/node

function factorial (num) {
  if (num === 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}

if (isNaN(process.argv[2]) || !process.argv[2]) {
  console.log('1');
} else {
  const num = factorial(parseInt(process.argv[2]));
  console.log(num);
}

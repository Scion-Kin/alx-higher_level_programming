#!/usr/bin/node

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(process.argv[2], process.argv[3]);

/* Write a script that prints the addition of 2 integers

    The first argument is the first integer
    The second argument is the second integer
    You have to define a function with this prototype:
    You must use console.log(...) to print all output
    You are not allowed to use var */

#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      // Base case: when the number is less than the base, return it as a string
      return num.toString(base);
    } else {
      // Recursive case: divide the number by the base and continue converting
      return convertToBase(Math.floor(num / base)) + convertToBase(num % base);
    }
  };
};

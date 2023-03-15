#!/usr/bin/node
const arg = parseInt(process.argv[2]);
function factorial (a) {
  if (a === undefined || isNaN(a) || a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
const num = factorial(arg);
console.log(num);

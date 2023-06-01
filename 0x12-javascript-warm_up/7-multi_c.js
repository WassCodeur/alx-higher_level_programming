#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < arg; x++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined || isNaN(arg)) {
  console.log('Missing size');
} else {
  let x = 0;
  let line = '';
  while (x < arg) {
    for (let j = 0; j < arg; j++) {
	    line += 'x';
    }
    console.log(line);
    line = '';
    x++;
  }
}

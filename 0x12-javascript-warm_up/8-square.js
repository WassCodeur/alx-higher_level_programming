#!/usr/bin/node   

import { argv } from 'node:process';
if ( argv[2] === undefined ) {
  console.log('Missing number of occurrences');
} else {
    let x = 0;
    while ( x < argv[2]) {
      console.log('C is fun');
      x++;
    }
}

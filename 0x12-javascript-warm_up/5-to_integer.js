#!/usr/bin/node

import { argv } from 'node:process';
if ( argv[2] >= 0 && argv <= 9) {
  console.log(`My number: ${argv[2]}`);
} else {
  console.log('Not a number');
}

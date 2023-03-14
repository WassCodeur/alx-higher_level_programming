#!/usr/bin/node
const arg1 =parseInt( process.argv[2]);
const arg2 =parseInt(process.argv[3]);
function add (a, b) {
  let sum;
  if (( a === undefined || b === undefined) || ( isNaN(a) || isNaN(b))) {
    console.log('NaN');
   } else {
       sum = a + b;
       console.log(sum);
   }
}

add(arg1, arg2);

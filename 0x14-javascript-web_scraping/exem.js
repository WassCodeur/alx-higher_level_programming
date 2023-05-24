#!/usr/bin/node
const fs = require('fs');
if (process.argv.length < 3) {
  console.log('USAGE: ./exem.js filename');
} else {
  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) throw err;
    const content = data;
    console.log(content);
  });
}

#!/usr/bin/node
const fs = require('fs');
if (process.argv.length < 3) {
  console.error('USAGE : ./0-readme.js filemane');
} else {
  fs.readFile(`${process.argv[2]}`, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      const content = data;
      console.log(content);
    }
  });
}

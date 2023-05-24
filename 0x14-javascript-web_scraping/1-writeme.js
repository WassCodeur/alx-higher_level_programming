#!/usr/bin/node
const fs = require('fs');
if (process.argv.length < 4) {
  console.error('USAGE : ./1-writeme.js filename txt');
} else {
  fs.writeFile(`${process.argv[2]}`, `${process.argv[3]}`, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

#!/usr/bin/node
const request = require('request');
const fs = require('fs');
if (process.argv.length < 4) {
  console.error('USAGE : ./5-request_store.js url filename');
} else {
  const url = process.argv[2];
  const filePath = process.argv[3];
  request.get(`${url}`, (err, res, body) => {
    if (err) {
      console.error(err);
    } else if (res.statusCode === 200) {
      fs.writeFile(`${filePath}`, body, { encoding: 'utf8' }, (err) => {
        if (err) {
          console.error(err);
        }
      });
    } else {
      console.error('Ooooup something went wrong');
    }
  });
}

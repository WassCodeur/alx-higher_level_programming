#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
  console.error('USAGE : ./2-statuscode.js url');
} else {
  const url = process.argv[2];
  request(`${url}`, (err, res) => {
    if (err) {
      console.error(url);
    }
    console.log('code: ', res.statusCode);
  });
}

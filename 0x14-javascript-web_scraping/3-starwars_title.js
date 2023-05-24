#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
  console.error('USAGE : ./3-starwars_title.js id');
} else {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  request(`${url}`, (err, res, body) => {
    if (err) {
      console.error(err);
    } else if (res.statusCode === 200) {
      const content = JSON.parse(body);
      console.log(content.title);
    } else {
      console.error('Ooop!! something went wrong ');
    }
  });
}

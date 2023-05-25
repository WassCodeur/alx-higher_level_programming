#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
  console.error('USAGE : ./4-starwars_count.js url');
} else {
  const filmUrl = process.argv[2];
  const peopleUrl = 'https://swapi-api.alx-tools.com/api/people/';
  const characterId = 18;
  request.get(`${filmUrl}`, (err, res, body) => {
    if (err) {
      console.error(err);
    } else if (res.statusCode === 200) {
      const content = JSON.parse(body);
      const filmsWithTheCharacter = content.results.filter((film) => {
        return film.characters.includes(`${peopleUrl}${characterId}/`);
      });
      console.log(filmsWithTheCharacter.length);
    } else {
      console.log('Ooups something went wrong');
    }
  });
}

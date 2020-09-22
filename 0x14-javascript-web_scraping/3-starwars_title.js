#!/usr/bin/node

const arg = process.argv[2];
const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/' + arg, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});

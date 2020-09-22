#!/usr/bin/node

const arg = process.argv[2];
const id = 18;
const request = require('request');

request.get(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resu = JSON.parse(body).results;
    let count = 0;
    for (const i of resu) {
      for (const j of i.characters) {
        if (j.includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

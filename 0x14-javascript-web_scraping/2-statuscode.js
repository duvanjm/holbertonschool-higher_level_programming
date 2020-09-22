#!/usr/bin/node

const arg = process.argv[2];
const request = require('request');

request(arg, function (err, response, body) {
  if (err) {
    console.log('code: ' + err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

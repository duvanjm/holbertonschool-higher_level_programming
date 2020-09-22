#!/usr/bin/node

const arg = process.argv;
const fs = require('fs');
const request = require('request');

request.get(arg[2], function (error, responce, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(arg[3], body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});

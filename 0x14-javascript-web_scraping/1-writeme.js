#!/usr/bin/node

const arg = process.argv;
const fs = require('fs');

fs.writeFile(arg[2], arg[3], 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node

const arg = process.argv[2];
const request = require('request');
const all = {};

request.get(arg, function (error, responce, body) {
  if (error) {
    console.log(error);
  } else {
    const resul = JSON.parse(body);
    for (const i of resul) {
      if (i.completed === true) {
        if (i.userId in all) {
          all[i.userId]++;
        } else {
          all[i.userId] = 1;
        }
      }
    }
    console.log(all);
  }
});

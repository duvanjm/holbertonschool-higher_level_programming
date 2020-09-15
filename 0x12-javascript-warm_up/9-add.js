#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  let add = 0;

  if (a === undefined || b === undefined) {
    add = NaN;
  } else {
    add = a + b;
  }
  console.log(add);
}

add(parseInt(arg[2]), parseInt(arg[3]));

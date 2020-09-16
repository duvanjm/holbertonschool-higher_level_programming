#!/usr/bin/node

const arg = process.argv;
arg.splice(0, 2);
const size = arg.length;
let value = 0;

if (size === 0 || size === 1) {
  console.log('0');
} else {
  arg.sort((a, b) => a - b);
  value = arg[size - 2];
  console.log(value);
}

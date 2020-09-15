#!/usr/bin/node
const arg = process.argv;

function factorial (n) {
  let re = 1;
  for (let i = 1; i <= n; i++) {
    re = re * i;
  }
  console.log(re);
}
factorial(parseInt(arg[2]));

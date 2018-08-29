#!/usr/bin/node
// JS to compute the factorial of a number
'use strict';
let a = Number(process.argv[2]);
function factorialize (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return (a * factorialize(a - 1));
  }
}
console.log(factorialize(a));

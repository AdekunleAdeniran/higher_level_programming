#!/usr/bin/node
// JS to print C is fun by number of passed in argument
'use strict';
let arg = process.argv[2];
let count = 0;
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}
while (count < arg) {
  console.log('C is fun');
  count++;
}

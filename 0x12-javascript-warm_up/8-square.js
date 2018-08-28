#!/usr/bin/node
// JS to print X square by number of passed argument
'use strict';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let count = 0; count < process.argv[2]; count++) {
    console.log('X'.repeat(process.argv[2]));
  }
}

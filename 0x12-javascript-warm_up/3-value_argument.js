#!/usr/bin/node
// JS to check arguments passed into script and prints first argument
'use strict';
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

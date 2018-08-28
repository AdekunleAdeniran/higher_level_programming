#!/usr/bin/node
// JS to check arguments passed into script
'use strict';
let len = process.argv.length;
if (len < 3) {
  console.log('No argument');
} else if (len > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}

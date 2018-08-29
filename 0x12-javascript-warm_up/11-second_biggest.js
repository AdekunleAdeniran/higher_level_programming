#!/usr/bin/node
// JS to find the second largest number
'use strict';
(function secondBiggest (arg) {
  let list = [];
  if (process.argv.length < 4) {
    console.log(0);
  } else {
    for (let count = 2; count < process.argv.length; count++) {
      list.push(Number(process.argv[count]));
    }
    console.log(list.sort()[list.length - 2]);
  }
})();

#!/usr/bin/node
// JS to print the addition of two integers given as arguments
'use strict';
exports.callMeMoby = function (x, theFunction) {
  for (let count = 0; count < x; count++) {
    theFunction();
  }
};

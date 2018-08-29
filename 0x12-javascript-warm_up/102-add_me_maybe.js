#!/usr/bin/node
// JS to print the addition of two integers given as arguments
'use strict';
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

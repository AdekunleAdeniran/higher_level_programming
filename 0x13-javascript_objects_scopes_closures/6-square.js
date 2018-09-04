#!/usr/bin/node
// JS script to define class that inherits from another class
const newSquare = require('./5-square');

class Square extends newSquare {
  charPrint (c) {
    for (let count = 0; count < this.height; count++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;

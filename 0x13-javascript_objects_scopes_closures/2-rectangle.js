#!/usr/bin/node
// JS script to define an empty class
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w == undefined || h == undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;

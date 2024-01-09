#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    if (char === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        let txt = '';
        for (let y = 0; y < this.width; y++) {
          txt += char;
        }
        console.log(txt);
      }
    }
  }
}
module.exports = Square;

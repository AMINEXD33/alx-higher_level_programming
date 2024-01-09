#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let txt = '';
      for (let y = 0; y < this.width; y++) {
        txt += 'X';
      }
      console.log(txt);
    }
  }
}

const ob = new Rectangle(2, 3);
ob.print();
module.exports = Rectangle;

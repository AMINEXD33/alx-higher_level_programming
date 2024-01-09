#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (a, b) {
    for (let x = 0; x < b; x++) {
      let txt = '';
      for (let y = 0; y < a; y++) {
        txt += 'X';
      }
      console.log(txt);
    }
  }
}
module.exports = Rectangle;

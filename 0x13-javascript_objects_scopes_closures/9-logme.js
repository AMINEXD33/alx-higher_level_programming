#!/usr/bin/node

let oldVal = 0;
exports.logMe = function (item) {
  console.log(oldVal + ': ' + item);
  oldVal++;
};

#!/usr/bin/node

exports.esrever = function (list) {
  let pointera = 0;
  let pointerb = list.length - 1;

  while (pointera !== pointerb && pointera < pointerb) {
    const tmp = list[pointera];
    list[pointera] = list[pointerb];
    list[pointerb] = tmp;

    pointera++;
    pointerb--;
  }
  return (list);
};

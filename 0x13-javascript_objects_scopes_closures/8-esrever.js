#!/usr/bin/node

exports.esrever = function (list) {
  // they cou've made it harder by
  // asking to sort in place
  const EmptyList = [];
  for (let x = list.length; x > 0; x--) {
    EmptyList.push(list[x]);
  }
  return (EmptyList);
};

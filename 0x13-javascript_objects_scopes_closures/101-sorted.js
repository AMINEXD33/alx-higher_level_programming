#!/usr/bin/node

// const dict = require('./100-data.js').dict;
let dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};
dict = Object.entries(dict);
const newMap = new Map();

for (const vals of dict.values()) {
  const val = vals[0];
  const key = vals[1].toString();
  if (newMap.has(key)) {
    console.log(key, 'with', val, 'already in ');
    const tmparr = newMap.get(key);
    tmparr.push(val);
    newMap.set(key, tmparr);
  } else {
    newMap.set(key, [val]);
  }
}
console.log(newMap);

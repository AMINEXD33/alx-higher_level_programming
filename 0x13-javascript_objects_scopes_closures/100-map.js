#!/usr/bin/node

const list = require('./100-data.js').list;

let mapVar = new Map();
let result = [];
for (let x = 0; x < list.length; x++)
{
    mapVar.set(x,(list[x] * x));
}
for (let x = 0; x < list.length; x++)
{
    result.push(mapVar.get(x));
}

#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const URL = argv[2];
const dict = {};

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(response.body);
    for (const x in data) {
      if (data[x].completed) {
        if (dict[data[x].userId] !== undefined) {
          dict[data[x].userId] = dict[data[x].userId] + 1;
        } else {
          dict[data[x].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});

#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const URL = argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(response.body).results;
    let count = 0;
    for (const row in data) {
      if (/18/.test(data[row].characters)) {
        count++;
      }
    }
    console.log(count);
  }
});

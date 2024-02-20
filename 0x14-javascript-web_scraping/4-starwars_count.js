#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const URL = argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const data = response.body;
    const rgx = /https:\/\/swapi-api.alx-tools.com\/api\/people\/18\//g;
    const count = data.match(rgx);
    console.log(count.length);
  }
});

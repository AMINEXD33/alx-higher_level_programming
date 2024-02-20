#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const id = argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const data = (JSON.parse(response.body));
    console.log(data.title);
  }
});

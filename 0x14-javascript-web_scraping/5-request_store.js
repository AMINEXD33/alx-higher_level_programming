#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const fs = require('fs');
const URL = argv[2];
const fileName = argv[3];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const fileContent = response.body;
    fs.writeFile(fileName, fileContent, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

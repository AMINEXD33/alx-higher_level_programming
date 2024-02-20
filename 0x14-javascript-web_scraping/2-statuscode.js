#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

function getCode (URL) {
  request(URL, function (error, response) {
    if (error) {
      console.log(error);
    } else {
      console.log('code: ', response && response.statusCode);
    }
  });
}

getCode(argv[2]);

#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

function getCode (URL) {
  request(URL, function (error, response, body) {
    if (!error) {
      console.log('code: ', response && response.statusCode);
    } else {
      console.log(error);
    }
  });
}

getCode(argv[2]);

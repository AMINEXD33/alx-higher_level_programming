#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

function getCode (URL) {
  request(URL, 'GET', function (error, response, body) {
    if (!error) {
      console.log('code: ', response && response.statusCode);
    }
  });
}

if (argv.length >= 3) {
  getCode(argv[2]);
}

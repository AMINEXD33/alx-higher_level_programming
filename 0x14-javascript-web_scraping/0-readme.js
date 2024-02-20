#!/usr/bin/node

// let request = require("./request-master/request");
const fs = require('fs');
const { argv } = require('node:process');

function showContent (err, content) {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
}

function read (fileName) {
  fs.readFile(fileName, 'utf-8', showContent);
}

if (argv.length >= 3) {
  read(argv[2]);
}

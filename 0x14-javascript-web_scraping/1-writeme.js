#!/usr/bin/node

// let request = require("./request-master/request");
const fs = require('fs');
const { argv } = require('node:process');

function writeFfile (fileName, fileContent) {
  fs.writeFile(fileName, fileContent, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}

writeFfile(argv[2], argv[3]);

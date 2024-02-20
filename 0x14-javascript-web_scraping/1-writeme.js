#!/usr/bin/node

// let request = require("./request-master/request");
const fs = require('fs');
const { argv } = require('node:process');

const fileName = argv[2];
const fileContent = argv[3];

fs.writeFile(fileName, fileContent, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

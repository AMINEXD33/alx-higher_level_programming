const { argv } = require('node:process');

const PotentialNnum = parseInt(argv[2]);
if (isNaN(PotentialNnum)) {
  console.log('Not a number');
} else {
  console.log('My number: ', PotentialNnum);
}

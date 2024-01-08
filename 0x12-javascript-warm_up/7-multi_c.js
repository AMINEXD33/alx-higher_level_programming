const { argv } = require('node:process');

function ToNum () {
  const PotentialNnum = parseInt(argv[2]);
  if (isNaN(PotentialNnum)) {
    console.log('Missing number of occurrences');
    return (false);
  } else {
    return (PotentialNnum);
  }
}
const Num = ToNum();
if (Num !== false) {
  for (let x = 0; x < Num; x++) {
    console.log('C is fun');
  }
}

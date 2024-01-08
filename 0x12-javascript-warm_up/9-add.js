const { argv } = require('node:process');

function ToNum1 () {
  const PotentialNnum = parseInt(argv[2]);
  if (isNaN(PotentialNnum)) {
    return (NaN);
  } else {
    return (PotentialNnum);
  }
}
function ToNum2 () {
  const PotentialNnum = parseInt(argv[3]);
  if (isNaN(PotentialNnum)) {
    return (NaN);
  } else {
    return (PotentialNnum);
  }
}

function add (a, b) {
  return (a + b);
}

let a = ToNum1();
const b = ToNum2();

a = add(a, b);
console.log(a);

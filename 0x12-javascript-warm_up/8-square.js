const { argv } = require('node:process');

function ToNum () {
  const PotentialNnum = parseInt(argv[2]);
  if (isNaN(PotentialNnum)) {
    console.log('Missing size');
    return (false);
  } else {
    return (PotentialNnum);
  }
}

const Num = ToNum();
if (Num !== false) {
  for (let x = 0; x < Num; x++) {
    let Str = '';
    for (let tmp = 0; tmp < Num; tmp++) {
      Str += 'X';
    }
    console.log(Str + '\r');
  }
}

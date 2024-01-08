const { argv } = require('node:process');

try {
  if (argv[2] !== undefined) {
    console.log(argv[2]);
  } else {
    console.log('No argument');
  }
} catch {

}

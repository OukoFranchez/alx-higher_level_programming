#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Not a number');
} else if (!isNaN(parseInt(process.argv[2], 10))) {
  console.log(`My number: ${parseInt(process.argv[2], 10)}`);
} else {
  console.log('Not a number');
}

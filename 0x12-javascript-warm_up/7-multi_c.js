#!/usr/bin/node

let string = "C is fun";
let convertedNumber = parseInt(process.argv[2], 10);

if (process.argv.length < 3 || isNaN(convertedNumber)) {
  console.log('Missing number of occurrences');
}else {
  for (let i = 0; i < convertedNumber; i++) {
    console.log(string);
  }
}

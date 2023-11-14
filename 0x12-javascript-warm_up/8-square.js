#!/usr/bin/node

const numberToSquare = parseInt(process.argv[2], 10);

if (process.argv.length < 3 || isNaN(numberToSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numberToSquare; i++) {
    let charToPrint = '';
    for (let j = 0; j < numberToSquare; j++) {
      charToPrint += 'X';
    }
    console.log(charToPrint);
  }
}

#!/usr/bin/node

function factorial (n) {
  // Base case
  if (n === 0 || n === 1) {
    return 1;
  } else {
    // recursive case
    return n * factorial(n - 1);
  }
}
if (process.argv.length < 3) {
  console.log(1);
} else {
  const numberToFact = parseInt(process.argv[2], 10);
  console.log(factorial(numberToFact));
}

#!/usr/bin/node

let argCount = 0;

// Loop until process.argv[argCount] is undefined
while (process.argv[argCount] !== undefined) {
  argCount++;
}

// console.log('Number of arguments:', argCount);

if (argCount <= 2) {
  console.log('No argument');
} else {
  // Print each argument
  for (let index = 2; index < argCount; index++) {
    console.log(`${process.argv[index]}`);
  }
}

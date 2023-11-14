#!/usr/bin/node

// Check if there are no arguments or only one argument
if (process.argv.length <= 2 || process.argv[2] === 1) {
  console.log(0);
} else {
  // Initialize the two largest variables
  let largest = Number(process.argv[2]);
  let secondLargest = Number(process.argv[3]);

  // Iterate through the command-line arguments starting from index 3
  for (let i = 3; i < process.argv.length; i++) {
    const currentNumber = Number(process.argv[i]);

    // Update largest and second largest values
    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber !== largest) {
      secondLargest = currentNumber;
    }
  }

  // Output the second largest integer
  console.log(secondLargest);
}

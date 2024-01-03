#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const filePath = args[2];
const dataToWrite = args[3];

fs.writeFile(filePath, dataToWrite, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	}
});

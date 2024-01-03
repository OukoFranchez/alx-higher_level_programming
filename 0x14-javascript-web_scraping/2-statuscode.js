#!/usr/bin/node

const args = process.argv;
const { error } = require('console');
const request = require('request');
url = args[2];

request(url, (error, response, body) => {
	if(!error) {
		console.log('code' + response.statusCode);
	}
});
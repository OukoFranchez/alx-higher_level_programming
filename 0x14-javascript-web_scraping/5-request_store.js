#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (!error) {
    fs.writeFile(args[3], body, 'utf-8', (err) => {
      if (err) {
        return -1;
      }
    });
  }
});

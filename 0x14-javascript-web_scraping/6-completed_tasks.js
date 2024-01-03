#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (!error) {
    const information = JSON.parse(body);
    const completedCount = [];

    information.forEach(function (entry) {
      if (completedCount[entry.userId] === undefined) {
        completedCount[entry.userId] = 0;
      }
      if (entry.completed === true) {
        completedCount[entry.userId]++;
      }
    });
    const result = {};
    for (let i = 1; i < completedCount.length; i++) {
      if (completedCount[i] > 0) {
        result[i] = completedCount[i];
      }
    }
    console.log(result);
  }
});

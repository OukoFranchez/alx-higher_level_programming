#!/usr/bin/node
const dict = require('./101-data.js');

const newDictionary = {};
const entries = dict.dict;

for (const key in entries) {
  if (newDictionary[entries[key]] === undefined) {
    newDictionary[entries[key]] = [key];
  } else {
    newDictionary[entries[key]].push(key);
  }
}

console.log(newDictionary);

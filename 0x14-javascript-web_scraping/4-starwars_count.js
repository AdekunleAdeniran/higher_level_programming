#!/usr/bin/node
let request = require('request');
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).results;
    let count = 0;
    for (let index = 0; index < results.length; index++) {
      for (let char = 0; char < results[index].characters.length; char++) {
        if (results[index].characters[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

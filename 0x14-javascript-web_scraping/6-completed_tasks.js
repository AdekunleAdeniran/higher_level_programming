#!/usr/bin/node
let request = require('request');
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let result = JSON.parse(body);
    let dic = {};
    for (let index = 0; index < result.length; index++) {
      if (result[index].completed === true) {
        if (dic[result[index].userId] === undefined) {
          dic[result[index].userId] = 1;
        } else {
          dic[result[index].userId] += 1;
        }
      }
    }
    console.log(dic);
  }
});

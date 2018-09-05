#!/usr/bin/node
let request = require('request');
let url = 'http://swapi.co/api/films/';
let id = process.argv[2];

request(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});

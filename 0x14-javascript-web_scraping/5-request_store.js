#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
let fs = require('fs');
request(url, 'utf-8').pipe(fs.createWriteStream(process.argv[3]));

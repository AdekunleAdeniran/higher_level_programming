#!/usr/bin/node
// JS to print an array of string
'use strict';
let languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let language in languages) {
  console.log(languages[language]);
}

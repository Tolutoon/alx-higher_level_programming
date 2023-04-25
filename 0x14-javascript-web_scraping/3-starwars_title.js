#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
<<<<<<< HEAD
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
=======
const API_URL = 'https://swap-api.alx-tools.com/api/films/';
>>>>>>> 4cdd1c39b3a00285ef14bba600144a98a6d8829a

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const reponseJSON = JSON.parse(body);
    console.log(reponseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

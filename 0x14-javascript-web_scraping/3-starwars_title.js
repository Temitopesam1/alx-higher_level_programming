#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('http://swapi.co/api/films/' + id, (error, body) => {
	if (error) {
	  console.error(error);
	  return;
	}
	const json = JSON.parse(body.body);
	console.log(json.title);
});

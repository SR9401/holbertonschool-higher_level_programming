#!/usr/bin/node

const lines = [
    "C is fun",
    "Python is cool",
    "JavaScript is amazing"
];
let output = lines[0];
for (let i = 1; i < lines.length; i++) {
    output += '\n' + lines[i];
}
console.log(output);

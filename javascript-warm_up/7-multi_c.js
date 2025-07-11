#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);
let output = '';

if (isNaN(x) || x < 0) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < x; i++) {
        output += 'C is fun\n';
    }
    console.log(output.trim());
}

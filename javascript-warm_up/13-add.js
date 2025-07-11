#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const args = process.argv.slice(2);
if (args.length < 2) {
    console.log("Veuillez fournir deux entiers.");
} else {
    const a = parseInt(args[0]);
    const b = parseInt(args[1]);
    if (isNaN(a) || isNaN(b)) {
        console.log("Les arguments doivent être des entiers.");
    } else {
        console.log(add(a, b));
    }
}

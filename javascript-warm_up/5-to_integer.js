#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length === 0) {
    console.log('Not a number');
} else {
    const arg = args[0];
    const numRegex = /^\s*[+-]?(\d+\.?\d*|\.\d+)\s*$/;
    if (numRegex.test(arg)) {
        const num = parseFloat(arg);
        const intNum = Math.trunc(num);
        console.log(`My number: ${intNum}`);
    } else {
        console.log('Not a number');
    }
}
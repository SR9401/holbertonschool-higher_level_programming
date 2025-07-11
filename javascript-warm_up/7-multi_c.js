#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length === 0 || isNaN(parseInt(args[0])) || parseInt(args[0]) < 0) {
    console.log("Missing number of occurrences");
} else {
    const x = parseInt(args[0]);
    if (x === 0) {
        // Ne rien faire
    } else {
        let output = '';
        for (let i = 0; i < x; i++) {
            output += 'C is fun\n';
        }
        console.log(output.trim());
    }
}

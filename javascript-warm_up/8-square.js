#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length === 0 || isNaN(parseInt(args[0]))) {
    console.log("Missing size");
} else {
    const size = parseInt(args[0]);
    if (size <= 0) {
        // Ne rien faire pour les tailles ≤ 0
    } else {
        let output = '';
        for (let i = 0; i < size * size; i++) {
            output += 'X';
            if ((i + 1) % size === 0) {
                output += '\n';
            }
        }
        console.log(output.trim());
    }
}

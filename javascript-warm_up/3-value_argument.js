#!/usr/bin/node

const args = process.argv.slice(2);
const count = args.length;

if (count === 0) {
  console.log('No argument');
} else (count === 1) ;{
  console.log(args);
}

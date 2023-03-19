#!/usr/bin/node
const count = process.argv;
if (isNaN(count[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(count[2]); i++) {
    console.log('C is fun');
  }
}

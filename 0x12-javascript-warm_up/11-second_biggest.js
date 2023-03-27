#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const secondBiggestNumber = args.sort().reverse()[1];
  console.log(secondBiggestNumber);
}

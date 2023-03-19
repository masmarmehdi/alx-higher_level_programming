#!/usr/bin/node
const num = process.argv;
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
if (!isNaN(num[2])) {
  console.log(factorial(num[2]));
} else {
  console.log(1);
}

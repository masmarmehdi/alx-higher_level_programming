#!/usr/bin/node
const size = process.argv;
if (isNaN(size[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size[2]; i++) {
	  let row = '';
	  for (let j = 0; j < size[2]; j++) {
		  row += 'X';
	  }
	  console.log(row);
  }
}

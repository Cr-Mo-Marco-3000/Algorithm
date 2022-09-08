const [N, ...myList] = require('fs')
  // .readFileSync('/dev/stdin')
  .readFileSync('input.txt')
  .toString()
  .trim()
  .split('\n')

myList.sort((a, b) => a - b)

const myString = myList.join('\n')
console.log(myString)

let [N, list] = require('fs')
  // .readFileSync('/dev/stdin')
  .readFileSync('input.txt')
  .toString()
  .trim()
  .split('\n')
list = list.split(' ').map((x) => parseInt(x))
list.sort((a, b) => {
  console.log(a, b)
  return a - b
})
console.log(list.at(0), list.at(-1))

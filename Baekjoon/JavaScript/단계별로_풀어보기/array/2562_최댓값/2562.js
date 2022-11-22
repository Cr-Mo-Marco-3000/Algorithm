const list = require('fs')
  // .readFileSync('/dev/stdin')
  .readFileSync('input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((x) => parseInt(x))

let maxValue = -1
let maxIndex = -1

const L = list.length

for (let i = 0; i < L; i++) {
  if (list[i] > maxValue) {
    maxValue = list[i]
    maxIndex = i
  }
}
console.log(maxValue)
console.log(maxIndex + 1)

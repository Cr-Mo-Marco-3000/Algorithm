const N = require("fs").readFileSync("input.txt").toString().trim()

let cnt = 1

let min = 1
let max = 1

while (true) {
  if (cnt === 1) {
    min = 1
    max = 1
  } else if (cnt === 2) {
    min = 2
    max = 7
  } else {
    min = min + 6 * (cnt - 2)
    max = min + 6 * (cnt - 1) - 1
  }
  if (N >= min && N <= max) {
    break
  }
  cnt++
}

console.log(cnt)

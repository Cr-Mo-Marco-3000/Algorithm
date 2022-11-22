const [N, ...input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => parseInt(x))

console.log(input)

const count = new Array(10001).fill(0)
for (const i of input) {
  count[i] += 1
}
let j = 10001
while (j >= 0) {
  j--
}

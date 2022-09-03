const [a, b] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

const [N, X] = a.split(" ").map((x) => parseInt(x))
const list = b.split(" ").map((x) => parseInt(x))
const ans = []

for (let i = 0; i < N; i++) {
  if (list[i] < X) {
    ans.push(list[i])
  }
}
console.log(...ans)

const [A, B, V] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((x) => parseInt(x))

let ans = Math.ceil((V - A) / (A - B)) + 1
console.log(ans)

const [N, ...input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => parseInt(x))

const stack = []

for (const i of input) {
  if (i === 0) {
    stack.pop()
  } else {
    stack.push(i)
  }
}
console.log(stack.reduce((acc, cur) => acc + cur, 0))

const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

const ans = []

for (const i of input) {
  if (i === ".") {
    break
  }
  stack = []
  for (const j of i) {
    if (j === '(' )
  }
  if (stack.length) {
    ans.push("no")
  } else {
    ans.push("yes")
  }
}

console.log(ans.join("\n"))

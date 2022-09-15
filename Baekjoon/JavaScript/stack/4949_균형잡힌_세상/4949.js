const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

for (const i of input) {
  let stack = []
  for (let j = 0; j < i.length; j++) {
    if (i[j] === "(") {
    } else if (i[j] === ")") {
    } else if (i[j] === "[") {
    } else if (i[j] === "]") {
    }
  }
  if (!stack.length) {
    print(yes)
  } else {
    print(no)
  }
}

const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

const L = input.length

for (let i = 0; i < L; i++) {
  const [a, b] = input[i].split(" ").map((x) => parseInt(x))
  if (a === 0 && b === 0) {
    break
  } else {
    console.log(a + b)
  }
}

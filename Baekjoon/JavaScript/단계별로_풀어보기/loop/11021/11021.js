const [T, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  // .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

for (let i = 0; i < T; i++) {
  const [a, b] = input[i].split(" ").map((x) => parseInt(x))
  console.log(`Case #${i + 1}: ${a + b}`)
}

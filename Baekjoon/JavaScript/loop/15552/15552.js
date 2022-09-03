const [N, ...input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

let string = ""

for (let i = 0; i < N; i++) {
  const [a, b] = input[i].split(" ").map((x) => parseInt(x))
  string += (a + b).toString() + "\n"
}
console.log(string)

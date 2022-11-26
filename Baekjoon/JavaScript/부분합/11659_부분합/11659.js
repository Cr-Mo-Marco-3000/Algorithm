let [command, numbers, ...input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

const [N, M] = command.split(" ").map((x) => parseInt(x))

const ans = []

numbers = numbers.split(" ").map((x) => parseInt(x))

for (let i = 0; i < M; i++) {
  const [start, end] = input[i].split(" ")
  let cum = 0
  for (const j of numbers) {
    cum += j
  }
  console.log(cum)
}

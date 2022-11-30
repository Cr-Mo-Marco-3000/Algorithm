let [order, ...input] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

const [N, K] = order.split(" ").map((x) => parseInt(x))
input = input.map((x) => parseInt(x))

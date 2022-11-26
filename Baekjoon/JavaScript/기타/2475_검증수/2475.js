input = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .reduce((x, y) => x + parseInt(y) ** 2, 0)

console.log(input % 10)

const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
if (!input[0]) {
  console.log(0)
} else {
  console.log(input.length)
}

let [a, b] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")

a = parseInt(a.split("").reverse().join(""))
b = parseInt(b.split("").reverse().join(""))

const myArray = [a, b].sort((a, b) => a - b)

console.log(myArray.at(-1))

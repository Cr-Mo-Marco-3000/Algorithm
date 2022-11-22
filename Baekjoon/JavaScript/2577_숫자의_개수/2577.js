const input = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .reduce((x, y) => x * parseInt(y))
myArray = new Array(10).fill(0)
const checkArray = input.toString()

for (let i = 0; i < checkArray.length; i++) {
  myArray[checkArray[i]]++
}

const ans = myArray.join("\n")

console.log(ans)

const [x, y, w, h] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((x) => parseInt(x))

myArray = []
myArray.push(x, y, w - x, h - y)
myArray.sort((x, y) => x - y)
console.log(myArray[0])

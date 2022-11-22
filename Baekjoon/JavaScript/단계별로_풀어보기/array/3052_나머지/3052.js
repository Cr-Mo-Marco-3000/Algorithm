const myList = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) => parseInt(x))

const mySet = new Set()

for (let i = 0; i < myList.length; i++) {
  mySet.add(myList[i] % 42)
}

console.log(mySet.size)

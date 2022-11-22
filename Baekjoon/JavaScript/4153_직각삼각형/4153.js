const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

const ans = []

for (let i = 0; i < input.length - 1; i++) {
  const myArray = input[i].split(" ").map((x) => parseInt(x))
  myArray.sort((x, y) => x - y)
  const [x, y, z] = myArray
  console.log(x ** 2 + y ** 2 === z ** 2 ? "right" : "wrong")
}

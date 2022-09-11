let [N, myList] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

myList = myList.split(" ").map((x) => {
  return parseInt(x)
})

const maxValue = Math.max(...myList)

let sum = 0

for (let i = 0; i < N; i++) {
  sum += (myList[i] / maxValue) * 100
}

console.log(sum / N)

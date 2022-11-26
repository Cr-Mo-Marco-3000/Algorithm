let [N, K] = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((x) => parseInt(x))

const list = new Array(N).fill().map((x, idx) => idx + 1)
const ans = []
let cnt = 1

while (list.length) {
  if (cnt % K) {
    list.push(list.shift())
  } else {
    ans.push(list.shift())
  }
  cnt++
}

console.log("<" + ans.join(", ") + ">")

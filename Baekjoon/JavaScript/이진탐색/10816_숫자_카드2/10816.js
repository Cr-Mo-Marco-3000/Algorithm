let [N, numList, M, searchList] = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

numList = numList
  .split(" ")
  .map((x) => parseInt(x))
  .sort((x, y) => x - y)

g = []

searchList = searchList.split(" ").map((x) => parseInt(x))

let left = 0
let crit = numList[0]

for (let i = 0; i < numList.length; i++) {
  if (numList[i] !== crit) {
    g.push([crit, i - left])
    left = i
    crit = numList[i]
  }
}
g.push([numList.at(-1), numList.length - left])

// 이진 탐색 시작

const ans = []

for (let j = 0; j < searchList.length; j++) {
  const v = searchList[j]
  let left = 0
  let right = g.length
  flag = false

  while (left < g.length && right >= 0 && left <= right) {
    const mid = parseInt((left + right) / 2)
    if (g[mid][0] === v) {
      ans.push(g[mid][1])
      flag = true
      break
    } else if (g[mid][0] > v) {
      right = mid - 1
    } else if (g[mid][0] < v) {
      left = mid + 1
    }
  }
  if (flag === false) {
    ans.push(0)
  }
}

console.log(ans.join(" "))

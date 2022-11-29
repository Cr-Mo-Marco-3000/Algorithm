const [N, K] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((x) => parseInt(x))

const g = new Array(100001).fill(100001)

const stack = [[N, 0]]

while (stack.length) {
  const [v, time] = stack.pop()

  if (time < g[v]) {
    g[v] = time
    if (v + 1 < 100001) {
      stack.push([v + 1, time + 1])
    }
    if (v - 1 >= 0) {
      stack.push([v - 1, time + 1])
    }
    if (v * 2 < 100001) {
      stack.push([v * 2, time + 1])
    }
  }
}

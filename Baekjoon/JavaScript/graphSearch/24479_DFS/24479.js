const [conf, ...input] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

const [N, M, R] = conf.split(" ").map((x) => parseInt(x))

const g = new Array(N + 1).fill(null).map((x) => new Array(0))

visited = new Array(N + 1).fill(0)

for (let i = 0; i < M; i++) {
  const [start, end] = input[i].split(" ").map((x) => parseInt(x))
  g[start].push(end)
  g[end].push(start)
}
g.map((x) => x.sort((a, b) => b - a))

const stack = [R]
let cnt = 1
while (stack.length) {
  let v = stack.pop()
  if (!visited[v]) {
    visited[v] = cnt
    cnt++
    for (let w = 0; w < g[v].length; w++) {
      stack.push(g[v][w])
    }
  }
}

visited.shift()

const ans = visited.join("\n")
console.log(ans)

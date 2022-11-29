let [commands, ...input] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

const [N, M, K, X] = commands.split(" ").map((x) => parseInt(x))

const g = new Array(N + 1).fill().map(() => new Array())

const visited = new Array(N + 1).fill(3000003)

for (let i = 0; i < M; i++) {
  const [start, end] = input[i].split(" ").map((x) => parseInt(x))
  g[start].push(end)
}

const Q = [[X, 0]]

while (Q.length) {
  const [v, dist] = Q.shift()
  if (visited[v] === 3000003 || visited[v] > dist) {
    visited[v] = dist
  }
  for (let w = 0; w < g[v].length; w++) {
    if (visited[g[v][w]] > dist + 1) {
      visited[g[v][w]] = dist + 1
      Q.push([g[v][w], dist + 1])
    }
  }
}
const ans = []

for (let j = 1; j < visited.length; j++) {
  if (visited[j] === K) {
    ans.push(j)
  } else if (visited[j] > K) {
    break
  }
}
console.log(ans.join("\n"))

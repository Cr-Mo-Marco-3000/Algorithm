const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map((x) => parseInt(x)))

const dr = [-1, 0, 1, 0, -1, 1, 1, -1]
const dc = [0, 1, 0, -1, 1, 1, -1, -1]

let checkLine = 0

ans = []

while (true) {
  const [m, n] = input[checkLine]
  if (m === 0 && n === 0) {
    break
  }

  const g = []

  for (let i = 1; i < n + 1; i++) {
    g.push(input[checkLine + i])
  }

  checkLine = checkLine + n + 1

  const visited = new Array(n).fill(0).map(() => new Array(m).fill(0))

  let cnt = 0

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (!visited[i][j] && g[i][j]) {
        cnt++
        const stack = [[i, j]]
        while (stack.length) {
          const [r, c] = stack.pop()
          if (!visited[r][c]) {
            visited[r][c] = 1
          }
          for (let w = 0; w < 8; w++) {
            const nr = r + dr[w]
            const nc = c + dc[w]
            if (
              0 <= nr &&
              nr < n &&
              0 <= nc &&
              nc < m &&
              !visited[nr][nc] &&
              g[nr][nc]
            ) {
              stack.push([nr, nc])
            }
          }
        }
      }
    }
  }
  ans.push(cnt)
}

console.log(ans.join("\n"))

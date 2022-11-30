let [N, ...input] = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

N = parseInt(N)

input = input.map((x) => x.split(" ").map((y) => parseInt(y)))

const g = new Array(N).fill(1)

for (let i = 0; i < N - 1; i++) {
  const [w1, h1] = input[i]
  for (let j = i + 1; j < N; j++) {
    const [w2, h2] = input[j]
    if (w1 < w2 && h1 < h2) {
      g[i]++
    } else if (w1 > w2 && h1 > h2) {
      g[j]++
    }
  }
}

console.log(...g)

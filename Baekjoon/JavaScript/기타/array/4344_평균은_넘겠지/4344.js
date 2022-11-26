let [T, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  // .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

for (let i = 0; i < T; i++) {
  const [N, ...scores] = input[i].split(" ").map((x) => parseInt(x))
  const sum = scores.reduce((sum, current, index) => sum + current, 0) / N
  let number = 0
  for (let j = 0; j < N; j++) {
    if (scores[j] > sum) {
      number++
    }
  }
  const ans = (number / N).toFixed(5).toString().split("").splice(2, 5)
  ans.splice(2, 0, ".")
  if (ans[0] === "0") {
    ans.shift()
  }
  console.log(`${ans.join("")}%`)
}

const [sum, N, ...list] = require("fs")
  .readFileSync("/dev/stdin")
  // .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

let ans = 0

for (let i = 0; i < N; i++) {
  const [a, b] = list[i].split(" ")
  ans += a * b
}

if (ans == sum) {
  console.log("Yes")
} else {
  console.log("No")
}

const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.trim())

const N = input.length

for (let i = 0; i < N - 1; i++) {
  const text = input[i]

  const M = text.length

  let flag = true

  for (let j = 0; j < parseInt(M / 2); j++) {
    if (text[j] === text[M - 1 - j]) {
    } else {
      flag = false
      break
    }
  }

  console.log(flag ? "yes" : "no")
}

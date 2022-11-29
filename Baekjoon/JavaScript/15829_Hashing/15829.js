let [n, str] = require("fs")
  // .readFileSync("./dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

const M = 1234567891
let result = 0
let r = 1
for (let i = 0; i < n; i++) {
  result += (str.charCodeAt(i) - 96) * r
  result %= M
  r *= 31
  r %= M
}

console.log(result)

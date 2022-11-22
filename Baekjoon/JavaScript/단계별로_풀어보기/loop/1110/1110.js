let N = parseInt(
  require("fs")
    .readFileSync("/dev/stdin")
    // .readFileSync("input.txt")
    .toString()
    .trim()
)
const crit = N

let ex = 0

let ans = 0

if (N < 10) {
  N = "0" + N
}

while (true) {
  const M = N.toString().split("")
  const start = M.at(0)
  const end = M.at(-1)
  N = (parseInt(start) + parseInt(end)).toString()
  N = end + (N % 10).toString()
  ans++
  if (N == crit) {
    break
  }
}

console.log(ans)

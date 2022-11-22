const N = parseInt(
  require("fs")
    // .readFileSync("/dev/stdin")
    .readFileSync("input.txt")
    .toString()
    .trim()
)

const func = function (N) {
  let ans = 0
  for (let i = N; i >= 1; i--) {
    const iString = i.toString()
    if (iString.length === 4) {
    } else if (iString.length === 3) {
      if (
        parseInt(iString[0]) - parseInt(iString[1]) ===
        parseInt(iString[1]) - parseInt(iString[2])
      ) {
        ans += 1
      }
    } else {
      ans += 1
    }
  }

  return ans
}

console.log(func(N))

const input = parseInt(
  require("fs").readFileSync("/dev/stdin").toString().trim()
)

const func = (cnt) => {
  if (cnt === 1) {
    return 1
  }
  return cnt * func(cnt - 1)
}

if (input === 0) {
  console.log(1)
} else {
  console.log(func(input))
}

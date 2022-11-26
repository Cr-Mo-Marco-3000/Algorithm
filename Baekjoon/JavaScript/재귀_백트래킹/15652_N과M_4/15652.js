const [N, M] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((x) => parseInt(x))

const ans = []

const stack = []

const func = (cnt) => {
  if (cnt === M) {
    ans.push(stack.join(" "))
  } else {
    for (let i = 1; i < N + 1; i++) {
      if (!stack.length || i >= stack.at(-1)) {
        stack.push(i)
        func(cnt + 1)
        stack.pop()
      }
    }
  }
}

func(0)

console.log(ans.join("\n"))

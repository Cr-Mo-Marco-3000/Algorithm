const [N, M] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((x) => parseInt(x))

const myList = new Array(N).fill(0)

const ans = []

for (let i = 0; i < N; i++) {
  myList[i] = i + 1
}

const func = (cnt, M) => {
  if (cnt === M) {
    ans.push()
  } else {
  }
}

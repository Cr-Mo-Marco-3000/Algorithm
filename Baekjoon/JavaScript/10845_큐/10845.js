const [N, ...input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(/\r\n|\r|\n/)

const Q = []

const ans = []

const ob = {
  pop: () => {
    Q.length ? ans.push(Q.shift()) : ans.push(-1)
  },
  size() {
    ans.push(Q.length)
  },
  empty() {
    ans.push(Q.length ? 0 : 1)
  },
  front() {
    ans.push(Q[0] || -1)
  },
  back() {
    ans.push(Q.at(-1) || -1)
  },
}
const L = input.length
for (let i = 0; i < L; i++) {
  const order = input[i]
  if (order.length > 5) {
    let [a, b] = order.split(" ")
    Q.push(parseInt(b))
  } else {
    ob[order]()
  }
}

console.log(ans.join("\n"))

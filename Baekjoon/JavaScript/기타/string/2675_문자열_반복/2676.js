const [N, ...input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

const ans = []
for (const i of input) {
  let temp = ""
  const [K, string] = i.split(" ")
  for (let j = 0; j < string.length; j++) {
    for (let k = 0; k < K; k++) {
      temp += string[j]
    }
  }
  ans.push(temp)
}

console.log(ans.join("\n"))

const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("")

// const myObject = {}
// for (let i = 97; i < 123; i++) {
//   myObject[String.fromCharCode(i)] = -1
// }

const ans = new Array(26).fill(-1)

for (let i = 0; i < input.length; i++) {
  const alpha = input[i].charCodeAt() - 97
  if (ans[alpha] === -1) {
    ans[alpha] = i
  } else {
  }
}

console.log(ans.join(" "))

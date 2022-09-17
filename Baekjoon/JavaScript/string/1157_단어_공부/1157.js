const input = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("")
  .map((x) => x.charCodeAt())

const myArray = new Array(26).fill(0)

for (let i of input) {
  if (i >= 97) {
    myArray[i - 97]++
  } else {
    myArray[i - 65]++
  }
}

const ans = Math.max(...myArray)

if (myArray.indexOf(ans) !== myArray.lastIndexOf(ans)) {
  console.log("?")
} else {
  const print = myArray.lastIndexOf(ans) + 65
  console.log(String.fromCharCode(print.toString()))
}

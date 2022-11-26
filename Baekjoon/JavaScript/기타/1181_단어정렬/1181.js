let [n, ...input] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

input = new Set(input)
input = [...input]

input.sort((x, y) => x.length - y.length)
input.sort((x, y) => {
  const xLength = x.length
  const yLength = y.length
  if (xLength !== yLength) {
    return xLength - yLength
  } else {
    for (let i = 0; i < xLength; i++) {
      if (x[i] !== y[i]) {
        return x[i].charCodeAt() - y[i].charCodeAt()
      } else {
      }
    }
  }
})
console.log(input.join("\n"))

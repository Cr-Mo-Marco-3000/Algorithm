const [n, ...input] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

const pr = []

for (const i of input) {
  const [a, b, c] = i.split(" ").map((x) => parseInt(x))
  const ans =
    ((c % a).toString() === "0" ? a : (c % a).toString()) +
    ((c % a === 0 ? parseInt(c / a) : parseInt(c / a) + 1).toString().length >=
    2
      ? (c % a === 0 ? parseInt(c / a) : parseInt(c / a) + 1).toString()
      : "0" + (c % a === 0 ? parseInt(c / a) : parseInt(c / a) + 1).toString())
  pr.push(ans)
}

console.log(pr.join("\n"))

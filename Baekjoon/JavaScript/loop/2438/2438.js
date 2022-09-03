const input = parseInt(
  require("fs")
    // .readFileSync("/dev/stdin")
    .readFileSync("input.txt")
    .toString()
    .trim()
)
const list = []

for (let i = 0; i < input; i++) {
  list.push(" ")
}

let string = list.join("")

for (let i = 0; i < input; i++) {
  list.shift()
  list.push("*")
  console.log(list.join(""))
}

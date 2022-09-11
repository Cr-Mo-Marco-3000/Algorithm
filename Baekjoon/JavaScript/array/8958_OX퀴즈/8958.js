const [N, ...myList] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

for (let i = 0; i < N; i++) {
  const eachList = myList[i].split("")
  const M = eachList.length
  let sum = 0
  let sumO = 0
  for (let j = 0; j < M; j++) {
    if (eachList[j] === "O") {
      sumO++
      sum += sumO
    } else if (eachList[j] === "X") {
      sumO = 0
    }
  }
  console.log(sum)
}

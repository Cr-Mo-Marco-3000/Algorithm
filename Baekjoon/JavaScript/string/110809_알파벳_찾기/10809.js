const input = require("fs")
  // .readFilesync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()

const L = input.length

const object = {}
console.log("z".charCodeAt())
for (let j = 97; j <= 122; j++) {
  object[j.toString(10)] = "z".charCodeAt()
  j.toString().fromCharCode()
}
console.log(object)
for (let i = 0; i < L; i++) {
  console.log(input[i])
}

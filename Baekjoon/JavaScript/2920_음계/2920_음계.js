const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .join("")

if (input === "12345678") {
  console.log("ascending")
} else if (input === "87654321") {
  console.log("descending")
} else {
  console.log("mixed")
}

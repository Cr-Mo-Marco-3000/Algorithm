const N = require('fs').readFileSync('/dev/stdin').toString().trim()
let sum = 0
for (let i=0; i <= N; i++) {
    sum += i
}
console.log(sum)
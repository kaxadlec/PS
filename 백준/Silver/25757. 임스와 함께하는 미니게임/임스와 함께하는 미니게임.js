const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);

let [n, gameType] = input[0].split(" ");
n = Number(n);
const people = input.slice(1);

const hashMap = {};
let capacity = 0;
if (gameType === "Y") {
  capacity = 1;
} else if (gameType === "F") {
  capacity = 2;
} else if (gameType === "O") {
  capacity = 3;
}

let cnt = 0;
let result = 0;
for (let elem of people) {
  if (hashMap[elem] === undefined) {
    hashMap[elem] = 1;
    cnt += 1;
  }

  if (cnt === capacity) {
    cnt = 0;
    result += 1;
  }
}

console.log(result);

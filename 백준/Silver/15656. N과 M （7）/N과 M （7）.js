const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);

let [N, M] = input[0].split(" ").map(Number);
let numbers = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
let path = [];
let result = "";

function backtrack(level) {
  if (level === M) {
    result += path.join(" ") + "\n";
    return;
  }

  for (let i = 0; i < N; i++) {
    path.push(numbers[i]);
    backtrack(level + 1);
    path.pop();
  }
}

backtrack(0);

console.log(result);

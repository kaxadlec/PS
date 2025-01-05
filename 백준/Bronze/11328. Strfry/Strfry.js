const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
let n = Number(input[0]);

function check(a, b) {
  let sorted_a = a.split("").sort().join("");
  let sorted_b = b.split("").sort().join("");
  const result = sorted_a === sorted_b ? 1 : 0;

  return result;
}
for (let i = 1; i < n + 1; i++) {
  [first, second] = input[i].split(" ");
  let result = check(first, second);
  const answer = result === 1 ? "Possible" : "Impossible";
  console.log(answer);
}

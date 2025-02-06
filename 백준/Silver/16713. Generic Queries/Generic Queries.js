const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
// let input = fs.readFileSync("input.txt").toString().trim();
// let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
// let input = fs.readFileSync("dev/stdin").toString().trim();
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split(/\r?\n/);

let [N, Q] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);
let dp = Array(N).fill(0);
dp[0] = arr[0];
for (let i = 1; i < N; i++) {
  dp[i] = dp[i - 1] ^ arr[i];
}

result = 0;
for (let i = 0; i < Q; i++) {
  let [s, e] = input[i + 2].split(" ").map(Number);
  let queryRes = s === 1 ? dp[e - 1] : dp[e - 1] ^ dp[s - 2];
  result ^= queryRes;
}

console.log(result);


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

let [N, M] = input[0].split(" ").map(Number);
let dist = input.slice(1, N + 1).map(Number);
let weather = input.slice(N + 1).map(Number);
let dp = Array.from({ length: N }, () => Array(M - N + 1).fill(0));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M - N + 1; j++) {
    const cost = dist[i] * weather[i + j];
    if (i === 0) dp[i][j] = j === 0 ? cost : Math.min(cost, dp[i][j - 1]);
    else dp[i][j] = j === 0  ? cost + dp[i - 1][j] : Math.min(cost + dp[i - 1][j], dp[i][j - 1]);
  }
}

console.log(dp[N - 1][M - N]);

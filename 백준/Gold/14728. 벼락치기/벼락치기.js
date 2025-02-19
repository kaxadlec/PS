const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt").toString().trim().split(/\r?\n/);

const [N, T] = input[0].split(" ").map(Number);
let times = Array(N).fill(0);
let scores = Array(N).fill(0);
for (let i = 0; i < N; i++) {
  let [time, score] = input[i + 1].split(" ").map(Number);
  times[i] = time;
  scores[i] = score;
}

let dp = Array.from({length: N+1}, () => Array(T+1).fill(0));

for (let i = 1; i < N+1; i++) {
  for (let t = 1; t < T+1; t++) {
    if (times[i - 1] <= t) {
      dp[i][t] = Math.max(dp[i-1][t], dp[i-1][t - times[i - 1]] + scores[i - 1]);

    } else {
      dp[i][t] = dp[i-1][t];
    }
  }
}

console.log(dp[N][T]);
const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
// let input = fs.readFileSync("input.txt").toString().trim();
// let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
let input = fs.readFileSync("dev/stdin").toString().trim();
let N = Number(input);
let fibo = Array(N)
  .fill(0)
  .map(() => Array(2).fill(0));

fibo[0][0] = 2;
fibo[0][1] = 1;
for (let i = 1; i < N; i++) {
  fibo[i][0] = fibo[i - 1][0] + fibo[i - 1][1];
  fibo[i][1] = fibo[i - 1][0];
}
// console.log(fibo);

let dp = Array(N + 1)
  .fill(0)
  .map(() => Array(2).fill(0));

let person = 0;
for (let elem of fibo) {
  person = elem[0];
  chicken = elem[1];
  if (person <= N) {
    dp[person][0] = chicken;
    dp[person][1] = chicken;
  } else {
    break;
  }
}

let half_num = 0;
for (let i = 4; i < N + 1; i++) {
  half_num = Math.floor(i / 2);
  for (let j = 2; j <= half_num; j++) {
    if (dp[i][0] !== 0) {
      dp[i][0] = Math.min(dp[i][0], dp[j][0] + dp[i - j][0]);
    } else {
      dp[i][0] = dp[j][0] + dp[i - j][0];
    }
    dp[i][1] = Math.max(dp[i][1], dp[j][1] + dp[i - j][1]);
  }
}

console.log(dp[N][0], dp[N][1]);

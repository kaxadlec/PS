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

let [M, N, K] = input[0].split(" ").map(Number);
// let arr2d = Array.from({ length: M }, () => Array(N).fill(0));
let board = Array(M)
  .fill(null)
  .map(() => Array(N).fill(0));
for (let idx = 1; idx < K + 1; idx++) {
  let coordinate = input[idx].split(" ").map(Number);
  let [i1, j1] = [coordinate[1], coordinate[0]];
  let [i2, j2] = [coordinate[3] - 1, coordinate[2] - 1];
  for (let i = i1; i <= i2; i++) {
    for (let j = j1; j <= j2; j++) {
      board[i][j] = 1;
    }
  }
}

const directions = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
function dfs(i, j) {
  // console.log(i, j);
  for (const [di, dj] of directions) {
    const ni = di + i;
    const nj = dj + j;
    if (ni < 0 || ni >= M || nj < 0 || nj >= N) continue;
    if (board[ni][nj] === 1) continue;
    board[ni][nj] = 1;
    check++;
    dfs(ni, nj);
  }
}

let cnt = 0;
let result = [];
let check;
for (let i = 0; i < M; i++) {
  for (let j = 0; j < N; j++) {
    if (board[i][j] === 0) {
      cnt++;
      check = 1;
      board[i][j] = 1;
      dfs(i, j);
      result.push(check);
    }
  }
}

console.log(cnt);
console.log(result.sort((a, b) => a - b).join(" "));

const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
// let input = fs.readFileSync("input.txt").toString().trim();
// let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
let input = fs.readFileSync("dev/stdin").toString().trim();
let [N, M, K] = input.split(" ").map(Number);
let arr2d = Array(N)
  .fill(0)
  .map(() => Array(M).fill(0));

if (N + M - 1 > K) {
  console.log("NO");
} else {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      arr2d[i][j] = i + j + 1;
    }
  }
  console.log("YES");
  for (let row of arr2d) {
    let str = "";
    for (let elem of row) {
      str += elem + " ";
    }
    console.log(str);
  }
}

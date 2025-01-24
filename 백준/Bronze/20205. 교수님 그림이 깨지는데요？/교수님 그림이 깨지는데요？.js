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

let [n, k] = input[0].split(" ").map(Number);
let board = input.slice(1).map(row => row.split(" ").map(Number))
let newBoard = Array.from({length: n*k}, () => Array(n*k).fill(0));

for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        for (let ni = i * k; ni < (i+1) * k; ni++) {
            for (let nj = j * k; nj < (j + 1) * k; nj++) {
                newBoard[ni][nj] = board[i][j];
            }
        }
    }
}

newBoard.forEach(row => {
    console.log(row.join(" "));
})
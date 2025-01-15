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

let N = Number(input[0]);
let flowers = input[1].split(" ").map(Number);
let Q = Number(input[2]);
let result = "";
for (let i = 3; i < 3 + Q; i++) {
  const query = input[i].split(" ").map(Number);
  const [st, en] = [query[1] - 1, query[2] - 1];
  if (query[0] === 1) {
    const targetNum = query[3];
    const res = flowers
      .slice(st, en + 1)
      .filter((num) => num === targetNum).length;
    result += `${res}\n`;
  } else {
    flowers.fill(0, st, en + 1);
  }
}

console.log(result);

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
let eggs = input.slice(1).map(str => str.split(" ").map(Number));
let maxBrokenEggCnt = 0;

function backtrack(handIdx, brokenEggCnt) {
  // console.log("handIdx", "brokenEggCnt", handIdx, brokenEggCnt);
  if (handIdx === N) {
    maxBrokenEggCnt = Math.max(maxBrokenEggCnt, brokenEggCnt);
    return;
  }
  if (eggs[handIdx][0] <= 0) {
    backtrack(handIdx + 1, brokenEggCnt);
    return;
  }

  let isHit = false;
  for (let targetIdx = 0; targetIdx < N; targetIdx++) {
    if (targetIdx === handIdx) continue;
    if (eggs[targetIdx][0] <= 0) continue;
    
    isHit = true;
    eggs[handIdx][0] -= eggs[targetIdx][1];
    eggs[targetIdx][0] -= eggs[handIdx][1];
    let newBrokenEggCnt = brokenEggCnt;
    if (eggs[handIdx][0] <= 0) newBrokenEggCnt += 1;
    if (eggs[targetIdx][0] <= 0) newBrokenEggCnt += 1;
    backtrack(handIdx + 1, newBrokenEggCnt);
    eggs[handIdx][0] += eggs[targetIdx][1];
    eggs[targetIdx][0] += eggs[handIdx][1];
  }

  if (!isHit) backtrack(handIdx + 1, brokenEggCnt);
}

backtrack(0, 0);

console.log(maxBrokenEggCnt);
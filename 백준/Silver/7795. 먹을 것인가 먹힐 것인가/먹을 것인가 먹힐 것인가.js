const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt").toString().trim().split(/\r?\n/);
const T = Number(input[0]);
let result = "";
for (let tc = 0; tc < T; tc++) {
  let [N, M] = input[3*tc + 1].split(" ").map(Number);
  let aSet = input[3*tc+2].split(" ").map(Number);
  let bSet = input[3*tc+3].split(" ").map(Number);
  bSet.sort((a, b) => a - b);
  let res = 0;
  for (let a of aSet) {
    res += lowerBound(bSet, M, a);
    // console.log(res);
  }
  result += res + "\n";
}

function lowerBound(arr, arrLen, target) {
  let left = 0;
  let right = arrLen - 1;
  let minIdx = arrLen;
  let mid;

  while (left <= right) {
    mid = parseInt((left+right) / 2);
    // console.log("mid", mid)

    if (arr[mid] >= target) {
      right = mid - 1;
      minIdx = Math.min(minIdx, mid);
    }
    else {
      left = mid + 1;
    }
  }
  return minIdx;
}

console.log(result.trim());
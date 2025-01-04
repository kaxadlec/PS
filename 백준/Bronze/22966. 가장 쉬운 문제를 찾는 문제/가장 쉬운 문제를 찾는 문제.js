const fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
let n = Number(input[0]);

let result = "";
let min_num = 5;

for (let i = 1; i < n + 1; i++) {
  [title, num] = input[i].split(" ");
  num = Number(num);

  if (min_num > num) {
    min_num = num;
    result = title;
  }
}

console.log(result);

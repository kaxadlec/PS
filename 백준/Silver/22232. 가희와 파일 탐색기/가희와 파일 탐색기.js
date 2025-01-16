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

const [N, M] = input[0].split(" ").map(Number);
let files = input.slice(1, N + 1);
let OSexe = new Set(input.slice(N + 1));

files.sort();
let fileName = Array(N).fill(0);
let fileExe = Array(N).fill(0);
for (let i = 0; i < N; i++) {
  fileName[i] = files[i].split(".")[0];
  fileExe[i] = files[i].split(".")[1];
}

let fileNameSet = new Set(fileName);
let fileDictOS = {};
let fileDict = {};
for (let key of fileNameSet) {
  fileDictOS[key] = [];
  fileDict[key] = [];
}

for (let i = 0; i < N; i++) {
  if (OSexe.has(fileExe[i])) {
    fileDictOS[fileName[i]].push(fileExe[i]);
  } else {
    fileDict[fileName[i]].push(fileExe[i]);
  }
}
for (let key in fileDictOS) {
  fileDictOS[key].sort();
}
for (let key in fileDict) {
  fileDict[key].sort();
}

let result = [];
for (let key of fileNameSet) {
  let arr1 = fileDictOS[key];
  let arr2 = fileDict[key];
  for (let elem of arr1) {
    result.push(`${key}.${elem}`);
  }
  for (let elem of arr2) {
    result.push(`${key}.${elem}`);
  }
}

console.log(result.join("\n"));

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

let [N, M] = input[0].split(" ").map(Number);
let S = input[1];
let T;
let eraseChance = N - M;
const vowels = ['A', 'E', 'I', 'O', 'U'];
let lastIndex = S.length - 1;
let favoriteS = "";
let canChooseS = false;
let firstflag = false;
let secondflag = false;
let secondLastIndex;
let thirdLastIndex;

while (eraseChance >= 0) {
    if (!firstflag) {
        const lastChar = S[lastIndex];
        if (vowels.includes(lastChar)) {
            eraseChance--;
            lastIndex--;
            continue;
        } 
        secondLastIndex = lastIndex - 1;
        favoriteS += lastChar;
        firstflag = true;
    }

    if (!secondflag) {
        const secondLastChar = S[secondLastIndex];
        if (secondLastChar !== 'A') {
            eraseChance--;
            secondLastIndex--;
            continue;
        } 
        thirdLastIndex = secondLastIndex - 1;
        favoriteS += secondLastChar;
        secondflag = true;
    }
    
   
    const thirdLastChar = S[thirdLastIndex];
    if (thirdLastChar !== 'A') {
        eraseChance--;
        thirdLastIndex--;
        continue;
    } 
    favoriteS += thirdLastChar;
    canChooseS = true;

    if (canChooseS) {
        for (let i = thirdLastIndex - 1; i >= 0; i--) {
            favoriteS += S[i];
        }
        favoriteS = favoriteS.split('').reverse().join('')
        break;
    }
}

if (canChooseS) {
    while (1) {
        if (favoriteS.length === M) {
            break
        } else if (favoriteS.length > M) {
            favoriteS = favoriteS.slice(1);
        } 
    }
}

if (canChooseS) {
    console.log("YES");
    console.log(favoriteS);
} else {
    console.log("NO");
}
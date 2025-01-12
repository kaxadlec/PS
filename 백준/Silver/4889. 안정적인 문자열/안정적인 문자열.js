const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split(/\r?\n/);

class Stack {
  constructor() {
    this.stack = [];
  }
  push(item) {
    this.stack.push(item);
  }
  isEmpty() {
    return this.stack.length === 0;
  }
  size() {
    return this.stack.length;
  }
  pop() {
    if (this.isEmpty()) {
      throw new Error();
    }
    return this.stack.pop();
  }
  top() {
    if (this.isEmpty()) {
      throw new Error();
    }
    return this.stack[this.stack.length - 1];
  }
}

function calculation(dataSet) {
  const stack = new Stack();
  let result = 0;
  for (let data of dataSet) {
    if (stack.isEmpty()) {
      stack.push(data);
    } else if (stack.top() === "{" && data === "}") {
      stack.pop();
    } else {
      stack.push(data);
    }
  }
  let check = 0;
  while (!stack.isEmpty()) {
    check++;
    if (check % 2 == 1) {
      if (stack.pop() === "{") {
        result++;
      }
    } else {
      if (stack.pop() === "}") {
        result++;
      }
    }
  }
  return result;
}

let test_num = 0;
for (let line of input) {
  if (line.indexOf("-") !== -1) {
    break;
  }
  test_num++;
  const result = calculation(line);
  console.log(`${test_num}. ${result}`);
}

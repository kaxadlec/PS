const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim().split(/\r?\n/);
// let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
// let input = fs.readFileSync("dev/stdin").toString().trim();
let [n, bridgeLen, maxLoad] = input[0].split(" ").map(Number);
let trucks = input[1].split(" ").map(Number);
class Queue {
  constructor() {
    this.q = [];
    this.head = -1;
    this.tail = -1;
  }

  logState() {
    console.log(`queue: [${this.q.slice(this.head + 1)}]`);
  }

  append(item) {
    this.q.push(item);
    this.tail++;
  }

  empty() {
    return this.head === this.tail;
  }

  size() {
    return this.tail - this.head;
  }

  popleft() {
    if (this.empty()) {
      throw new Error();
    }
    return this.q[++this.head];
  }
  front() {
    if (this.empty()) {
      throw new Error();
    }
    return this.q[this.head + 1];
  }
}

const waitingQ = new Queue();
trucks.forEach((item) => waitingQ.append(item));
const bridgeQ = new Queue();
const popCheckQ = new Queue();
let cnt = 0;
let loadOnBridge = 0;

while (!waitingQ.empty() || !bridgeQ.empty()) {
  cnt++;
  // console.log(`cnt ${cnt}`);

  if (!popCheckQ.empty() && popCheckQ.front() === cnt) {
    popCheckQ.popleft();
    let popTruck = bridgeQ.popleft();
    loadOnBridge -= popTruck;
  }
  if (!waitingQ.empty()) {
    let truck = waitingQ.front();
    if (maxLoad < loadOnBridge + truck) {
      continue;
    }
    waitingQ.popleft();
    bridgeQ.append(truck);
    popCheckQ.append(cnt + bridgeLen);
    loadOnBridge += truck;
  }

  // console.log(`watingQ`);
  // waitingQ.logState();
  // console.log(`bridgeQ`);
  // bridgeQ.logState();
  // console.log(`popCheckQ`);
  // popCheckQ.logState();
  // console.log("\n");
}

console.log(cnt);

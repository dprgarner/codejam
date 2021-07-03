// const { strict: assert } = require("assert");

const MAX = 100000;

const arr = [0];
for (let i = 1; i < MAX; i++) {
  arr.push(Infinity);
}

for (let i = 0; i < MAX; i++) {
  const reversed = parseInt(`${i}`.split("").reverse().join(""), 10);
  if (reversed > i) {
    arr[reversed] = Math.min(arr[reversed], 1 + arr[i]);
  }
  arr[i + 1] = Math.min(arr[i + 1], 1 + arr[i]);
}

// // Check against itself. This DP approach works if and only if we can't get a
// // more optimal answer on a second pass.
// for (let i = 0; i < MAX; i++) {
//   const reversed = parseInt(`${i}`.split("").reverse().join(""), 10);
//   if (reversed < MAX) {
//     assert(arr[reversed] <= 1 + arr[i], `${i}, ${arr[reversed]}, ${arr[i]}`);
//   }
//   assert(arr[i + 1] <= 1 + arr[i], `${i}, end`);
// }
// console.log("verified");

// // Check against explicit value of `solve`
// for (let i = 0; i < MAX; i++) {
//   if (solve(i) !== arr[i]) {
//     throw new Error(`${i}, ${solve(i)}, ${arr[i]}`);
//   }
// }

function eg(start, end) {
  for (let i = start; i < end; i++) {
    console.log(`${i}: ${arr[i]}`);
  }
}

eg(90, 110);
eg(990, 1010);
eg(9990, 10010);

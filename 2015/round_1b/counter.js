// https://codingcompetitions.withgoogle.com/codejam/round/0000000000433551/0000000000433a0f
const readline = require("readline");

const fastestToPower = {
  1: 10,
  2: 29,
  3: 138,
  4: 337,
  5: 1436,
  6: 3435,
  7: 14434,
  8: 34433,
  9: 144432,
  10: 344431,
  11: 1444430,
  12: 3444429,
  13: 14444428,
  14: 34444427,
};

function solve(target) {
  if (target <= 10) return target;
  const digits = `${target}`.length;
  let count = fastestToPower[digits - 1];
  if (target == 10 ** (digits - 1)) return count;

  const lastDigitZero = `${target}`.slice(-1) == "0";
  if (lastDigitZero) target -= 1;

  const firstHalfLength = Math.floor(digits / 2);
  const secondHalfLength = Math.ceil(digits / 2);

  let firstHalf = `${target}`.slice(0, firstHalfLength);
  firstHalf = parseInt(firstHalf.split("").reverse().join(""), 10);
  const secondHalf = parseInt(`${target}`.slice(-secondHalfLength));

  if (firstHalf !== 1) {
    // Count out the (reversed) first half, then reverse.
    // The second half is then 0...01.
    count += firstHalf;
  }

  count += secondHalf;
  if (lastDigitZero) count += 1;
  return count;
}

async function processLineByLine() {
  const iterator = readline
    .createInterface({
      input: process.stdin,
      crlfDelay: Infinity,
    })
    [Symbol.asyncIterator]();

  const testCases = parseInt((await iterator.next()).value, 10);
  for (let i = 1; i < testCases + 1; i++) {
    const soln = solve(parseInt((await iterator.next()).value, 10));
    console.log(`Case #${i}: ${soln}`);
  }
}

processLineByLine();

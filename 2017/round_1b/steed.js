function solve(distance, horses) {
  let max_time = 0
  for (const [d1, s1] of horses) {
    max_time = Math.max(max_time, (distance - d1) / s1)
  }
  return distance / max_time
}

const readline = require('readline');
const util = require('util');

async function processLineByLine() {
  const iterator = readline.createInterface({
    input: process.stdin,
    crlfDelay: Infinity
  })[Symbol.asyncIterator]();

  const testCases = (parseInt((await iterator.next()).value, 10))
  for (let i = 1; i < testCases + 1; i++) {
    const [totalDistance, horseCount] = (await iterator.next()).value.split(' ').map(x => parseInt(x, 10));
    const horses =[];
    for (let h = 0; h < horseCount; h++) {
      const [distance, speed] = (await iterator.next()).value.split(' ').map(x => parseInt(x, 10));
      horses.push([distance, speed]);
    }
    const soln = solve(totalDistance, horses);
    console.log(`Case #${i}: ${soln}`);
  }
}

processLineByLine();

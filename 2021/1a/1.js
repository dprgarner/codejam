function solve(arr) {
  throw new Error('TODO')
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
    const _len = (parseInt((await iterator.next()).value, 10));
    const arr = (await iterator.next()).value.split(' ').map(x => parseInt(x, 10));
    const soln = solve(arr);
    console.log(`Case #${i}: ${soln}`);
  }
}

processLineByLine();

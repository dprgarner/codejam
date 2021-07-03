// fastestToPower[i] is the minimum number of turns to get to 10**i.
const fastestToPower = {};

function precalculate() {
  fastestToPower[1] = 10;
  let count = 10;
  for (let i = 2; i < 15; i++) {
    count += 10 ** Math.ceil(i / 2) - 1 + 1 + 10 ** Math.ceil((i - 1) / 2) - 1;
    fastestToPower[i] = count;
  }
  console.log(fastestToPower);
}

precalculate();

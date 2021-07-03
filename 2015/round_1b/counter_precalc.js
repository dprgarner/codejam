// fastestToPower[i] is the minimum number of turns to get to 10**i.
const fastestToPower = {};

function precalculate() {
  fastestToPower[1] = 10;
  let count = 10;
  for (let i = 2; i < 15; i++) {
    // The fastest way to get from 10...0 to the next power of ten is to:
    // - Count up to 100...09...999
    // - Reverse the number
    // - Count up from 999...90...01 to 99...9
    // - Count over to the next power of 10.
    count += 10 ** Math.ceil(i / 2) - 1 + 1 + 10 ** Math.ceil((i - 1) / 2) - 1;
    fastestToPower[i] = count;
  }
  console.log(fastestToPower);
}

precalculate();

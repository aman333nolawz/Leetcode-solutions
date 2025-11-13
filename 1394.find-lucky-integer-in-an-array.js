// @leet start
/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function (arr) {
  const eachCount = new Map();
  const luckyNumbers = new Set();

  for (let i = 0; i < arr.length; i++) {
    const number = arr[i];
    let count;
    if (eachCount.has(number)) {
      count = eachCount.get(number);
      eachCount.set(number, count + 1);
      count += 1;
    } else {
      eachCount.set(number, 1);
      count = 1;
    }

    if (number == count) {
      luckyNumbers.add(number);
    }

    if (number != count && luckyNumbers.has(number)) {
      luckyNumbers.delete(number);
    }
  }

  return [...luckyNumbers.values()].length > 0
    ? Math.max(...luckyNumbers.values())
    : -1;
};
// @leet end


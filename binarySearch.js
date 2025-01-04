// binary search in a sorted array

const first_and_last = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    //define mid
    let mid = Math.floor((left + right) / 2);
    // if targets matches the mid return it
    if (nums[mid] === target) {
      return mid;
      // if target is below the mid then switch up the array to let the right end to be mid - 1
    } else if (nums[mid] > target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
};
console.log(first_and_last([1, 3, 5, 7, 9, 11], 7));

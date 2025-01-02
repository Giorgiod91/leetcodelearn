// binary search in a sorted array

const first_and_last = (nums, target) => {
  left = 0;
  right = nums.length - 1;
  mid = left + right / 2;

  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (nums[mid] == target) {
      return target;
    } else if (nums[mid] > target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
};
console.log(first_and_last([1, 3, 5, 7, 9, 11], 7));

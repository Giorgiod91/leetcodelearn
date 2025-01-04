const binarySearch = (array, target) => {
  left = 0;
  right = array.length - 1;

  while (left < right) {
    mid = Math.floor((left + right) / 2);
    if (array[mid] === target) {
      return mid;
    } else if (target < array[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
};
console.log(binarySearch([1, 2, 4, 5, 6, 7, 8], 5));

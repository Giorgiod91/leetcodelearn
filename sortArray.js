const bubbleSort = (array) => {
  // Loop through the array
  for (let i = 0; i < array.length - 1; i++) {
    // Inner loop to perform comparisons
    for (let j = 0; j < array.length - 1 - i; j++) {
      // Swap if the current element is greater than the next
      if (array[j] > array[j + 1]) {
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }

  return array; // Return the sorted array
};

// Test the function
console.log(bubbleSort([5, 2, 9, 1]));

// challenge remove duplicates if there are some

const removeDuplicatesFromSortedArray = (array) => {
  //define empty array
  let newArray = [];
  //loop through
  for (let i = 0; i < array.length; i++) {
    //check if the number at current index is not allready in the new array to avoid duplicates then if its true push the value at the index into new array
    if (!newArray.includes(array[i])) {
      newArray.push(array[i]);
    }
  }
  // return new array
  return newArray;
};

console.log(removeDuplicatesFromSortedArray([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));

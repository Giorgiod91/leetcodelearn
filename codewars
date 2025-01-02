// remove all items but not the last 4
// "4556364607935616" --> "############5616"
//   "64607935616" -->      "#######5616"

// "What was the name of your first pet?"
//"Skippy" --> "##ippy"
// "Nananananananananananananananana Batman!" --> "####################################man!"

const removeAllButLast4 = (inputString) => {
  // Determine the length of the string minus the last 4 characters
  const newStringLength = inputString.length - 4;

  // Create a new string with '#' for all characters except the last 4
  const newString = "#".repeat(newStringLength) + inputString.slice(-4);

  return newString;
};

console.log(removeAllButLast4("4556364607935616"));

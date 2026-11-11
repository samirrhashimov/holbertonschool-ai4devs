// Calculates the average of the numbers in an array
function average(numbers) {
    if (numbers.length === 0) {
      return 0;
    }
  
    let total = 0;
    // FIX: use < instead of <= so the loop stops at the last element
    for (let i = 0; i < numbers.length; i++) {
      total += numbers[i];
    }
  
    return total / numbers.length;
  }
  
  console.assert(average([80, 90, 70, 100]) === 85, "Test 1 failed");
  console.assert(average([10]) === 10, "Test 2 failed");
  console.assert(average([]) === 0, "Test 3 failed");
  console.log("All 3 test cases passed");
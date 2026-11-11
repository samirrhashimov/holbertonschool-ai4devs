// Calculates the average of the numbers in an array
function average(numbers) {
    let total = 0;
  
    // BUG: loop goes one step beyond the end of the array
    for (let i = 0; i <= numbers.length; i++) {
      total += numbers[i];
    }
  
    return total / numbers.length;
  }
  
  const scores = [80, 90, 70, 100];
  console.log("Average:", average(scores)); // Expected: 85
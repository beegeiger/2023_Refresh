JavaScript Refresh 2023
Easy
Third Greatest
def ThirdGreatest(strArr):
  strArr.remove(max(strArr, key=len))
  strArr.remove(max(strArr, key=len))
  return max(strArr, key=len)

# keep this function call here 
print(ThirdGreatest(input()))

Easy
Hamming Distance
function HammingDistance(strArr) { 
  let out = 0
  var i
  for (let i=0; i < strArr[0].length; i++) {
    if (strArr[0][i] != strArr[1][i]) {
      out += 1
    }
  }
  return(out)
}
   
// keep this function call here 
console.log(HammingDistance(readline()));

Easy
Number Addition
function NumberAddition(str) { 
  let out = 0
  let tracker = ""
  var i
  for (let i = 0; i<str.length; i++) {
    if (isNaN(str[i]) == false && str[i] != " ") {
      tracker += str[i]
    } else {
      if (tracker.length > 0) {
        out += parseInt(tracker)
        tracker = ""
      }
    }
  }
  if (tracker.length > 0) {
        out += parseInt(tracker)
        tracker = ""
  }
  return out; 

}
   
// keep this function call here 
console.log(NumberAddition(readline()));

Easy 
Vowel Count
function VowelCount(str) { 
  let vowels = "aeiouAEIOU"
  let counter = 0
  var i
  for (let i = 0; i < str.length; i++) {
    if (vowels.includes(str[i])) {
      counter += 1
    }
  }
  return counter; 

}
   
// keep this function call here 
console.log(VowelCount(readline()));

Easy
Dash Insert
function DashInsert(str) { 
  let output = ""
  var i
  for (let i=0; i<str.length; i++) {
    if (output.length > 0 ) {
      if (isNaN(output.charAt(output.length - 1)) == false) {
        if (parseInt(output.charAt(output.length - 1)) % 2 == 1 && parseInt(str[i]) % 2 == 1) {
          output += "-"
        }
      }
    }
    output += str[i]
  }  
  return output; 

}
   
// keep this function call here 
console.log(DashInsert(readline()));


Medium
Binary Converter

function BinaryConverter(str) { 
  let reverString = str.split("").reverse().join("")
  let output = 0
  let counter = 1
  var i
  for (let i=0 ; i<str.length; i++) {
    if (reverString[i] == "1") {
      output += counter
    }
    counter = counter * 2
  }
  return output; 

}

// keep this function call here 
console.log(BinaryConverter(readline()));

Medium
Fibonacci Checker
function FibonacciChecker(num) { 
  let fib = [1,2]
  var i
  for (let i = 0; i<50; i++) {
    fib.push(fib[i]+fib[i+1])
  }  
  if (fib.includes(num)){
    return "yes"
  }; 
  return "no"
}
   
// keep this function call here 
console.log(FibonacciChecker(readline()));


Medium
Consecutive
function Consecutive(arr) { 
  let values = arr
  values.sort(function(a, b){return a - b});
  let counter = 0
  var i
  for (let i = 0; i<values.length; i++) {
    if (i > 0) {
      if (values[i] - values[i - 1] > 1) {
        counter += (values[i] - values[i - 1]) - 1
      }
    }
  }  
  return counter; 

}
   
// keep this function call here 
console.log(Consecutive(readline()));


function arrayDiff(a, b) {
  let output = []
  var i
  for (let i=0; i<a.length; i++) {
    if (b.includes(a[i]) == false) {
      output.push(a[i])
    }
  }
  return output
}

function isPangram(string){
  let alpha = "abcdefghijklmnopqrstuvwxyz"
  var i
  for (let i = 0; i<alpha.length; i++) {
    if (string.includes(alpha[i]) == false) {
      return false
    }
  }
  return true
}

function isPangram(stri){
  let alpha = "abcdefghijklmnopqrstuvwxyz"
  let string = stri.toLowerCase()
  var i
  for (let i = 0; i<alpha.length; i++) {
    if (string.includes(alpha[i]) == false) {
      return false
    }
  }
  return true
}

function OverlappingRanges(arr) { 
  let l1 = []
  let l2 = []
  let counter = 0

  for(i=arr[0]; i<=arr[1]; i++){
    l1.push(i);
  };

  for(j=arr[2]; j<=arr[3]; j++){
    l2.push(j);
  };


  for (x in l1) {
    if (x in l2) {
      counter +=1;
    }
  }
  if (counter >= arr[4]) {
    return 'true'
  } else {
    return 'false'
  }

}
   
// keep this function call here 
console.log(OverlappingRanges(readline()));
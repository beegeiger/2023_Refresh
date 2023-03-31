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
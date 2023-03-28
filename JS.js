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
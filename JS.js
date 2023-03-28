JavaScript Refresh 2023
Easy
Third Greatest
def ThirdGreatest(strArr):
  strArr.remove(max(strArr, key=len))
  strArr.remove(max(strArr, key=len))
  return max(strArr, key=len)

# keep this function call here 
print(ThirdGreatest(input()))
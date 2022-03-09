let arr = intArr(readLine(strippingNewline: true)!)
var sum = 0
for i in arr{
     sum += i
}
print(sum)
func intArr(_ str: String) -> [Int] {
   let split = str.split(separator: " ")
   return split.compactMap({ Int($0) })
}

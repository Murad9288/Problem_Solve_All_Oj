# Hello

print("Hello world")

# Namota

n = int(input())
for i in range(1,11):
  print("%d x %d = %d"%(n,i,i*n))
  
  
  # output:
  
  '''
  n  = 10
  
  10 x 1 = 10
  10 x 2 = 20
  10 x 3 = 30
  10 x 4 = 40
  10 x 5 = 50
  10 x 6 = 60
  10 x 7 = 70
  10 x 8 = 80
  10 x 9 = 90
  10 x 10 = 100
  
  
  '''
  
  //
//  Main.swift
//  Swift_All_Problem
//
//  Created by Md Murad Hossain on 5/7/22.
//


import Foundation


/*
 
import Foundation
let t = Int(readLine()!)!
for _ in 1...t{
 // array input:
    let arr = readLine()!.split(separator: " ").map { Int($0)!}
    let a = arr[0]
    let r = arr[1]
    let n = arr[2]
    var res = a
    var total = a
    for _ in 2...n{
        total *= r
        res += total
    }
    print(res)
}
*/



// Switch case a range use korar subidha ache.
/*
var murad = 100
switch murad{
case 80...100:
    print("A+")
case 70...79:
    print("A")
default:
    print("Fail")
}
 */
// range baad diye..
/*
var murad = 34
switch murad{
case 1:
    print("Number is one")
case 2:
    print("Number is two")
default:
    print("Number is Invalid")
}
*/


// Array:
/*
var fruits = ["apple","mango","banana","orange"]
print("Count the array: \(fruits.count)")
var array = [String]()
array.append("3") // Blank_Array.
array.append("Apple")
print(array)

*/

/*

func sum(a:Int,b:Int)->(c:Int,d:Int){
    let c = a
    let d = b
    return (c,d)
}
var Result = sum(a: 3, b: 10)
print(Result.c)
print(Result.d)

*/

// MARK: Fucntion Creator and  used swift.

/*
func simple(string: String) -> String{
    return string
}
print(simple(string: "Hello, Swift"))
 */

// MARK: CAT Simple.

/*
func cat(c: String) -> String{
    return c
    
}
var t = "🐱"
print(cat(c: t))
*/


 

//
//
//let s = 25
//var b =  [Int](repeating: 0, count: s+1)
//
//b[03] = +08
//b[06] = +11
//b[09] = +09
//b[10] = +02
//b[14] = -10
//
//print(b)
//
//var sq = 0
//var roll = 0
//while sq < s{
//    roll += 1
//    if roll == 7{
//        roll = 1
//    }
//    sq += roll
//    if sq < b.count{
//        sq += b[sq]
//    }
//}
//print("Game Over")
//
//
// MARK: Null Array Code
//
//var a = [Int](repeating: 0, count: 100)
//print(a)
//
//

// MARK: Conditional Statements
//
//var t = 30
//if t <= 32 {
//    print("Yes")
//}
//else{
//    print("No")
//}

// MARK: Switch Case:
//
//let character: Character = "c"
//switch character{
//case "a":
//    print("1st Character")
//case "z":
//    print("last Character")
//default:
//    print("Some the character")
//}


// MARK: Interval matching
//
//let a: Character = "a"
//switch a{
//case "A", "a":
//    print("The letter A")
//default:
//    print("Not the letter A")
//}
//
//let a = 62
//let c = "Moons orbiting Saturn"
//let n: String
//switch a{
//case 0:
//    n = "No"
//case 1..<5:
//    n = "a few"
//case 5..<12:
//    n = "several"
//case 12..<100:
//    n = "dozens of"
//case 100..<1000:
//    n = "hundreds of"
//default:
//    n = "many"
//
//}
//print("There are \(n) \(c).")
//
//
// MARK: Tuples
//
//let p = (1,1)
//switch p{
//case (0,0):
//    print("point is at the origin")
//case (_,0):
//    print("is on thex-axis")
//case (0,_):
//    print("is on the y-axis")
//case (-2...2, -2...2):
//    print("is inside the box")
//default:
//    print("is outside of the box")
//
//}

// MARK: Value Bindings
//
//let a = (2,0)
//switch a {
//case (let x,0):
//    print("on the x-axis with an x value of \(x)")
//case (0,let y):
//    print("on the y-axis with a y value of \(y)")
//case let(x, y):
//    print("somewhere else at (\(x),\(y)")
//}
//

// MARK: Comand Cases
//
//let someCharacter: Character = "e"
//switch someCharacter {
//case "a", "e", "i", "o", "u":
//    print("\(someCharacter) is a vowel")
//case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
//     "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z":
//    print("\(someCharacter) is a consonant")
//default:
//    print("\(someCharacter) isn't a vowel or a consonant")
//}
// Prints "e is a vowel"

// MARK: Type safety and type inference
//
//let p = (8,0)
//switch p {
//case (let distance, 0),(0,let distance):
//    print("On an axis,\(distance)")
//default:
//    print("Not on an axis")
//}
//
// MARK: Continue

//let p = "great minds think alike"
//var p_out = ""
//let ch_remove: [Character] = ["a","e","i","o","u"," "]
//for i in p{
//    if ch_remove.contains(i){
//        continue
//    }
//    p_out.append(i)
//}
//print(p_out)


// MARK: Break in a Switch Statement

//
//let numberSymbol: Character = "三"  // Chinese symbol for the number 3
//var possibleIntegerValue: Int?
//switch numberSymbol {
//case "1", "١", "一", "๑":
//    possibleIntegerValue = 1
//case "2", "٢", "二", "๒":
//    possibleIntegerValue = 2
//case "3", "٣", "三", "๓":
//    possibleIntegerValue = 3
//case "4", "٤", "四", "๔":
//    possibleIntegerValue = 4
//default:
//    break
//}
//if let integerValue = possibleIntegerValue {
//    print("The integer value of \(numberSymbol) is \(integerValue).")
//} else {
//    print("An integer value couldn't be found for \(numberSymbol).")
//}
//// Prints "The integer value of 三 is 3."
//

// MARK: Fallthrough

//
//
//let integerToDescribe = 10
//var description = "The number \(integerToDescribe) is"
//switch integerToDescribe {
//case 2, 3, 5, 7, 11, 13, 17, 19:
//    description += " a prime number, and also"
//    fallthrough
//default:
//    description += " an not prime integer."
//}
//print(description)

// Prints "The number 5 is a prime number, and also an integer."


// MARK: Checking API avaiblity

//
//@available(macOS 10.12, *)
//struct ColorPreference {
//    var bestColor = "blue"
//}
//
//func chooseBestColor() -> String {
//    guard #available(macOS 10.12, *) else {
//        return "gray"
//    }
//    let colors = ColorPreference()
//    return colors.bestColor
//}

// MARK: Type annotations
//
//let str = "Hello how are you"
//let album: String = "wwww"
//let year: Int = 2022
//let bool: Bool = true
//let d: Double = 3.2
//print(str,album,year,bool,d)
//
// MARK: tuples
//
//var tuples = (first:"12",second:"23")
//print(tuples.0)
//print(tuples.second)
//

// MARK: Enumerations

//let result = "failure"
//let result2 = "failed"
//let result3 = "fail"
//enum Result {
//    case success
//    case failure
//}
//let res = Result.failure
//print(res)




// MARK: Function
//
//
//func printHelp(){
//    let messages = """
//Bangladesh is small country.
//"""
//    print(messages)
//
//}
//printHelp()


// MARK: Function use to parameter swap

//func swapint(_ a: inout Int, _ b: inout Int){
//    let temp = a
//    a = b
//    b = temp
//
//}
//var a = 3
//var b = 4
//swapint(&a, &b)
//print(a,b)
//
//
//func doubleInPlace(number: inout Int) {
//    number *= 2
//}
//var a = 10
//doubleInPlace(number: &a)
//print(a)


// MARK: Structures and classes
//
//struct Resulation {
//    var width = 0
//    var height = 0
//
//}
//
//class videoMode {
//    var resulation = Resulation()
//    var inter = false
//    var frame = 0.0
//    var name: String?
//}
//
//let someResulation = Resulation()
//let someVideoMode = videoMode()
//
//print("The width of someResulation is \(someResulation.width)")
//
//print(someVideoMode.resulation.width)


//
//struct marksheet {
//    var m1:Int
//    var m2 : Int
//    var m3 : Int
//
//    init(m1: Int, m2: Int, m3: Int) {
//        self.m1 = m1
//        self.m2 = m2
//        self.m3 = m3
//    }
//
//}
//
//var pass = marksheet(m1: 90, m2: 90, m3: 49)
//print(pass.m1,pass.m2,pass.m3)



// MARK: Cluseres

//
//let number = [5,7,3,2,4,1]
//
//func backward(_ a: Int, _ b: Int) -> Bool {
//    return a<b
//}
//print(number.sorted(by: backward(_:_:)))

//reversedNumber = number.sorted(by: { (a: Int, b:
//    Int) -> Bool in
//        return a>b
//})

//let digitNames = [0: "Zero", 1: "One", 2:"Two", 3: "Three",
//                  4:"Four",5:"Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10:"Ten"
//
//]
//
//let numbers = [16,58,510]
//let strings = numbers.map { (number) -> String in
//    var number = number
//    var output = ""
//    repeat {
//        output = digitNames[number % 10]! + output
//        number /= 10
//
//    } while number > 0
//            return (output)
//}
//
//print(strings)
//
//
//let a = "Bangladesh is a small country "
//
//
//print(a)


// MARK: Propertise

//
//
//struct FixedLengthRange {
//    var firstValue: Int
//    let length: Int
//}
//
//var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)
//// the range represents integer values 0, 1, and 2
//rangeOfThreeItems.firstValue = 6
//// the range now represents integer values 6, 7, and 8
//print(rangeOfThreeItems)
//
//

//
//class DataImporter {
//    /*
//    DataImporter is a class to import data from an external file.
//    The class is assumed to take a nontrivial amount of time to initialize.
//    */
//    var filename = "data.txt"
//    // the DataImporter class would provide data importing functionality here
//}
//
//class DataManager {
//    lazy var importer = DataImporter()
//    var data: [String] = []
//    // the DataManager class would provide data management functionality here
//}
//
//let manager = DataManager()
//manager.data.append("Some data")
//manager.data.append("Some more data")
//// the DataImporter instance for the importer property hasn't yet been created
//print(manager)
//print(DataManager())


// MARK: Computed Properties


//
//struct Point {
//    var x = 0.0, y = 0.0
//}
//struct Size {
//    var width = 0.0, height = 0.0
//}
//struct Rect {
//    var origin = Point()
//    var size = Size()
//    var center: Point {
//        get {
//            let centerX = origin.x + (size.width / 2)
//            let centerY = origin.y + (size.height / 2)
//            return Point(x: centerX, y: centerY)
//        }
//        set(newCenter) {
//            origin.x = newCenter.x - (size.width / 2)
//            origin.y = newCenter.y - (size.height / 2)
//        }
//    }
//}
//var square = Rect(origin: Point(x: 0.0, y: 0.0),
//                  size: Size(width: 10.0, height: 10.0))
//let initialSquareCenter = square.center
//// initialSquareCenter is at (5.0, 5.0)
//square.center = Point(x: 15.0, y: 15.0)
//print("square.origin is now at (\(square.origin.x), \(square.origin.y))")
//// Prints "square.origin is now at (10.0, 10.0)"

//
//let a = ""
//if a == ""{
//    print("true")
//}else {
//    print("false")
//}

// MARK: Querying and Setting Type Properties

//
//struct SomeStructure {
//    static var storedTypeProperty = "Some value."
//    static var computedTypeProperty: Int {
//        return 1
//    }
//}
//enum SomeEnumeration {
//    static var storedTypeProperty = "Some value."
//    static var computedTypeProperty: Int {
//        return 6
//    }
//}
//class SomeClass {
//    static var storedTypeProperty = "Some value."
//    static var computedTypeProperty: Int {
//        return 27
//    }
//    class var overrideableComputedTypeProperty: Int {
//        return 107
//    }
//}
//print(SomeStructure.storedTypeProperty)
//// Prints "Some value."
//SomeStructure.storedTypeProperty = "Another value."
//print(SomeStructure.storedTypeProperty)
//// Prints "Another value."
//print(SomeEnumeration.computedTypeProperty)
//// Prints "6"
//print(SomeClass.computedTypeProperty)
//// Prints "27"
///
///
//  MARK: Two system


//struct SomeStructure {
//    static var stp = "Some value."
//    static var ctp : Int {
//        return 1
//    }
//}
//enum SomeEnumeration {
//    static var stp = "Some value."
//    static var ctp : Int {
//        return 6
//    }
//}
//class SomeClass {
//    static var stp = "Some value."
//    static var ctp : Int {
//        return 27
//    }
//    class var overridectp: Int {
//        return 107
//    }
//}
//
//print(SomeStructure.stp)
//
//SomeStructure.stp = "Another value."
//
//print(SomeStructure.stp)  // MARK: Querying and setting type propeerties - someStructure.stp
//print(SomeEnumeration.ctp) // MARK: Querying and setting type propeerties
//print(SomeClass.ctp)  // MARK: Querying and setting type propeerties
//print(SomeClass.overridectp) // MARK: Querying and setting type propeerties



// MARK: Subscript Declaration


struct subexample {
    let dcr: Int
    subscript(index: Int) -> Int {
        return dcr / index
    }
}

let division = subexample(dcr: 100)
print(division[9])

print(division[3])


print("hello world")






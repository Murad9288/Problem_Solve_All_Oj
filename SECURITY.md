# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.


// conform Employee to Equatable
struct Employee: Equatable {
    
    var name: String
    var salary: Int
}

// initialize two objects with different property values 
let obj1 = Employee(name: "Sabby", salary: 40000)
let obj2 = Employee(name: "Sabby", salary: 40000)
let obj3 = Employee(name: "Cathy", salary: 30000)

// compare obj1 and obj2
if obj1 == obj2 {
    print("obj1 and obj2 are equal")
}
else {
    print("obj1 and obj2 are not equal")
}

// compare obj1 and obj3
if obj1 == obj3 {
    print("obj1 and obj3 are equal")
}
else {
    print("obj1 and obj3 are not equal")
}

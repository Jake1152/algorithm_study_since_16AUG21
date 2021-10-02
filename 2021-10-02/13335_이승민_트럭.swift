import Foundation

let data = readLine()!.components(separatedBy: " ").map { Int(String($0))! }
let (n, w, l) = (data[0], data[1], data[2])
let arr = readLine()!.components(separatedBy: " ").map { Int(String($0))! }
var q = [[arr[0], 1]]
var time = 1
var sum = 0
var index = 0

while !q.isEmpty {
    if index < arr.count && q.count < w && sum + arr[index] <= l {
        q.append([arr[index], time])
        sum += arr[index]
        index += 1
    }
    
    if q[0][1] + w <= time {
        if index < arr.count {
            sum -= q.removeFirst()[0]
            q.append([arr[index], time])
            sum += arr[index]
            index += 1
        }
        else {
            q.removeFirst()
        }
    }
    time += 1
}
print(time)


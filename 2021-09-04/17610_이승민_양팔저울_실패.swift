import Foundation

let input = Int(readLine()!)!
let array = readLine()!.components(separatedBy: " ").map{Int(String($0))!}
let ansLen = array.reduce(0, +)
var ansSet = Set<Int>(Array(Range(1...ansLen)))

for k in 0..<array.count { // 개수
    for i in 0..<array.count { // 기준 인덱스
        if i + k > array.count { // 합
            break
        }
        var sum = array[i]
        for j in i..<i+k {
            if ansSet.contains(sum) {
                ansSet.remove(sum)
            }
            sum += array[j]
        }
    }

}
print(ansSet)
print(ansSet.count)


import Foundation

// green: 1, blue: 2, red: 3, black: 4, white: 5
let n = Int(readLine()!)!
var dp = Array(repeating: Array(repeating: Array(repeating: Array(repeating: Array(repeating: Array(repeating: Array(repeating: -1, count: 6), count: 6), count: 11), count: 11), count: 11), count: 11), count: 11)
var bead = [0, 0, 0, 0, 0]
var ans = 0


for i in 0..<n {
    bead[i] = Int(readLine()!)!
}

func dfs(_ green: Int, _ blue: Int, _ red: Int, _ black: Int, _ white: Int, _ pastColor: Int, _ pastPastColor: Int) {
    if green < 0 || blue < 0 || red < 0 || black < 0 || white < 0 {
        return
    }

    if dp[green][blue][red][black][white][pastColor][pastPastColor] != -1 {
        return
    }

    dp[green][blue][red][black][white][pastColor][pastPastColor] = 0
    
    if green == 0 && blue == 0 && red == 0 && black == 0 && white == 0 {
        ans += 1
        return
    }
    
    if pastColor != 1 && pastPastColor != 1 { dfs(green - 1, blue, red, black, white, 1, pastColor) }
    if pastColor != 2 && pastPastColor != 2 { dfs(green, blue - 1, red, black, white, 2, pastColor) }
    if pastColor != 3 && pastPastColor != 3 { dfs(green, blue, red - 1, black, white, 3, pastColor) }
    if pastColor != 4 && pastPastColor != 4 { dfs(green, blue, red, black - 1, white, 4, pastColor) }
    if pastColor != 5 && pastPastColor != 5 { dfs(green, blue, red, black, white - 1, 5, pastColor) }
}

dfs(bead[0], bead[1], bead[2] ,bead[3], bead[4], 0, 0)
print(ans)

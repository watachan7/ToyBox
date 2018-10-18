package main
// https://qiita.com/135yshr/items/77613fb8366998f0ee52

import (
    "fmt"
)

func main() {
    fmt.Println("1+1=", 1+1)       // 1. 足し算した結果
    fmt.Println("1+1=", add(1, 1)) // 2. ２つの引数を取るメソッド
    add1 := cadd(1)
    fmt.Println("1+1=", add1(1))   // 3. カリー化したメソッド（１）
    fmt.Println("1+1=", cadd(1)(1)) // 4. カリー化したメソッド（２）
}

func add(x, y int) int {
    return x + y
}

func cadd(x int) func(int) int {
    return func(y int) int { return x + y }
}
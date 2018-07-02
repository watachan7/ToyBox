sum = -> *ns { ns.reduce :+ }  # sum は可変引数をとる

p sum.()           #=> nil
p sum.(1)          #=> 1
p sum.(1,2)        #=> 3
p sum.(1,2,3)      #=> 6
p sum.(1,2,3,4)    #=> 10
p sum.(*1..10)     #=> 55
p sum.(*"a".."z")  #=> "abcdefghijklmnopqrstuvwxyz" (この例は、お遊び)

sum1     = sum.curry(3)[1]         # curry の引数で 3 を指定
sum1_2   = sum1.(2)
sum1_2_3 = sum1_2.(3)

                  # 結果は、元のProcが3引数だった場合と同じ
p sum1.(2,3)      #=> 6
p sum1_2.(3)      #=> 6
p sum1_2_3        #=> 6
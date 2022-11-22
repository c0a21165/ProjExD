import random
import datetime
date1=7
date2=3
mdate=9
m=0
def kaitou(x):
    while m>9:
        x=set()
        for i in range(data1):
            x.add(chr(random.randint(65,90)))
        k=set()
        for j in range(data2):
            k.add(x.pop())
        print("対象文字：")
        print(f"{x}")
        print("欠損文字")
        print(f"{k}")

        st = datetime.datetime.now()
        print(len(k))
        ans = int(input("欠損文字はいくつあるでしょうか："))
        print("2")
        
        if ans == len(k):
            print("正解です。それでは、具体的に欠損文字を１つずつ入力してください。")
                    
        else:
            print(f"不正解です。欠損文字は{len(k)}個です。欠損文字を推測して１つずつ入力してください")
                
        ans2 = input("一つ目の文字を入力してください")
        ans3 = input("二つ目の文字を入力してください")

        if ans in x:
            print("正解！！！")
            break
        else:
            print("不正解です。またチャレンジしてください")
        ed = datetime.datetime.now()


if __name__=="__main__":
    x=0
    kaitou(x)

    
    
    
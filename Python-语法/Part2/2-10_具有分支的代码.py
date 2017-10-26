# 练习：在 which_prize() 中使用对象的真值
# 运用所学的关于真值的内容，重写以前的 which_prize() 函数。 以根据积分设置变量 prize = None，更改 prize 编写函数，然后根据是否获得 prize 使用另一个条件表达式返回消息。这将避免代码 return 部分多次重复。
def which_prize(points):
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafe-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."

print(which_prize(164))

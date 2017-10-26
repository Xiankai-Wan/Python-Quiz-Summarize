# 练习：获得哪种奖励？
# 在本次练习中，运行一个名为 which_prize() 的函数，该函数用于通知参赛者他们在游戏中根据积分所赢得的奖励。
# which_prize() 的输入将是积分数（整数）。函数 which_prize() 应该返回文本"恭喜！你赢得了 [奖品名称]!"，如果他们赢得了奖品，还应包括奖品名称，如果没有获奖，文本内容应为"哦，亲爱的，这次没有奖品"。和往常一样，测试函数，检查一下它是否能正常执行
def which_prize(point):
    if 0 < point <=50:
        return "Congratulations! You have won a wooden rabbit!"
    elif 50 < point <= 150:
        return "Oh dear, no prize this time."
    elif 150 < point <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"

# 练习：创建帮助函数 sum_of_middle_three
# 现在是时候完成 sum_of_middle_three 这个函数了。确保使用打印语句测试该函数。可以根据之前编写的框架开始。你可以使用 max() 和 min() 查找最大值和最小值。max() 返回一组数字中的最大值，min() 返回最小值。例如：
# max(1,2,3,4) #returns 4
# min(1,2,3,4) #returns 1
def sum_of_middle_three(score1,score2,score3,score4,score5):
    return (score1 + score2 + score3 + score4 + score5)-min(score1,score2,score3,score4,score5)-max(score1,score2,score3,score4,score5)

print(sum_of_middle_three(1,2,3,4,5))

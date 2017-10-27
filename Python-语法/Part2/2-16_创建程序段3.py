# 练习：创建帮助函数 score_to_rating_string
# 完成最后一个帮助函数 score_to_rating_string 的时间！下表指导大家如何将得分映射到评分。
#
# Average Score	Rating
# 0 <= score < 1	Terrible
# 1 <= score < 2	Bad
# 2 <= score < 3	OK
# 3 <= score < 4	Good
# 4 <= score <= 5	Excellent
# 需要单独检查和处理每个案例。但不要忘记使用一些打印语句来测试你的函数。可以回顾一下之前编写的框架。

def score_to_rating_string(score):
    rating = "Excellent"
    if 0 <= score < 1:
        rating = "Terrible"
    elif 1 <= score < 2:
        rating = "Bad"
    elif 2 <= score < 3:
        rating = "OK"
    elif 3 <= score < 4:
        rating = "Good"
    else:
        rating = rating

    return rating

print(score_to_rating_string(4))

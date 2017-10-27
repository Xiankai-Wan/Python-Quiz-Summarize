# 练习：组合 scores_to_rating 函数
# 先前所有帮助函数都构建得不错！现在可以将所有这些函数组合到一起，使其成为一个整体进行运行。
#
# 在该编程练习中，将编写的每个帮助函数放入编码窗口，然后在编写函数 scores_to_rating 时使用。请注意，此函数以五个分数（可能不是数字）开始，取中间三个分数的平均值，并将该平均值转换为返回的书面评分。
#
# 需要确保将一个函数的输出正确传递到 scores_to_rating 函数体的下一个输入。一次添加一个，同时还需添加有用的注释，而且调用 print 进进行测试，将有助于控制错误！

def convert_to_numeric(score):
    """Covert the score to a float
    """
    return float(score)

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum

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

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    score11 = convert_to_numeric(score1)
    score22 = convert_to_numeric(score2)
    score33 = convert_to_numeric(score3)
    score44 = convert_to_numeric(score4)
    score55 = convert_to_numeric(score5)

    average_score = sum_of_middle_three(score11,score22,score33,score44,score55)/3

    rating = score_to_rating_string(average_score)

    return rating

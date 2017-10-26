# 练习：搭建帮助函数的框架
# 在本练习中，为 scores_to_rating 所需的帮助函数搭建框架。框架中应包括定义行，一个描述函数的 docstring 和一个返回语句。此阶段，没有必要实际加入函数中所含的任何代码。如果不构建帮助函数，解决方案就无法运行。 现在没问题了！
#
# 需要搭建框架的函数：
#
# 第 1 步：convert_to_numeric
# 第 2、3 步：sum_of_middle_three
# 第 4 步：score_to_rating_string
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score =
        sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

def convert_to_numeric(score):
    """Turn the score to number
    """
    number = int(score)
    return number

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """Return the sum of middle three
    """
    sum_of_middle_three = sum(score1,score2,score3,score4,score5) - max(score1,score2,score3,score4,score5) - min(score1,score2,score3,score4,score5)
    return sum_of_middle_three

def score_to_rating_string(score):
    """Turn the score to string
    """
    rating = str(score)
    return rating

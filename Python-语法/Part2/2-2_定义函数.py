# 练习：人口密度函数
# 编写一个名为 population_density 的函数，该函数有两个参数，population 和 land_area（以平方公里计），可以返回一个根据这些值计算出的人口密度。下面有两个测试案例，你可以使用这两个案例验证自己的函数是否可用。编写函数后，使用测试答案按钮测试代码。
# todo: define a function named `population_density` that takes two arguments,
# `population` and `land_area` (in square kilometres), and returns a population
# density calculated from those values.

# Your code goes here!
def population_density(population,land_area):
    return population/land_area



# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

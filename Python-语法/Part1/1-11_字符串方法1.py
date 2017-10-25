# 练习：元音计数
# 使用 count 方法来确定字符串 prophecy 中有多少个元音。将此计数存储在 vowel_count 变量中。
#
# 注意：元音是 a、e、i、o 和 u。
#
# 提示：可能需要多次调用 count 方法，并且多次添加到 vowel_count 中。
#
# 如果出现问题，请查看 solution.py 选项卡。

prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0

# TODO: set the value of vowel_count to be the number of vowels in prophecy
prophecy = prophecy.lower()
vowel_count_a = prophecy.count('a')
vowel_count_e = prophecy.count('e')
vowel_count_i = prophecy.count('i')
vowel_count_o = prophecy.count('o')
vowel_count_u = prophecy.count('u')
vowel_count = vowel_count_a + vowel_count_e + vowel_count_i + vowel_count_o + vowel_count_u

# Print the final count
print(vowel_count)

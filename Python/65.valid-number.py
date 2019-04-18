#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (13.92%)
# Total Accepted:    119.8K
# Total Submissions: 860.6K
# Testcase Example:  '"0"'
#
# Validate if a given string can be interpreted as a decimal number.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one. However, here is a
# list of characters that can be in a valid decimal number:
#
#
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
#
#
# Of course, the context of these characters also matters in the input.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
#
#
class Solution:
    # Valid Numbers: 符号 + 浮点数 + e + 符号 + 整数
    """
    首先应该明确合法的数字有哪些:
    整数, 例如 "122", "114"
    浮点数, 例如 "1.2", "2.", ".5", "1e10", "1E10"
    上面两种数加上符号, 即 "+" 或 "-"
    "2.", ".5" 这两种形式可能让你有点迷惑, 你可以试一试, 在大多数编程语言中它们都是合法的字面量.

    为了方便, 我们可以先处理掉首尾的空白字符. 然后再判断第一个是否符号, 如果是也过滤掉.

    然后, 剩下的字符串就只能包含 0-9, ., e/E 这三类字符了, 如果含有这三类之外的, 直接返回 false 即可. 然后根据以下原则判断即可:
        1. 小数点和 e/E 都至多只能出现 1 次
        2. 如果含有小数点, 则小数点前后至少有一个数字, 一个孤立的小数点是非法的.
        3. 如果含有 e/E, 则它的前后必须有数字.
    """
    # Your runtime beats 100 % of python3 submissions
    def isNumber(self, s: str) -> bool:
        if not str or len(s) == 0:
            return False
        space = " \t"
        l, r = 0, len(s) - 1
        while l <= r and s[l] in space:
            l += 1
        while l <= r and s[r] in space:
            r -= 1
        if l > r:
            return False

        if s[l] in "+-":
            l += 1
        if l > r:
            return False

        dot, ex, num = False, False, False
        for i in range(l, r + 1):
            curr = s[i]
            if curr in "1234567890":
                num = True
                continue

            if curr == ".":
                if ex or dot:
                    return False
                dot = True
            elif curr in "Ee":
                if ex or num == False:
                    return False
                ex = True
                num = False
            elif curr in "+-":
                if s[i - 1] not in "Ee":
                    return False
            else:
                return False
        return num


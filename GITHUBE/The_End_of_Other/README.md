For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of 
words, such that one word is the end of another (a suffix of another). For example: {"hi",
"hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
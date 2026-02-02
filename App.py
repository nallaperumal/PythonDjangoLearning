import re #regular expression

patternStartsWitha = "^[aA]"
test_string = "Apple"
banana = "banana"
result = re.match(patternStartsWitha, test_string)

if result:
    print("search succeeded")
else:
    print("failed")

testStr = """My number is 1231233
                my frinds number is 789799 """
onlyNumbers =  "\d+"
match = re.findall(onlyNumbers, testStr)
# print(match)

pattern = "ab+"
sample_str = "ababbaabbb"
all = re.findall(pattern, sample_str)
print(all)
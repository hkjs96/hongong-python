# 염기서열 = 'ctacaatgtcagtatacccattgcattagccgg'
염기서열 = input("염기 서열을 입력해주세요: ")

dictionary = {
    "a": 0,
    "t": 0,
    "c": 0,
    "g": 0
}

for i in range(len(염기서열)):
    dictionary[염기서열[i]] += 1

for key, value in dictionary.items() :
    print("{}의 개수: {}".format(key, value))


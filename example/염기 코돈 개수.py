# 염기서열 = 'ctacaatgtcagtatacccattgcattagccgg'
염기서열 = 'ctacaatgtcagtatacccattgcattagccgggg'
# 염기서열 = input("염기 서열을 입력해주세요: ")
dictionary = {}

if len(염기서열) % 3 != 0:
    print(염기서열)
else:
    for i in range(0, len(염기서열), 3):
        코돈 = 염기서열[i : i + 3]
        if dictionary.get(코돈) == None :
            dictionary[코돈] = 1
        elif dictionary.get(코돈) != None :
            dictionary[코돈] += 1

    print(dictionary)

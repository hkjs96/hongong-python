from multiprocessing.dummy import Array


리스트 = [1,2,[3,4],5,[6,7],[8,9]]

리스트_평탄화 = []

for element in 리스트:
    if type(element) == list:
        for i in element:
            리스트_평탄화.append(i)
    else: 
        리스트_평탄화.append(element)

print(f'{리스트}를 평탄화하면 \n{리스트_평탄화}입니다.')
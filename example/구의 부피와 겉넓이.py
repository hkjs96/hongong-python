# 구의 반지름 입력 받기
r = input("구의 반지름을 입력해주세요: ")

# 구의 부피
volume = "= 구의 부피는 {}입니다.".format(4*3.141592*int(r)**3/3)
print(volume)

# 구의 겉넓이
width = 4*3.141592*int(r)**2
print("= 구의 겉넓이는 "+str(width)+"입니다.")
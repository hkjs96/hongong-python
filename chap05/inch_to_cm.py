# 숫자 입력받기
raw_inch = input("Inch를 입력하세요!> ")

# 숫자 변환하기
## 1. 문자를 숫자로 변환하기
inch = int(raw_inch)

## 2. 인치를 센티미터로 변환하기 (1:2.54)
cm = 2.54 * inch

# 숫자 출력하기 
print(cm)
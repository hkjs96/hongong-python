import datetime

# 입력
input_value = input("입력: ")

# 출력
if "안녕" in input_value:
    print("안녕하세요.")
elif "몇 시".strip() in input_value.strip():
    now = datetime.datetime.now()
    print("지금은 {}시입니다.".format(now.hour))
else:
    print(input_value)



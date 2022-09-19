num_list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dictionary = {}

num_list.sort()
print(type(num_list));

for i in range(len(num_list)):
    # if (dictionary["{}".format(num_list[i])]) in num_list:
    if dictionary.get("{}".format(num_list[i])) in num_list:
        continue
    else:
        dictionary["{}".format(num_list[i])] = num_list.count(num_list[i])

print((
    "{}에서 \n"
    "사용된 숫자의 종류는 {}개입니다. \n"
    "참고: {}"
    ).format(num_list, dictionary.__len__(), dictionary))
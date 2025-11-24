import sys
sys.stdin = open("input.txt", "r")

# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

while True :
    n = int(input())
    if n == -1:
        break
    divisor = 0
    divisor_box = list()

    temp_sum = 0

    while divisor <= n/2:
        divisor += 1
        if n % divisor:
            continue
        else:
            temp_sum += divisor
            divisor_box.append(divisor)

    result_right = str()

    if temp_sum == n:
        divisor_box = list(map(str, divisor_box))
        for i in range(len(divisor_box)):
            result_right = result_right + divisor_box[i]
            if i < len(divisor_box) - 1:
                result_right = result_right + ' + '
            result_right = ''.join(result_right)
        print(f'{n} = {result_right}')
        continue

    else:
        print(f'{n} is NOT perfect.')
        continue
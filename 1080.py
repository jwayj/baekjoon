# 입력 받기
n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]


# 3x3 부분 행렬 뒤집기 함수
def flip_3x3(matrix, x, y):
    for i in range(3):
        for j in range(3):
            matrix[x + i][y + j] = 1 - matrix[x + i][y + j]


# A와 B가 같아질 수 있는지 확인하는 함수
def can_transform():
    # 연산 횟수
    count = 0

    # A에서 B로 변환하기 위해 3x3 뒤집기 적용
    for i in range(n - 2):
        for j in range(m - 2):
            # A와 B가 다른 경우 3x3 뒤집기 연산을 적용
            if a[i][j] != b[i][j]:
                flip_3x3(a, i, j)
                count += 1

    # 모든 연산이 끝난 후 A와 B가 같은지 확인
    if a == b:
        return count
    else:
        return -1


# 결과 출력
print(can_transform())

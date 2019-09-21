SIZE = 7
# [[0, 0, 0, 0, 0, 0, 0]]
array = [[0] * 7]
# 创建一个长度为SIZE * SIZE 的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]
# 该orient代表绕圈的方向
# 其中0代表向下，1代表向右，2代表向上，3代表向左
orient = 0
# 控制将1~SIZE * SIZE 的数值填入二维列表中
# 其中j控制行索引，k 控制列索引
j = 0
k = 0
# 填入数值
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    # 决定转向
    if j + k == SIZE - 1:
        # 左下角
        if j > k:
            orient = 1
        else:
            orient = 3
    elif (j == k) and (k >= SIZE/2):
        orient = 2
    # 这里容易犯的一个错 j k 中要选大的，这里k较大。所以是 k <SIZE/2  [j <= SIZE/2 - 1]
    elif (j == k - 1) and (k <= SIZE/2):
        orient = 0
    # 根据转向决定位置
    if orient == 0:
        j += 1
    elif orient == 1:
        k += 1
    elif orient == 2:
        j -= 1
    elif orient == 3:
        k -= 1

# 打印数值
for i in range(SIZE):
    for j in range(SIZE):
        print("%02s" % array[i][j], end=" ")
    # 换行
    print()


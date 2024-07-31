

# 这个函数主要是寻找中点左边最大值，中点右边最大值，然后将两个值相加
def find_cross_subarray(A,low , mid, high):
    infinity = -float('inf')
    left_sum = infinity
    sum = 0
    max_left = 0
    for i  in range(mid ,low , -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = infinity
    sum = 0
    max_right = 0
    for j in range(mid+1 , high , 1):
        sum = sum +A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right , left_sum + right_sum)



if __name__ == '__main__':
    A = [-1, 2, 4, 6, -2, 3, 1, 0]
    low = 0
    mid = 3
    high = 7
    lows, highs, sums = find_cross_subarray(A , low, mid, high)
    print(lows,highs,sums)

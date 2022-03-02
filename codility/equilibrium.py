def equilibrium(A):
    sum_left = 0
    sum_right = 0
    min = 0
    p_min = 0
    p_index_minus_one_value = 0

    for number in A:
        sum_right += number

    min = sum_right

    for i in range(0 , len(A) ):
        if ( i > 0 ):
            p_index_minus_one_value = A[i-1]
            sum_left += p_index_minus_one_value
            sum_right -= p_index_minus_one_value
            if ( abs(sum_left-sum_right) < min):
                min = abs(sum_left-sum_right)
                p_min = i
    return p_min

print(equilibrium([3,1,2,4,3]))
print(equilibrium([]))
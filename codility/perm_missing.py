def permMissing(A):
    actual_sum = 0
    for number in A:
        actual_sum += number
    max_number = len(A) + 1
    expected_sum = (max_number*(max_number+1)//2)
    return expected_sum - actual_sum

print(permMissing([]))
print(permMissing([1,2,3,5]))

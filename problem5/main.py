def pair_sum(arr, target):
    left, right = 0, len(arr) -1 # mendefine kanan dan kiri dari sebuah array

    while left < right:
        current_sum = arr[left]+arr[right] 
        if current_sum == target:
            return [left,right] #tampilkan pair yang jumlahnya sama dengan target
        elif current_sum < target : 
            left += 1 #jika hasil kurang dari target, geser ke kanan
        else : 
            right -= 1 #jika hasil lebih dari target, geser ke kiri
    return []
    

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]
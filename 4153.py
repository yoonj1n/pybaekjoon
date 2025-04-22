while True:
    nums = list(map(int, input().split()))
    if(nums[0]==0 and nums[1]==0 and nums[2]==0): break
    max_len = max(nums)
    nums.remove(max_len)
    if nums[0]**2 + nums[1]**2 == max_len**2:
        print('right')
    else:
        print('wrong')
    
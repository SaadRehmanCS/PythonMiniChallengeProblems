def consecutiveNums():
    nums = []
    for i in range(100):
        inputNum = eval(input("Enter a number:\nEnter 0 to quit loop "))
        if inputNum == 0:
            break
        nums.append(inputNum)

    countingList = []
    for k in range(len(nums)):
        counter = 0
        for j in range(len(nums)):
            if nums[k] == nums[j]:
                counter += 1
        if nums[k] not in countingList:
            print(str(nums[k]) + " is repeated " + str(counter) + " times")
            countingList.append(nums[k])


consecutiveNums()

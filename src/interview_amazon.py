def organizeNum(num):
    storage = {}
    c_i = 0 # counter for the first loop to keep track of list, num

    for i in num:
        count = 0 #counter for the same number
        c_j = 0 #counter for the second loop to keep track of list, num
       
        if storage.has_key(num[c_i])== False:
            for j in num:
                if num[c_i] == num[c_j]:
                    count = count + 1         
                c_j = c_j + 1
            storage[num[c_i]] = count
        c_i = c_i + 1
    
    return storage;

print organizeNum([1,3,4,5,4,3,2,1,5])
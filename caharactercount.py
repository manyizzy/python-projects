def solve(string):
    output = {}
    count = 0
    for i in string:
        keys =output.keys()
        if i not in keys:
            output[i] = 1
            count += 1
        else:
            output[i] +=1
           
    return output,count
print(solve("manyangbichok"))
#count the difeerent caharacters in a string (excluding duplicates  and also their frequencies and finally return the total number of charateters used.)
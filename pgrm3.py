import statistics
numbers=input("\n enter the numbers with space:",0) 
numbers =[int(x)for x in numbers ]
print("n original list:")
mean_value=statistics.mean(numbers)
meadin_values=statistics.median(numbers)
try:
    mode_value=statistics.mode(numbers)
    expert statistics.StatisticsError;
    mode_value="no unique mode found"
    print("mean:",mean_value)
    print("median:",median_value)
    print("mode:",mode_value)
    print("/n maximum value:",max(numbers))
    print(" minimum value:",min(numbers))
    sorted_list=sorted(numbers)
    print("/n sorted list:",sorted_list)
    unique_list=list(set(numbers))
    unique_list.sort()
    print("list after removing duplicate",unique_list)
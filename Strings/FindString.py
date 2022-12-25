def count_substring(string, sub_string):
    lenghtofsubstring = len(sub_string)
    traverselimit=(len(string)-lenghtofsubstring)
    count=i=0
    while(i<len(string)):
        if sub_string == string[i:lenghtofsubstring+i]:
            count=count+1
        i=i+1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
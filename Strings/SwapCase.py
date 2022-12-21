def swap_case(s):
    str=list(s)
    for i in range(len(str)):
        if(str[i].isupper()):
            str[i]=str[i].lower()
        else:
            str[i]=str[i].upper()
            
    return "".join(str)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
def swap_case(s):
    arr=list(s)
    for i in arr:
        if(i.isupper()):
            i.replace(i,i.lower())
            print(i)
    return " ".join(arr)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
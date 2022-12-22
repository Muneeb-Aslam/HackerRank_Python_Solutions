def wrap(string, max_width):
    str=list(string)
    j=1
    for index,i in enumerate(str):
        if (index+1)%max_width==0:
            str.insert(index+j,"\n")
            j=j+1
    return "".join(str)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
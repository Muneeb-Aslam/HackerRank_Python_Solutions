if __name__ == '__main__':
    N = int(input())
    commands = [input() for _ in range(N)]
    list=[]
    for i in commands:
        cmds,*args=i.split(" ")
        if(cmds=="print"):
            print(list)
        else:
            opearations = f"list.{cmds}({','.join(args)})"
            exec(opearations)
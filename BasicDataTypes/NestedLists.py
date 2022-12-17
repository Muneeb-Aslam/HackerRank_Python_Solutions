if __name__ == '__main__':
    stds=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        stds.append([name,score])
    scores=set(scores)
    scores=list(scores)
    scores.sort()
    results=[ i for i in stds if i[1]==scores[1]]
    results.sort()
    for i in results:
        print(i[0])
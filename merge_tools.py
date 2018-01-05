def merge_the_tools(x, k):
    t = int(len(x)/k)
    for i in range(t):
        temp = x[i*k:(k*i)+k]
        new = []
        for i in temp:
            if i not in new:
                new.append(i)
        print(''.join(new))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
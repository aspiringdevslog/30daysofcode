if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max = max(arr)
    arr.sort()
    # arr.reverse()
    runnerup = -1
    
    for item in arr:
        if item < max and runnerup != max:
            runnerup = item
            
    print(runnerup)
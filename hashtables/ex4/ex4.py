def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}



    # Your code here

    for num in a:
        if abs(num) in cache:
            cache[abs(num)] += 1
        else:
            cache[abs(num)] = 1

    for k, v in cache.items():
        if v > 1:
            result.append(k)
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))




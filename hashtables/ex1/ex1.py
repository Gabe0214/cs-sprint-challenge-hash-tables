def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}


    # return None
    # result = None
    # for num in weights:
    #     if limit - num in cache:
    #         result = [num, cache[limit - num]]
    #         return result
    #     cache[num] = num

    for num in range(length):
      if limit - weights[num] in cache:
          return [num, cache[limit - weights[num]]]
      else:
          cache[weights[num]] = num
    return None





# t1= [4,4]
# t2 = len(t1)
# t3 = 8
#
# answers = get_indices_of_item_weights(t1,t2,t3)
#
# print(answers[0])
def min_rewards(scores):
  rewards = [1 for _ in range(len(scores))]
  
  for i in range(1, len(scores)):
    j = i
    k = i
    while j > 0 and scores[j - 1] > scores[j]:
      print("first", scores[j - 1], scores[j])
      rewards[j - 1] = max(rewards[j - 1], rewards[j] + 1)
      j -= 1
  
    while k < len(scores) - 1 and scores[k] < scores[k + 1]:
      print("second", scores[k], scores[k + 1])
      rewards[k + 1] = max(rewards[k], rewards[k + 1] + 1)
      k += 1
  
  return sum(rewards)

scores = [8,4,2,1,3,6,7,9,5]
print(min_rewards(scores))
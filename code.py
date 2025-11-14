votesDictionary = []
candidateVotes = {}
ifContinue = 'yes'
while ifContinue == 'yes':
  votesDictionary.append(input("What word do you want to add to your list?: "))
  ifContinue = input("Do you want to add anymore words to the list?(yes/no): ")
for key in votesDictionary:
    candidateVotes[key] = 0
def getWinner(x):
  for vote in votesDictionary:
      candidateVotes[vote] += 1
  return candidateVotes

print(getWinner(votesDictionary))

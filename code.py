votesDictionary = []
candidateVotes = {}
for key in votesDictionary:
    candidateVotes[key] = 0
def getWinner(x):
  for vote in votesDictionary:
      candidateVotes[vote] += 1
      print(candidateVotes)
  return candidateVotes

print(getWinner(votesDictionary))

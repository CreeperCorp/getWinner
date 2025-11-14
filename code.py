votesDictionary = ['hello', 'good', 'goodbye', 'hello', 'hello', 'yes', 'good', 'good']
candidateVotes = dict.fromkeys(votesDictionary)
print(candidateVotes)
for key in candidateVotes:
    candidateVotes[key] = 0
print(candidateVotes)
def getWinner(x):
  for vote in candidateVotes:
    print(candidateVotes)
    if vote in candidateVotes:
        candidateVotes[vote] += 1
    return candidateVotes

print(getWinner(candidateVotes))

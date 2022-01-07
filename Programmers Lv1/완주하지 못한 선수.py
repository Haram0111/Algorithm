participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
for i in completion:
    if i in participant:
        participant.remove(i)
print(participant)
#효율성테스트 미통과
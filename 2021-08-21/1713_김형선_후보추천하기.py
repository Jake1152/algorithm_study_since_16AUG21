N = int(input())
_ = input()
votes = list(map(int, input().split()))
photos = []
for vote in votes:
    min_idx = -1
    is_found = False
    for j in range(min(N, len(photos))):
        if (min_idx == -1 or photos[min_idx][1] > photos[j][1]):
            min_idx = j
        if vote == photos[j][0]:
            photos[j][1] += 1
            is_found = True
    if is_found:
        continue
    if len(photos) >= N:
        photos.pop(min_idx)
    photos.append([vote, 1])

photos.sort()
for photo in photos[:-1]:
    print(photo[0], end=" ")
print(photos[-1][0])

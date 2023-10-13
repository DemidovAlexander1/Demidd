n, m, q = map(int, input().split())
watched_episodes = set()

for _ in range(q):
    season, episode = map(int, input().split())
    watched_episodes.add((season, episode))

missing_episodes = []

for season in range(1, n + 1):
    for episode in range(1, m + 1):
        if (season, episode) not in watched_episodes:
            missing_episodes.append((season, episode))

print(len(missing_episodes))
for episode in missing_episodes:
    print(episode[1], episode[0])

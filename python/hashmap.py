hash_map = [[] for x in range(255)]
key = hash('06770') % len(hash_map)
print(key)

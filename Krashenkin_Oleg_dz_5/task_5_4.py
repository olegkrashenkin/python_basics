src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[i + 1] for i in enumerate(src) if src[-1] != src[i] and src[i + 1] > src[i])  # Или len, как лучше?
print(*result)

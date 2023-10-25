from string import ascii_lowercase as LOWERS

dict = { key:n for key, n in zip(LOWERS, range(1, 27)) }










dict = {key:c**2 for key, c in zip('ABCDE', range(1, 6))}
print(dict)
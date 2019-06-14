import time

start_time = time.time()

with open('names_1.txt', 'r') as f1, open('names_2.txt', 'r') as f2:
    duplicates = []
    hash = {}
    for line in f1:
        hash[line] = True
    for line in f2:
        if line in hash:
            duplicates.append(line.strip())

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

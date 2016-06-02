with open('file.txt', 'r') as f:
    for current_line in f:
        #current_line = f.readline()
        words = current_line.split()
        for word in words:
            print(word)
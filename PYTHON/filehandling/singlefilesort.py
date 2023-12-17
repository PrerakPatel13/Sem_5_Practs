def sort_and_write(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'w') as f2:
        lines = f1.readlines()
        lines.sort() 
        for line in lines:
            f2.write(line.strip() + '\n')

sort_and_write('file1.txt', 'file2.txt')

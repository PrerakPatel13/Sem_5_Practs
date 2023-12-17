def merge_files(file1, file2, file3):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
        lines1 = list(map(str.strip, f1.readlines()))
        lines2 = list(map(str.strip, f2.readlines()))

        merged_lines = sorted(lines1 + lines2, key=int)
        merged_lines_with_newline = map(lambda x: x + '\n', merged_lines)

        f3.writelines(merged_lines_with_newline)

merge_files('file1.txt', 'file2.txt', 'file3.txt')

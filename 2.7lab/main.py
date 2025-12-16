def merge_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as f1, \
         open(file2_path, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    result_lines = []
    for i in range(len(lines1)):
        line1 = lines1[i].rstrip('\n')
        if i < len(lines2):
            line2 = lines2[i].rstrip('\n')
            result_lines.append(line1 + line2)
        else:
            result_lines.append(line1)
    
    with open(file1_path, 'w', encoding='utf-8') as f1:
        f1.write('\n'.join(result_lines) + '\n')

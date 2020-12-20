import os

file_list = sorted(list(
    filter(lambda name: '.py' in name and '-' in name, os.listdir())))

with open('README.md', 'w') as f:
    f.write('# LeetCode Solutions\n\n')
    f.write('Welcome to the repository of my LeetCode solutions\n\n')
    f.write('## Completed Problems\n\n')
    f.write('| Problem | Language |\n')
    f.write('| --- | --- |\n')
    for qn in file_list:
        file = ' '.join(
            list(map(lambda name: name[0].upper() + name[1:], qn.split('-'))))[:-3]
        f.write(
            f'| [{file}](https://github.com/nhzaci/LeetCode/blob/master/{qn}) | Python |\n')
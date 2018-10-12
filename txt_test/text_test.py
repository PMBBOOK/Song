import random
import os

f = open('result.txt', 'w')
data = '스테디셀러\n2000년이전\n소설\n추리\n'
f.write(data)
f.close()
f = open("result.txt", 'r+')
script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]
result_txt_path = '%s\\result.txt' %script_dir
result = open(result_txt_path, 'r+')
details = result.readlines()
print(details)
details_index = random.randrange(0, len(details))
txt_path = 'link\\%s.txt' % details[details_index][:-1]
abs_txt_path = os.path.join(script_dir, txt_path)
link = open(abs_txt_path, 'r+')
link_lines = link.readlines()
link_index = random.randrange(0, len(link_lines))

print(abs_txt_path)
print(link_lines[link_index])
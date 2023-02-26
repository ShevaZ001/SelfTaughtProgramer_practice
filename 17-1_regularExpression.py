import re

l='Beautiful is better than ugly.'
matches=re.findall('Beautiful', l)
matches2=re.findall('beautiful', l, re.IGNORECASE)
zen = '''Although never is 
often better than 
*right* now.
If the implementation 
is hard to explain, 
it's a bad idea.
If the implementation 
is easy to explain, 
it may be a good 
idea. Namespaces 
are one honking 

great idea -- let's 
do more of those!'''

m = re.findall('^IF', zen, re.MULTILINE)

print('default result ---> {}\n' .format(matches))
print('ignoring captal result ---> {}\n' .format(matches2))
print('multi-line result ---> {}\n' .format(m))
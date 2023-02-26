question=input('貴方何歳？:')

with open('./python_practice/9-0_question.txt','w') as f:
    f.write('貴方何歳？ の答えは、「'+question+'」でした。')

Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
unite = twice + black_pink
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    unite = twice + black_pink
NameError: name 'twice' is not defined. Did you mean: 'slice'?
unite
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    unite
NameError: name 'unite' is not defined
twice = ['momo', 'sana', 'zwi', 'nayun', 'dahyun']
black_pink = ['jisu', 'jeni', 'rose', 'risa']
twice
['momo', 'sana', 'zwi', 'nayun', 'dahyun']
twice.append('jihyo')
twice
['momo', 'sana', 'zwi', 'nayun', 'dahyun', 'jihyo']
twice.sort()
twice
['dahyun', 'jihyo', 'momo', 'nayun', 'sana', 'zwi']
len(twice

    )
6
unite = twice + black_pink
unite
['dahyun', 'jihyo', 'momo', 'nayun', 'sana', 'zwi', 'jisu', 'jeni', 'rose', 'risa']
unite.remove('momo')
unite
['dahyun', 'jihyo', 'nayun', 'sana', 'zwi', 'jisu', 'jeni', 'rose', 'risa']
unite[0]
'dahyun'
unite[-1]
'risa'
unite[:3]
['dahyun', 'jihyo', 'nayun']
unite[-3:]
['jeni', 'rose', 'risa']
>>> score = {'momo' : 80, 'zwi' : 85, 'sana' : 98}
>>> type(score)
<class 'dict'>
>>> score['momo']
80
>>> score['nayun'] = 100
>>> score
{'momo': 80, 'zwi': 85, 'sana': 98, 'nayun': 100}
>>> del score ['momo']
>>> score
{'zwi': 85, 'sana': 98, 'nayun': 100}
>>> score.keys()
dict_keys(['zwi', 'sana', 'nayun'])
>>> score.values()
dict_values([85, 98, 100])
>>> 'zwi' in score
True
>>> 'momo' in score
False
>>> score.clear()
>>> scroe
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    scroe
NameError: name 'scroe' is not defined. Did you mean: 'score'?
>>> score
{}
>>> score['nayun']
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    score['nayun']
KeyError: 'nayun'
>>> type(score)
<class 'dict'>

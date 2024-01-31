import pyperclip,re

text = str(pyperclip.paste())
pattern = re.compile(r'')
# results  = pattern.findall(text)
# pyperclip.copy('\n'.join(results))
for i in text.split('\r\n'):
    if pattern.match(i):
        print(pattern.match(i).group())
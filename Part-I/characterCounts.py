import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = dict()

for character in message:
    count.setdefault(character,0)
    count[character] += 1

pprint.pprint(count)
print()
# print(pprint.pformat(count))
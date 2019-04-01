import time

data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
start_time = time.time()
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')

print(len(wc))

while True:
	word = input('What word do you want to check? ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過得次數為: ', wc[word])
	else:
		print('這個是沒有出現過喔')

print('感謝使用此功能')
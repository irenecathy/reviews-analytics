data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for length in data:
	sum_len += len(length)
average = sum_len/(len(data))
print('留言的平均長度為', average)
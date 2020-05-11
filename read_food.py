
#'r'為讀取(read)的指令，'w'則為寫入(write)的指令
#用於字串的功能.strip()可以用來去掉換行符號
with open('food.txt', 'r') as f:#將food.txt這個檔案讀進來後稱為f
	for line in f:
		print(line.strip())

good_drinks = []
with open('drinks.txt', 'r') as d:#將drinks.txt這個檔案讀進來後稱為d
	for line in d:
		good_drinks.append(line.strip())
print(good_drinks)

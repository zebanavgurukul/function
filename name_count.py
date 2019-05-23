def name_new(name_list):
	i = 0
	while i < len(name_list):
		sec_list = name_list[i]
		def name_count(list_1):
			j = 0
			while j <= len(sec_list):
				count = j
				j = j + 1
			print count,sec_list
		name_count(sec_list)
		i = i + 1
name = ["zeba","ravina","nilam","sweti","rashmi","kajal","sweta"]
name_new(name)

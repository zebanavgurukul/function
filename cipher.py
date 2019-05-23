def find_in_list(query, mainlist):
	mainlist_len = len(query)
	range_for_loop = len(mainlist)
	index = 0
	i = 0
	while i < (range_for_loop):
		element = mainlist[i]
		if element == query:
		    index = i
		i = i + 1
	return index


chars =        	['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['o','d','f','l','g','e','i','j','v','u','m','n','c','p','q','r','s','t','h','k','w','x','y','z','a','b']


def encrypt_message(plain_msg):
	encrypted_msg = ""
	character = 0
	while character < len(plain_msg):
		if plain_msg[character] in chars:
			char_index = find_in_list(plain_msg[character], chars)
			new_char = shifted_chars[char_index]
			encrypted_msg = encrypted_msg + new_char
		character = character + 1
	return encrypted_msg


def decrypt_message(encrypted_msg):
	decrypted_msg = ""
	chara = 0
	while chara < len(encrypted_msg):
		if encrypted_msg[chara] in shifted_chars:
			char_index = find_in_list(encrypted_msg[chara], shifted_chars)
			new_char = chars[char_index]
			decrypted_msg = decrypted_msg + new_char
		chara = chara + 1
	return decrypted_msg


flag = True
while True:
	choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
	if choice == "e":
	    plain_message = raw_input("Enter message to encrypt??")
	    print encrypt_message(plain_message)
	elif choice == "d":
	    encrypted_msg = raw_input("Enter message to decrypt?")
	    print decrypt_message(encrypted_msg)
	else:
	    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
	    if play_again == "y":
	        continue
	    elif play_again == "n":
	        break

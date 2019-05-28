chars =        	['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['o','d','f','h','g','e','i','j','v','u','m','n','c','p','q','r','b','t','l','k','w','x','y','z','a','s']


while True: 
    choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively:)  ")
    if choice == "e":
        plain_user = raw_input("Enter message to encrypt??:)  ")
        string = " "
        index = 0
        while index < len(plain_user):
            character = 0
            while character < len(chars):
                if plain_user[index] == chars[character]:
                    collect = character
                    string = string + shifted_chars[collect]
                character = character + 1
            index = index + 1
        print string
    elif choice == "d":
        plain_user = raw_input("Enter message to decrypt?:)  ")
        string2 = " "
        index = 0
        while index < len(plain_user):
            character = 0
            while character < len(shifted_chars):
                if plain_user[index] == shifted_chars[character]:
                    collect = character
                    string2 = string2 + chars[collect]
                character = character + 1
            index = index + 1
        print string2
	play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)-:) ")
	if play_again == "y":
	    continue
	elif play_again == "n":
	    break

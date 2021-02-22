loop = 0
loop2 = 0

logg = []


lösenord = input("Lösenord:\n>>>")
if lösenord == "EE19":
    loop = 1
    while loop == 1:
        meny = input("------\n[1] Visa loggar\n[2] Skriv en log\n[3] Rensa loggar\n[4] Avlsuta\n>>>")
        if meny == "1":
            print(f"------\nLoggar:\n{logg}")
            continue
            
        elif meny == "2":
            loop2 = 1
            while loop2 == 1:
                ny_logg = input("------\nLog:\n>>>")
                logg.append(ny_logg)
                fortsätta = input("------\n[1] Skriv en till log\n[2] Gå tillbaka till menyn\n>>>")
                if fortsätta == "1":
                    continue
                elif fortsätta == "2":
                    loop2 = 0
                    print("------\nDu skickas tillbaka till menyn...")
                    continue
                else:
                    print("------\nInget av alternativen blev valda, du skickas tillbaka till menyn...")

        elif meny == "3":
            logg_rensa = input("------\nVill du rensa dina loggar?\n[1] Ja\n[2] Nej, gå tillbaka till menyn\n>>>")
            if logg_rensa == "1":
                logg.clear()
            elif logg_rensa == "2":
                print("------\nDu skickas tillbaka till menyn...")
                continue
            else:
                print("------\nInget av alternativen blev valda, du skickas tillbaka till menyn...")

        elif meny == "4":
            print("------\nAvlutar...")
            print("Hejdå!")
            loop = 0

        else:
            continue
else:
    print("------\nFelaktigt lösenord")
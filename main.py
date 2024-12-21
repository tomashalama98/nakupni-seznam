print("Zapište potraviny, které chcete koupit. Pro ukončení napište 'konec'.")

nakupni_seznam = [] #list nákupního seznamu
while True:
    polozka = input("Zadejte potravinu (nebo 'konec' pro dokončení): ").strip()   #strip = odstranění prázdných znaků

    if polozka.lower() == 'konec':  # kontrola pro ukončení; "lower" = malá písmena
        break

    if not polozka:  # kontrola prázdného vstupu
        print("Zadali jste prázdný vstup, zkuste to znovu.")
        continue

    if " " in polozka:  # kontrola více slov
        print("Zadejte pouze jednu potravinu, ne více slov.")
        continue

    if not polozka.isalpha():  # kontrola zadání pouze písmen
        print("Zadejte platnou potravinu (pouze písmena).")
        continue

# kontrola duplicity položky v seznamu
    if polozka.lower() in [item.lower() for item in nakupni_seznam]:
        print(f"Položka '{polozka}' už je v seznamu.")
    else:
        nakupni_seznam.append(polozka)  # Přidání položky do seznamu
        print(f"Položka '{polozka}' byla přidána do seznamu.")

print("\nVáš nákupní seznam:", nakupni_seznam)


# odebrání položky
while True:
    odebrat = input("\nZadejte potravinu, kterou chcete odebrat (nebo 'konec' pro ukončení): ").strip()

    if odebrat.lower() == 'konec':  # kontrola pro ukončení
        break

    if not odebrat:  # kontrola prázdného vstupu
        print("Zadali jste prázdný vstup, zkuste to znovu.")
        continue

    # odebrání položky bez ohledu na velikost písmen
    for item in nakupni_seznam:
        if item.lower() == odebrat.lower():
            nakupni_seznam.remove(item)
            print(f"Položka '{item}' byla odebrána ze seznamu.")
            break
    else:
        print(f"Položka '{odebrat}' v seznamu neexistuje.")

print("\nVáš konečný nákupní seznam:", nakupni_seznam)
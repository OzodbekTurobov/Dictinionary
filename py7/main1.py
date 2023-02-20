a = input("Yo`nalishlarni tanlang: ").lower()
lolo = {
    "Python":" asosan beshta yo`nalishda ishlaydi",
    "Birinchisi":"Web Development",
    "Ikkinchisi":"Gul Development",
    "Uchinchisi":"Sciantific and Numeri",
    "To`rtinchisi":"Softwer Development",
    "Beshinchisi":"System Administration",
}
lolo.items()


if a == "python":
    print("Yo`nalishlari", a)
    print(lolo["Python"])
elif a == "birinchisi":
    print("Yo`nalish", a)
    print(lolo["Birinchisi"])
elif a == "ikkinchisi":
    print("Yo`nalish", a)
    print(lolo["Ikkinchisi"])
elif a == "uchinchisi":
    print("Yo`nalish", a)
    print(lolo["Uchinchisi"])
elif a == "to`rtinchisi":
    print("Yo`nalish", a)
    print(lolo["To`rtinchisi"])
elif a == "beshinchisi":
    print("Yo`nalish", a)
    print(lolo["Beshinchisi"])
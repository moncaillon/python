note = input("Quelle est votre note ? ")
note = int(note)
if note >= 17:
    print("A")
elif note >=14 and note <= 16:
    print("B")
elif note <=13 and note >=6:
    print("C")
#elif note <= 5:
else:
    print("D")
    
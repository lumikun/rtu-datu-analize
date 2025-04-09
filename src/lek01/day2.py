#  Loģika
#
# Uzd. 1
#
# Likumā “Par nekustamā īpašuma nodokli” ir noteiktas nodokļa likmes.
# #  Mājokļiem: 0,2 procenti no kadastrālās vērtības, kas nepārsniedz 56 915 eiro; 
# # 0,4 procenti no kadastrālās vērtības daļas, kas pārsniedz 56 915 eiro, bet nepārsniedz 106 715 eiro;
# # 0,6 procenti no kadastrālās vērtības daļas, kas pārsniedz 106 715 eiro

s = float(input("Nekustamā īpašuma vērtība: "))
likme = 0.0

if s <= 56915.00:
    likme = s * 0.002
elif s <= 106715.00:
    s -= 56915.00
    likme = 56915.00 * 0.002
    likme += s * 0.004
else:
    likme = 56915.00 * 0.002
    s -= 106715.00
    likme += 49800.00 * 0.004
    likme += s * 0.006

print(f"Jūsu nekustāmā īpašuma nodokļa likme ir €{likme:.2f}!")

# Uzd. 2

v = 6

# Principā taspats kas 'switch' C
match v:
    case 10:
        atzime = "Izcili"
    case 9:
        atzime = "Teicami"
    case 8:
        atzime = "Ļoti labi"
    case 7:
        atzime = "Labi"
    case _: 
        atzime = "Slikti"

print(f"{v} - {atzime}")

# Cikli
#
# Uzd. 3
# Uzņēmumam jasasniedz 10k darījumi, kad tos sasniedz jāizvada summa un darījumu skaits.
#

summa = 0.0
i = 0
while summa < 10000:
    summa += float(input("Ievadiet pārdoto summu: "))
    i += 1

print(f"Pārdotā summa ir sasniegta €{summa:.2f} kas sastāv no {i} darījumiem!")

# Funkcījas
#


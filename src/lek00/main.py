# Print 
x = -5.0
y = 5.0

print(f"{x:+10.3f} days, {y:+.0f} points")

# Type 

x = 5
y = -5.0
s = "Čiv riv!"
b = True
print(type(x)) # int (bigint?)
print(type(y)) # float
print(type(s)) # char* (str)
print(type(b)) # bool

# conversion
v1 = "5"
v2 = "6"

ret = int(v1) + int(v2)
print(ret)
ret = float(v1) + int(v2)
print(ret)

# Sestdienā 7 otrās klases bērni lasīja avenes. Katrs salasīja 5 litrus aveņu. Cik litrus aveņu bērni salasīja kopā?
b = 7
a = 5.0
ret = b * a 
print(f"Bērni kopā salasīja {ret:.2f} litru aveņu!")

# Tramvajā uz Zoodārzu brauca 44 pasažieri. Pieturā Mežaparks izkāpa 16 pieaugušie un 23 bērni. 
# Cik pasažieru palika tramvajā?
p = int(input("Pasažieru skaits tramvajā: "))
pie = int(input("Cik pieaugušo izkāpa?: "))
ber = int(input("Cik bērnu izkāpa?: "))
ret = p - pie - ber;
print(f"No tramvaja Mežparkā izkāpa {pie + ber} pasažieri un tramvajā palika {ret} pasažieri.")


# Papildspēle džokers?
# Skaitļu SUMMA? visās rindās un kolonnās ir vienāda?
#1 0 0 0 0 0 0 0 0 0
#2 4 0 0 0 0 0 0 0 0
#3 5 7 0 0 0 0 0 0 0
#0 6 8 10 0 0 0 0 0 0
#0 0 9 11 13 0 0 0 0 0
#0 0 0 12 14 16 0 0 0 0
#0 0 0 0 15 17 19 0 0 0
#0 0 0 0 0 18 20 22 0 0
#0 0 0 0 0 0 21 23 25 0
#0 0 0 0 0 0 0 24 26 27

#1 2 4 0 0 0 0 0 0 0
#0 3 5 7 0 0 0 0 0 0
#0 0 6 8 10 0 0 0 0 0
#0 0 0 9 11 13 0 0 0 0
#0 0 0 0 12 14 16 0 0 0
#0 0 0 0 0 15 17 19 0 0
#0 0 0 0 0 0 18 20 22 0
#0 0 0 0 0 0 0 21 23 25
#0 0 0 0 0 0 0 0 24 26
#0 0 0 0 0 0 0 0 0 27

#27 0 0 0 0 0 0 0 0 0
#26 25 0 0 0 0 0 0 0 0
#24 23 22 0 0 0 0 0 0 0
#0 21 20 19 0 0 0 0 0 0
#0 0 18 17 16 0 0 0 0 0
#0 0 0 15 14 13 0 0 0 0
#0 0 0 0 12 11 10 0 0 0
#0 0 0 0 0 9 8 7 0 0
#0 0 0 0 0 0 6 5 4 0

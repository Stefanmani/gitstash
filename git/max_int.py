# Gera lykkju til að leifa fjöld inputa
# Spyr aftur og aftur þanga til að sett er inn neikvæð tala
# Tekur input frá user og gáir hvort hún er stærri en sú fyrri

max_int = 0
while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int < 0:
        break
    if num_int > max_int:
        max_int = num_int
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line

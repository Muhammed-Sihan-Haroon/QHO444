print("How many bars should be charged")
bar_to_charge = int(input())
bars = 0
battery = ""
# ASCII
while bars < bar_to_charge:
    bars += 1
    battery = battery + "*"
    print(f"charging: {battery}")

print("The battery is full")
curr = "xxxxxGxx$xxT"
new_str = curr.replace("x", "")
ind_thief = new_str.index("T")
ind_dollars = new_str.index("$")
if abs(ind_dollars - ind_thief) == 1:
    print("ALARM")
else:
    print("quiet")



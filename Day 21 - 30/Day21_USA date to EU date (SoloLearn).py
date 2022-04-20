# CONVERT USA DATE TO EU DATE
month = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
}
usa_date = input(": ")
if "/" in usa_date:
    usa_split = usa_date.split("/")
    euro_date = usa_split[1] + "/" + usa_split[0] + "/" + usa_split[2]
    print(euro_date)
else:
    for i in month:
        if month[i] in usa_date:
            usa_split = usa_date.split(" ")
            usa_split1 = usa_split[1].split(",")
            euro_date = usa_split1[0] + "/" + str(i) + "/" + usa_split[2]
            print(euro_date)

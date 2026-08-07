#in ssmv school thgere are 60 students roll no. 35 is left the school so please remove it from your school data
#and print all other numbers.

data=list(range(1,61))
data.remove(35)
print(data)


#make a list of all states in india and print states which is in south india
states=["Arunachal Pradesh", "Assam", "Bihar","Chhattisgarh", "Goa", "Gujarat","Haryana", "Himachal Pradesh", "Jharkhand", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andhra Pradesh", "Karnataka", "Kerala", "Tamil Nadu", "Telangana"]
print(states[23:28])


#in one school prayer are going for the purpose siting arrangement of all numbers are last
#roll no to first roll no but what happen students are arogent and they do not seat with this pattern
#they seat with there friends kindlynarrange them in this order total student count is 10 and roll no
#is start with n101 to n102 like this

prayer=["N101","N102","N103","N105","N106","N104","N107","N108","N110","N109"]
print(prayer.sort())
print(prayer.reverse())
print(prayer)

prayer=["N101","N102","N103","N105","N106","N104","N107","N108","N110","N109"]
print(prayer.sort(reverse=True))

print(prayer)

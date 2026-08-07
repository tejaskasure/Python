hero={
    "Name":["tejas","gaurav","tanmay"],
    "movie":["abc","cocktail","3idiots"]}
print(hero)
hero["movie"][2]="PK"
print(hero)
hero["Name"].insert(3,"vedant")
print(hero)

#create a disctionary and state and city and kindly update state, maharashtra with new city
#palghar
#and remove pune from maharashtra
state={"Maharashtra":

["Mumbai","Pune","Nagpur"]," Gujarat":["Ahmedabad","Surat","Vadodara"],"Karnataka": ["Bangalore","Mysore","Hubli"]}

state["Maharashtra"].remove("Pune")

state["Maharashtra"].insert(3, "palgar")

print(state)

#creatye a record of hospital name is rubi hospital create patient and doctor name as well as room no. and 
#disease and kindely arange patient name in assennding orders and doctor name dessending order
#and room no in assending order and isease in desending order
# Hospital Record Data
hospital_record = {
    "hospital_name": "Ruby Hospital",
    "patients": ["Suresh", "Amit", "Pooja", "Deepak", "Ananya"],
    "doctors": ["Dr. Sharma", "Dr. Verma", "Dr. Kulkarni", "Dr. Deshmukh","Dr. Zende"],
    "room_numbers": [305, 102, 401, 204, 105],
    "diseases": ["Malaria", "Dengue", "Typhoid", "Flu", "Covid-19"],
}

# Sorting the data based on requirements:
# 1. Patient names in Ascending order
hospital_record["patients"].sort()

# 2. Doctor names in Descending order
hospital_record["doctors"].sort(reverse=True)

# 3. Room numbers in Ascending order
hospital_record["room_numbers"].sort()

# 4. Diseases in Descending order
hospital_record["diseases"].sort(reverse=True)


# Displaying the organized record
print(f"--- {hospital_record['hospital_name']} Record ---")
print("Patients (Ascending):", hospital_record["patients"])
print("Doctors (Descending):", hospital_record["doctors"])
print("Room Numbers (Ascending):", hospital_record["room_numbers"])
print("Diseases (Descending):", hospital_record["diseases"])

#example
movie={"abc": "ccc","nnn":"sss"}
print(movie.values())
serial={"anupama":["annirudha"],"tarak meheta":["tarak"]}
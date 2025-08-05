import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-4e4e7-default-rtdb.firebaseio.com/"
})
ref= db.reference('Students')

data= {
    "2206156":{
        "name": "Abdullah Maaz",
        "Dept": "IT",
        "starting_year": 2022,
        "total_attendance":7,
        "standing": "G",
        "year": 2,
        "last_attendance_time":"2024-4-11 00:54:34"
    },
    "2206149":{
        "name": "Imaduddin Qazi",
        "Dept": "IT",
        "starting_year": 2022,
        "total_attendance":8,
        "standing": "G",
        "year": 2,
        "last_attendance_time":"2024-4-11 00:54:34"
    },
    "2206151":{
        "name": "Sahil Saraf",
        "Dept": "IT",
        "starting_year": 2022,
        "total_attendance":9,
        "standing": "G",
        "year": 2,
        "last_attendance_time":"2024-4-11 00:54:34"
    },
    "2206158":{
        "name": "Pratik Ghute",
        "Dept": "IT",
        "starting_year": 2022,
        "total_attendance":10,
        "standing": "G",
        "year": 2,
        "last_attendance_time":"2024-4-11 00:54:34"
    },
    "2206137":{
        "name": "Rishi Khandelwal",
        "Dept": "IT",
        "starting_year": 2022,
        "total_attendance":10,
        "standing": "G",
        "year": 2,
        "last_attendance_time":"2024-4-11 00:54:34"
    }
}
for key,value in data.items():
    ref.child(key).set(value)
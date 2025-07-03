import json

with open('students.json' , 'r') as json_file:
    students = json.load(json_file)

sorted_students=students.sort(key=lambda x : x['score'] , reverse = True)

with open('rating.json' ,'w') as json_file_w:
    json.dump(students , json_file_w, indent=4)
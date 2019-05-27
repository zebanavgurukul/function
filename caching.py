import requests
import json
import os


course_url = "http://saral.navgurukul.org/api/courses"


def request(url):
        response = requests.get(url)
        with open("coursesData.json","w") as file:
                file.write(response.content)
        return response.json()
#print(request(course_url))


def read_file(f_read):
        with open("coursesData.json","r") as file:
                data_read = file.read()
                # print data_read
                data_load = json.loads(data_read)
                # print data_load
        return(data_load)
#print(read_file())


coursesIdList = []
def saral_courses(data_load):
        index = 0
        while index < (len(data_load['availableCourses'])):
                courses = data_load['availableCourses'][index]
                courses_name = courses['name']
                coursesId = courses['id']
                coursesIdList.append(coursesId)
                print index+1,"*",courses_name,coursesId
                index = index + 1
        return coursesId
#saral_courses()


def file_courses_fun():
        if os.path.exists("coursesData.json"):
                data_load = read_file("coursesData.json")
                saral_courses(data_load)
                print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        else:
                request(course_url)
                data_load = read_file("coursesData.json")
                saral_courses(data_load)
                print "########################################"
file_courses_fun()


user_exercises = int(raw_input("enter your id"))
select_courses = coursesIdList[user_exercises - 1]
# print select_courses
exercise_url = course_url+"/"+str(select_courses)+"/exercises"
# print exercise_url
def exercises(user_id):
        # print user_id
        exercise_data = requests.get(user_id)
        #print (exercise_data)
        with open("exercises_"+str(select_courses)+".json","w") as file:
                file.write(exercise_data.content)
        exercise_response = exercise_data.json()
        #print (exercise_response)
        return (exercise_response)
# exercises_name = exercises(exercise_url)
# print exercises_name


def exercise_read(f_read):
        with open("exercises_"+str(select_courses)+".json","r") as file:
                data_read = file.read()
                # print data_read
                data_load = json.loads(data_read)
                # print data_load
        return(data_load)


def exercise_name(data1):
        # print data1
        i = 0
        while i < len((data1["data"])):
                course_exercise = data1["data"][i]["name"]
                print i+1, "*",course_exercise
                i = i + 1
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"        
        return course_exercise
# course_data = exercise_name(exercises_name)
#print course_data


def file_exists_fun():
        if os.path.exists("exercises_"+str(select_courses)+".json"):
                data_load = exercise_read("exercises_"+str(select_courses)+".json")
                exercise_name(data_load)
                print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        else:
                exercises(exercise_url)
                data_load = exercise_read("exercises_"+str(select_courses)+".json")
                exercise_name(data_load)
                print "########################################"
file_exists_fun()


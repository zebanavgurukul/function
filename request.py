import requests
import json

saral_url = "http://saral.navgurukul.org/api/courses" 


def saral(link):
        saral_url_data = requests.get(link)
        response = saral_url_data.json()
        return response
saral (saral_url)


all_courses = saral(saral_url)
# print all_courses


def displayCourses(all_courses):
        #print all_courses
        i = 0
        while i < len((all_courses["availableCourses"])):
                course = all_courses["availableCourses"][i]["name"]
                course_list = (all_courses["availableCourses"][i]["id"])
                print (i+1), course, course_list
                i = i + 1
        return course_list
displayCourses(all_courses)


course_list = all_courses["availableCourses"]
# print course_list

def exercises(user_id):
        # print user_id
        exercise_url = saral_url+"/"+str(user_id)+"/exercises"
        #print exercise_url
        exercise_data = requests.get(exercise_url)
        #print (exercise_data)
        exercise_response = exercise_data.json()
        #print (exercise_response)
        return (exercise_response)
user_exercises = int(raw_input("enter your id"))
exercises_name = exercises(user_exercises)
#print exercises_name


def exercise(data1):
        print data1
        i = 0
        while i < len((data1["data"])):
                course_exercise = data1["data"][i]["name"]
                print i+1, course_exercise
                i = i + 1
        return course_exercise
course_data = exercise(exercises_name)
#print course_data


def parentExerciseId(data):
        #print data
        child_excercise_list = []
        i = 0
        while i < len(data["data"]):
                child_exercise_data = data["data"][i]
                child_exercise = child_exercise_data["childExercises"]
                child_excercise_list.append(child_exercise)
                i = i + 1
        return child_excercise_list
childExercises_data = parentExerciseId(exercises_name)
# print childExercises_data


def childexcercise_name(name,user_child):
        #print name
        child_excercise_user = name[user_child-1]
        #print  child_excercise_user
        i = 0
        while i < len(child_excercise_user):
                child_name = child_excercise_user[i]["name"]
                i = i + 1
                print i,child_name
        return child_excercise_user
user_child = input("enter the childexcercise")
exerci_name = childexcercise_name(childExercises_data,user_child)
# print exerci_name


def childexcercise_slug(slug,user_child_slug):
        #print slug
        slug_list = []
        i = 0
        while i < len(slug):
                child_slug = slug[i]["slug"]
                slug_list.append(child_slug)
                i = i + 1
        print slug_list
        return slug_list
user_child_slug = input("enter the slug")
exerci_slug = childexcercise_slug(exerci_name,user_child_slug)
# print exerci_slug


def childexcercise_id(child_id,user_child_id):
        #print child_id
        id_list = []
        i = 0
        while i < len(child_id):
                id_child_ex = child_id[i]["id"]
                id_list.append(id_child_ex)
                i = i + 1
        print id_list
        return id_list
user_child_id = input("enter the id")
exerci_id = childexcercise_id(exerci_name,user_child_id)
#print exerci_id


def content_name(slug_cont,slug_user):
        slug = slug_cont[slug_user-1]
        slug_id = exerci_id[slug_user-1]
        slug_url = "http://saral.navgurukul.org/api/courses/" +str(slug_id)+"/exercise/getBySlug?slug="+(slug)
        print slug_url
        slug_data = requests.get(slug_url)
        # print slug_data
        slug_content = slug_data.json()
        # print slug_content
        content = slug_content["content"]
        print content
        return content
slug_user = input("enter your slug")
content_data = content_name(exerci_slug,slug_user)
# print content_data


def next_and_Previous (slug_n_p):
        slug_num = 1
        while True:
                slug_np = str(raw_input("enter n for next slug and enter p for previous slug"))
                if slug_np == "n":
                        #print slug_np
                        if slug_user <len(exerci_slug):
                                # print(slug_user)
                                # print(len(slug_list))
                                next = slug_user+slug_num
                                # print(slug_num)
                                # print(next)
                                slug = exerci_slug[next-1]
                                #print slug, "slug"
                                next_slug = exerci_id[slug_user]
                                #print next_slug, "id" 
                                slug_url = "http://saral.navgurukul.org/api/courses/" +str(next_slug)+"/exercise/getBySlug?slug="+str(slug)
                                #print slug_url
                                slug_data = requests.get(slug_url)
                                #print slug_data
                                slug_content = slug_data.json()
                                #print slug_content
                                content = slug_content["content"]
                                print content
                        else:
                                print " their are no slugs left "

                elif slug_np == "p":
                        # print slug_np
                        if slug_user < len(exerci_slug)-1:
                                previous = slug_user - slug_num
                                # print previous
                                slug = exerci_slug[previous-1]
                                # print slug 
                                previous_slug = exerci_id[slug_user]
                                # print previous_slug
                                slug_url = "http://saral.navgurukul.org/api/courses/" +str(previous_slug)+"/exercise/getBySlug?slug="+str(slug)
                                # print slug_url
                                slug_data = requests.get(slug_url)
                                # print slug_data
                                slug_content = slug_data.json()
                                # print slug_content
                                content = slug_content["content"]
                                print content
                                break 
                        else:
                                print "their are no slugs left"
                slug_num = slug_num + 1
                print (slug_num, "------------")
previous_and_next = next_and_Previous(content_data)
# print previous_and_next

def up (up_data,user_up):
        # print up_data
        if user_up == "up":
                # print user_up
                i = 0
                while i < len(up_data["availableCourses"]):
                        course = up_data["availableCourses"][i]["name"]
                        print (i+1), course
                        i = i + 1
                return course
user_up = str(raw_input ("enter your up"))    
Up_navigation = up (all_courses,user_up) 
# print Up_navigation
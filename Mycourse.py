import secrets
from extensionMycourse import loop,courses_avaliable
from functools import reduce
print("Welcome")
print()
print(courses_avaliable)
print()
#taking name of user
name = input("please enter your name : ")
print()
#taking interest of user
interests = input("please give information about things you like, what you would like to do, subjects you like,"
                      " things you love being around and in it mention the specific fields "
                      "eg: science(technology or health), "
                      "arts...etc also try to narrow it down as possible"
                      " eg: i have interest in science and technology : ").lower()
print()

#Here User enters the number of subjects taken in Waec and Jamb
entry_waec = int(input("please enter number of entry for waec : "))
entry_jamb = int(input("please enter number of entry for jamb : "))
jamb_courses, jamb_results = [], []
waec_courses, waec_results = [], []
surge1 = [waec_courses, waec_results]
surge2 = [jamb_courses, jamb_results]
print('For your Waec')
loop(surge1,entry_waec) #function imported from extensionMycourse to take courses and results for Waec
print()
print('Now for your Jamb')
loop(surge2,entry_jamb) #function imported from extensionMycourse to take courses and results for Jamb
data2 = dict(zip(waec_courses,waec_results))
data1 = dict(zip(jamb_courses,jamb_results))
if 'mathematics' not in waec_courses or data2['mathematics']<40 or\
        'english' not in waec_courses or data2['english']<40:
    print()
    print("mathematics and english are compuslory subjects")
    exit(0)
print("Waec data", data2)
print("Jamb data", data1)
total_jamb = reduce(lambda a,b : a+b, jamb_results)
print(f'Jamb total = {total_jamb}')
print()


#Now the selection, the conditional statements evaluate which course will
# be most suitable for User and if not, renders User not eligible
if 'technology' in interests or 'engineering' in interests or 'engineer' in interests:
    if (data2['mathematics'] >= 70) and (data2['physics'] >= 70) and (data2['chemistry'] >= 70):
        if total_jamb >= 260:
            print(f'name : {name} | Your course : {secrets.choice(courses_avaliable[1:5])}')
        elif 200 <= total_jamb < 260:
            print(f'name : {name} | Your course : {secrets.choice(courses_avaliable[8:12])}')
        else:
            print("Not eligible for admission")
            exit(0)
    elif (40 <= data2['mathematics'] <= 100) and (40 <= data2['physics'] <= 100) and (40 <= data2['chemistry'] <= 100):
        print(f'name : {name} | Your course : {secrets.choice(courses_avaliable[8:12])}')
    else:
        print("Not eligible for admission")
        exit(0)


elif 'health' in interests or 'medicine' in interests or 'doctor' in interests:
    if (data2['biology']>=70) and (data2['physics']>=70) and (data2['chemistry']>=70):
      if total_jamb >= 275:
          print(f'name : {name} | Your course : {secrets.choice(courses_avaliable[5:8])}')
      elif 200<= total_jamb <= 275:
          print(f'name : {name} | Your course : {secrets.choice(courses_avaliable[8:10])}')
      else:
          print("Not eligible for admission")
          exit(0)
    elif (40 <= data2['biology'] <= 100) and (40 <= data2['physics'] <= 100) and (40 <= data2['chemistry'] <= 100):
        print(f'name : {name} | Your course : {secrets.choice(courses_avaliable[8:10])}')
    else:
        print("Not eligible for admission")
        exit(0)

    
elif 'arts' in interests or 'law' in interests or 'lawyer' in interests:
    if data2['government'] >= 70 and data2['english'] >= 70 and data2['literature'] >= 70:
        if total_jamb >= 270:
            print(f'name : {name} | Your course : {courses_avaliable[12]}')
        elif 200 <= total_jamb <= 270:
            print(f'name : {name} | Your course : {courses_avaliable[13:16]}')
        else:
            print("Not eligible for admission")
            exit(0)
    elif (40 <= data2['government'] <= 100) and (40 <= data2['english'] <= 100) and (40 <= data2['literature'] <= 100):
        print(f'name : {name} | Your course : {courses_avaliable[13:16]}')
    else:
        print("Not eligible for admission")
        exit(0)



elif 'commercial' in interests or 'business' in interests or 'accountant' in interests:
    if data2['commerce'] >= 70 and data2['economics'] >= 70 and data2['accounting'] >= 70:
        if total_jamb >= 260:
            print(f'name : {name} | Your course : {courses_avaliable[16:18]}')
        elif 200<=total_jamb <260:
            print(f'name : {name} | Your course : {courses_avaliable[18]}')
        else:
            print("Not eligible for admission")
            exit(0)
    elif (40 <= data2['commerce'] <= 100) and (40 <= data2['economics'] <= 100) and (40 <= data2['accounting'] <= 100):
        print(f'name : {name} | Your course : {courses_avaliable[18]}')
    else:
        print("Not eligible for admission")
        exit(0)

else:
    print("Information needed not gotten, please check that you entered the proper requirements")
    exit(0)
print()
print("NB: mathematics and english are required for all fields in waec")
print()

















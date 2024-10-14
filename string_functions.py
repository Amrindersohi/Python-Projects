school_name = input('please enter the school name')
location = input('please enter the location ')

school_caps= school_name.upper()
location_caps=location.upper()
print(school_caps, location_caps)

school_lower=school_caps.lower()
location_lower= location_caps.lower()
print(school_lower,location_lower)

print(school_name, location.replace(location,"computer network"))

instructor= "Mary"
subject= "math"
year= "summer 2020"
print('{} will teach {} in {}.'.format(instructor,subject,year))

str1= "pythonabcd"
str2= "xyzlanguage"

print(str1[0:6],str2[3:])

name=" amrinder "
print(name*3)

print("because it is an assignment operator and it only supports boolean operation")
student_heights = input("Input a list of student heights in centimeters seperated by a space \n")
heights_list = student_heights.split()

heights = []

for height in heights_list:
    heights.append(int(height))


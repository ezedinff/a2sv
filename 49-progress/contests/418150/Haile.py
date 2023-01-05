'''
Nati B wants to get the information of all the group 42 students from Hailemariam - a head of education for Group 42. Haile stores all his students' information in a grid. Each student's information is stored in a new row and each column represents specific information about the student in a particular row. He has three columns for - Full names, emails, and phone numbers respectively. But to save memory space he separates these columns with Hashes(#). He did not want to do the work of separating them so he just sent the information as it is to Nati B.

Nati B wants you to help him organize the data in a manageable fashion.

Input
The first line contains an integer N - the number of students in group 42 ( 1 <= N <= 28).

The following N lines contain a string s. S can only contain alphabets, digits, and @, # symbols. the length of each s can be at most 100.

Output
Print N lines that contain the students' First Name, Phone Number, and Email separated by Spaces.

Example
input
2
AdmasTerefe#0987654363#admas@gmail.com
AmanuelYihune#091234567#aman@gmail.com

output
AdmasTerefe 0987654363 admas@gmail.com
AmanuelYihune 091234567 aman@gmail.com
'''


n = int(input())
for i in range(n):
    s = input()
    s = s.split('#')
    print(s[0], s[1], s[2])

# Path: Haile.py
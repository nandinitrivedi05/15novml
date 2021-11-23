print(5**9)                                               
print(3//2)						  						  
print(7/3)						  
print(6==6)						  
a=20;a+=30;a%=3						  
print(a)						  
print(True * False)					  
print(True & False)					  
print(True and False)		 		  	  
print(((6>3) and (7<4) or (18==3)) and (9>3))		  
print(True is False)					  
print(False in False)
                                                          
                                                          
                                                        

print(((True==False) or (False>True)) and (False<=True))  

#Ques3
s1="Nice to have it"
s2="here"
print(s1+' '+s2)

#Ques4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Ques5
s1="Nice to have it"
s2="here"

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

a.insert(0,s1)
a.append(s2)
print(a)

#Ques6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

i=0
while(numbers[i]!=412):
    if numbers[i]%2==0:
        print(numbers[i])
    i=i+1
#Ques7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)
    
#Ques8
#--------

#Ques9
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#Ques10
#--------

#Ques11
print("Enter the string: ")
s4=input().split(',')
print(s4)
s4.sort()
print(s4)

#Ques12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i
        
d2=d['Student']
print(d2[j])

#Ques13
#s='hello world! 123'
s=input("Enter a string:")
letter=0
digit=0
for i in s:
    if i.isalpha():
        letter=letter+1
    if i.isdigit():
        digit=digit+1
print("LETTERS ",letter)
print("DIGITS ",digit)

#Ques14
#------

#Ques 16
#-------

    

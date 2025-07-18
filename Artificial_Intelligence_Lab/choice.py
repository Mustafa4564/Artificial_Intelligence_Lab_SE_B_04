print("This is a simple stream selection system for students, The program will suggest you the specific stream based on your interest")
print("Select any two subjects from the Given list:\n 1.Math\n 2.Physics\n 3.Chemistry\n 4.Biology\n 5.Logic and gates\n 6.graphics\n 7.programming\n 8.AI\n")
sub1=str(input("Select the 1st subject"))
sub2=str(input("Select the 2nd subject"))
if(sub1=="Math" and sub2=="Physics")or(sub1=="Physics" and sub2=="Math"):
	print("Mechanical Engineering")
elif(sub1=="Math" and sub2=="Logic and gates")or(sub1=="Logic and gates" and sub2=="Math"):
	print("Electrical Engineering")
elif(sub1=="chemistry" and sub2=="Biology")or(sub1=="Biology" and sub2=="Chemistry"):
	print("MBBS")
elif(sub1=="graphics" and sub2=="Math")or(sub1=="Math" and sub2=="graphics"):
	print("Civil")
elif(sub1=="programming" and sub2=="Math")or(sub1=="Math" and sub2=="programming"):
	print("CS Engineering")
elif(sub1=="AI" and sub2=="Math")or(sub1=="Math" and sub2=="AI"):
	print("AI & DS Engineering")
else:
	print("No Stream for you,sorry")

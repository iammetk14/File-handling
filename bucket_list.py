#'w' erases all the previous content and starts from the beggining.
#'r' is used to only read the content without being able to make any changes into it.
#'a' is used to append/add new lines and content after the original data. i.e. both original data and new content are displayed.
file=open(r"D:\Web dev course\Specialization in python\File handling\sample.txt","w")
file.write("1. Visit europe to watch Manchester city play.")
file.write("\n2. Practice football.")
file.write("\n3. Learn how to play guitar.")
file.write("\n4. Learn how to do coding and get specialized in python and other languages.")
file.close()
print("Bucket list saved to sample.txt")

#reading the conetext.
file=open("D:\Web dev course\Specialization in python\File handling\sample.txt","r")
content=file.read()
print("THE CONTENT:")
print(content)
file.close()

#counting number of lines.
file=open("D:\Web dev course\Specialization in python\File handling\sample.txt","r")
lines=file.readlines()
print(f"This bucket list has {len(lines)} lines")
file.close()

#Appending/adding more lines to the bucket list.
file=open(r"D:\Web dev course\Specialization in python\File handling\sample.txt","a")
file.write("\n5. Finish exam syllabus.")
file.write("\n6. Have fun with friends, family and in classes.")
file.close()
print("\n Bucket list updated.")
#Last part(reading).
file=open("D:\Web dev course\Specialization in python\File handling\sample.txt","r")
print(file.read())
file.close()
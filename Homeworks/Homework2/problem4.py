

text=input("Enter please text:")

count_USA=text.count("USA")
count_usa=text.count("usa")
count=count_USA+count_usa

new_text=text.replace("USA","Armenia")
new_text=new_text.replace("usa","Armenia")

print("The given string:",text)
print("The USA/usa count is:",count)
print("the new string:",new_text)



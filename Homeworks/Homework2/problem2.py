

text=input("Enter please text,which has seven or more odd characters։")

start=len(text)//2-1
end=start+3
mid3chars=text[start:end]
text_upper=text.upper()

print("The old string:",text)
print("Middle 3 characters:",mid3chars)
print("The new string:",text_upper)



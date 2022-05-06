from dataclasses import replace


name=input("Enter your name:")
address=input("Enter your add:")
city=input("Enter your city:")
zip=input("Enter your code:")
phone=input("Enter phone number:")
letter='''
[name]
[address] | [City,Code] | [Phone] | [Email]
[Date]
[Recipient Name]
[Title]
[Company]
[Address]
[City, ST ZIP Code]
Dear [Recipient]:
[If you’re ready to write, just select this tip text and start typing to replace it with your own. Don’t include space to the right or left of the characters in your selection.]
[Apply any text formatting you see in this letter with just a click from the Home tab, in the Styles group.]
[Wondering what to include in your cover letter? It’s a good idea to include key points about why you’re a great fit for the company and the best choice for the specific job. Of course, don’t forget to ask for the interview—but keep it brief! A cover letter shouldn’t read like a novel, no matter how great a plot you’ve got.]
Sincerely,


[Your Name]
'''
letter=letter.replace("[name]",name)
letter =letter.replace("[address]",address)
print(letter)
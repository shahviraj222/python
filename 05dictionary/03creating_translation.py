hindi_english={"pankha":"fan",
                "dabba":"Box",
                "vastu":"item"}
print(type(hindi_english))
v=input("Enter the Hindi word to translate:")
print(" Translation\n",v,":",hindi_english.get(v))
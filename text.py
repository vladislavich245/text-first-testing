with open(
    'notes.txt','r', encoding='utf-8'
    ) as file:
    data = file.read()
print(data)
question1= input('Хто написав ці рядки?')
with open(
    'notes.txt','a', encoding='utf-8'
    ) as file:
    file.write(question1)
question2 = input("Хочете добавити цитату?(Так/Ні)")
if question2=='так' or question2=='Так':

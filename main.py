# текстовые, бинарные

# чтение r
# запись w
# дозапись а

# чтение rb
# запись wb

# open(путь_до_файла,режима_работы,


file=open("byron.txt", mode="r", encoding="utf-8")
# .read()-считывает весь текст из файла
# .readlines()-считает каждую строку сформировав список строк
# .readline()-считывает каждыую строку по очереди

#text = file.read()
# text = file.readlines()
# print(text)

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.writable())
file.close()

# запись данных в файл
file2 =open('new_file.txt',mode='w',encoding='utf-8')
#.write()- записывает текст в одну строку
#.writelines(cписок_строк)-принимает список строку и записывает в файл
# file2.write('Hello world\n')
# file2.write('Привет мир')
lines = [f'{i} строка\n' for i in range(1,101)]
file2.writelines(lines)
file2.close()

# работа с бинарными файлами

# img = open('photo_2023-10-02_19-45-49.jpg', mode='rb')
# content = img.read()
# print(content)
# img.close()
#with - контекстный менежер, позводящий не закрывать соединение

# with open('photo_2023-10-02_19-45-49.jpg', mode='rb') as img:
#     content = img.read()
#     for i in range(1,11):
#         new_img = open(f'{i}.jpg',mode='wb')
#         new_img.write(content)
#         new_img.close()
#     print(img.closed)
# print(img.closed)

file2 = open('new_file.txt', mode='a', encoding='utf-8')
lines = [f'{i} строка\n' for i in range(101,201)]
file2.writelines(lines)
file2.close()

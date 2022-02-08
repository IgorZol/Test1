with open("test.txt", "w", encoding = "utf-8") as file:
    x = file.write("Привет, я тестовый файл")
    file.close()
import subprocess


''' Задание 1.
Напиши функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе и False в противном случае. 
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
'''

def read_file(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, ""
    except subprocess.CalledProcessError:
        return False, ""

if __name__ == '__main__':
    open_success, file_content = read_file("cat /home/user/exchange/Test/Lesson_01/Seminar_DZ/text.txt")
    if open_success:
        print("SUCCESS")
        print(f"File Content: {file_content}")
    else:
        print("FAIL")

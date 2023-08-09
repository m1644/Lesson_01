import subprocess
import string


''' Задание 2.
Доработать функцию из предыдущего задания таким образом, чтобы у нее появился дополнительный режим работы, 
в котором вывод разбивается на слова с удалением всех знаков пунктуации 
(их можно взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие слова в выводе.
'''

def read_file(command, split_words=False, target_word=None):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')
        if result.returncode == 0:
            output = result.stdout
            if split_words:
                words = output.split()
                words_without_punctuation = [word.strip(string.punctuation) for word in words]
                if target_word and target_word in words_without_punctuation:
                    return True, words_without_punctuation
                else:
                    return False, []
            else:
                return True, output
        else:
            return False, ""
    except subprocess.CalledProcessError:
        return False, ""

if __name__ == '__main__':
    open_success, content = read_file("cat /home/user/exchange/Test/Lesson_01/Seminar_DZ/text.txt", 
                                      split_words=True, 
                                      target_word="Hello")
    if open_success:
        print("SUCCESS")
        print(f"File Content (Words without Punctuation): {content}")
    else:
        print("FAIL")

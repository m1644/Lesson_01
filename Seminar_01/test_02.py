import subprocess


''' Задание 2
Переписать тест на Python c использованием модуля subprocess
'''

if __name__ == '__main__':
    result = subprocess.run("cat /etc/os-release", 
                            stdout=subprocess.PIPE,  
                            shell=True, 
                            encoding='utf-8')
    result_output = result.stdout

    if "22.04.3" in result_output and "jammy" in result_output and result.returncode == 0:
        print("SUCCESS")
    else:
        print("FAIL")

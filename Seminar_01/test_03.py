import subprocess


''' Задание 3
Доработать тест из предыдущего задания таким образом, чтобы вывод сохранялся построчно в список 
и в тесте проверялось, что в этом списке есть строки VERSION="22.04.1 LTS (Jammy Jellyfish)" 
и VERSION_CODENAME=jammy . Проверка должна выполняться только если код возврата равен 0.
'''

if __name__ == '__main__':
    result = subprocess.run("cat /etc/os-release", 
                            stdout=subprocess.PIPE,  
                            shell=True, 
                            encoding='utf-8')
    output_lines = result.stdout.splitlines()
    return_code = result.returncode

    if return_code == 0 and any('VERSION="22.04.3 LTS (Jammy Jellyfish)"' in line for line in output_lines) and any('VERSION_CODENAME=jammy' in line for line in output_lines):
        print("SUCCESS")
    else:
        print("FAIL")

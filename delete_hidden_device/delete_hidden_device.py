import os
import subprocess
import time


def exec_subprocess(cmd_line, print_stdout=True):
    # print('Exex cmd: ' + cmd_line)
    xe = subprocess.run(cmd_line, stdout=subprocess.PIPE)
    stdout = xe.stdout.decode('gbk', 'ignore')
    if print_stdout:
        print(stdout)
    return stdout


visitable_device = exec_subprocess('devcon find *', False)
# print('visitable_device =', visitable_device)
all_device = exec_subprocess('devcon findall *', False)
# print('all_device =', all_device)

all_device_lines = all_device.split('\r\n')
visitable_device_lines = visitable_device.split('\r\n')

print('Hidden Devices:')
hidden_device_lines = []
for line in all_device_lines:
    if line not in visitable_device_lines:
        if 'matching device(s) found.' not in line:
            hidden_device_lines.append(line)
            print(line)

if len(hidden_device_lines) > 0:
    key = input('To delete hidden device, Press y/Y')
    if 'y' not in key.lower():
        print('Exit')
        time.sleep(3)
        exit(0)

    for dev in hidden_device_lines:
        dev_ins_path = dev.split(':')[0].strip()
        exec_subprocess('devcon remove "@' + dev_ins_path + '"')

else:
    print('None')

input("Press Any Key Exit")

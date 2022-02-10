from psutil import process_iter
from os import system


version = 1.0
author = 'Ivan Perzhinsky'

roblox = 'RobloxPlayerBeta.exe'
trx = 'TRX.exe'

roblox_kill_command = f'taskkill /F /IM {roblox}'

def get_processes_names():
    return [proc.name() for proc in process_iter()]

def kill_roblox():
    for proc in process_iter():
        if proc.name() == roblox:
            system(roblox_kill_command)

print('Welcome to Roblox protector from TRX injector.')
print(f'Version: {str(version).replace(".", ",")}.')
print(f'By {author}.')

print('\nStarting listener.')
print('Press [CTRL + C] to stop.\n')

while True:
    try:
        processes = get_processes_names()

        roblox_started = roblox in processes
        trx_started = trx in processes

        if roblox_started and trx_started:
            print('Roblox detected.')
            print('TRX Detected.')

            print('Killing roblox.\n')

            kill_roblox()

            print('\nRoblox killed.')
            print('Continuing work...')
    except KeyboardInterrupt:
        print('\nInterrupted.')

        break

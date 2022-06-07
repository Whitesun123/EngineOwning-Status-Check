from rich import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from selenium.webdriver.chrome.options import Options
import logging
import os
from time import sleep

def clear():
        if os.name == 'nt':
                return os.system('cls')
        else:
                return os.system('clear')
clear()
print('[[bold green]*[/]] Cleared [bold blue]terminal[/] ...')
logging.disable(logging.CRITICAL)

x = PrettyTable(center=True)

x.field_names = ["Game", "Status"]

x.border = True
x.junction_char = '%'
x.horizontal_char = '+'
x.vertical_char = '^'
print('[[bold green]*[/]] Setting up [bold blue]tables[/] ...')
options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
print('[[bold green]*[/]] Starting [bold blue]Google[/] ...')
driver.get("https://www.engineowning.to/shop/status")

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/ul/li[18]/img")))
print('[[bold green]*[/]] Waiting for [bold blue]element[/] ...')


def Vanguard():
    #VANGUARD
    try:
        Vanguard = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/ul/li[11]")

        if Vanguard.text == 'CoD: Vanguard: Undetected':
#            return '[+] CoD: Vanguard: [bold green]Undetected[/]'
            x.add_row(['CoD: Vanguard', 'Undetected'])
            print('\n[[bold green]*[/]] Adding [bold blue]Vanguard[/] status to [bold blue]table[/] ...')
            return 'Undetected'
            
        else:
#            return print('[-] CoD: Vanguard: [bold red]Updating[/]')
#             return '[-] CoD: Vanguard: [bold red]Updating[/]'
            x.add_row(['CoD: Vanguard', 'Updating'])
            print('\n[[bold green]*[/]] Adding [bold blue]Vanguard[/] status to [bold blue]table[/] ...')
            return 'Updating'
            
    except:
#        return '[-] CoD: Vanguard: [bold red]Updating[/]'
        x.add_row(['CoD: Vanguard', 'Updating'])
        print('\n[[bold green]*[/]] Adding [bold blue]Vanguard[/] status to [bold blue]table[/] ...')
        return 'Updating'

def Modern_Warfare():
    #MODERN WARFARE    
    try:
        ModernWarfare = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/ul/li[8]")
        if ModernWarfare.text == 'CoD: MW and Warzone: Undetected':
#            return '[+] CoD: Modern Warfare: [bold green]Undetected[/]
            x.add_row(['CoD: Modern Warfare', 'Undetected'])
            print('\n[[bold green]*[/]] Adding [bold blue]Modern Warfare[/] status to [bold blue]table[/] ...')
            return 'Undetected'
        else:
#            return '[-] CoD: Modern Warfare: [bold red]Updating[/]'
            x.add_row(['CoD: Modern Warfare', 'Updating'])
            print('\n[[bold green]*[/]] Adding [bold blue]Modern Warfare[/] status to [bold blue]table[/] ...')
            return 'Updating'
            
    except:
#        return '[-] CoD: Modern Warfare: [bold red]Updating[/]'
        x.add_row(['CoD: Modern Warfare', 'Updating'])
        print('\n[[bold green]*[/]] Adding [bold blue]Modern Warfare[/] status to [bold blue]table[/] ...')
        return 'Updating'

def Modern_Warfare_Lite():
    #MODERN WARFARE LITE    
    try:
        ModernWarfare = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/ul/li[9]")
        if ModernWarfare.text == 'CoD: MW and Warzone LITE: Undetected':
#            return '[+] CoD: Modern Warfare Lite: [bold green]Undetected[/]'
            x.add_row(['CoD: Modern Warfare Lite', 'Undetected'])
            print('\n[[bold green]*[/]] Adding [bold blue]Modern Warfare Lite[/] status to [bold blue]table[/] ...')
            return 'Undetected'
        else:
#            return '[-] CoD: Modern Warfare Lite: [bold red]Updating[/]'
            x.add_row(['CoD: Modern Warfare Lite', 'Updating'])
            print('\n[[bold green]*[/]] Adding [bold blue]Modern Warfare Lite[/] status to [bold blue]table[/] ...')
            return 'Updating'
            
    except:
#        return '[-] CoD: Modern Warfare Lite: [bold red]Updating[/]'
        x.add_row(['CoD: Modern Warfare Lite', 'Updating'])
        print('\n[[bold green]*[/]] Adding [bold blue]Modern Warfare Lite[/] status to [bold blue]table[/] ...')
        return 'Updating'

def Spoofer():    
    #SPOOFER
    try:
        ModernWarfare = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/ul/li[13]")
        if ModernWarfare.text == 'EngineOwning Spoofer: Undetected':
#            return '[+] EngineOwning Spoofer: [bold green]Undetected[/]'
            x.add_row(['EngineOwning Spoofer', 'Undetected'])
            print('\n[[bold green]*[/]] Adding [bold blue]Spoofer[/] status to [bold blue]table[/] ...')
            return 'Undetected'
        else:
#            return '[-] EngineOwning Spoofer: [bold red]Updating[/]'
            x.add_row(['EngineOwning Spoofer', 'Updating'])
            print('\n[[bold green]*[/]] Adding [bold blue]Spoofer[/] status to [bold blue]table[/] ...')
            return 'Updating'
            
    except:
#        return '[-] CoD: Modern Warfare Lite: [bold red]Updating[/]'
        x.add_row(['EngineOwning Spoofer', 'Updating'])
        print('\n[[bold green]*[/]] Adding [bold blue]Spoofer[/] status to [bold blue]table[/] ...')
        return 'Updating'

Vanguard()
print('[[bold green]*[/]] Checking [bold blue]Vanguard[/] ...')
sleep(0.5)
Modern_Warfare()
print('[[bold green]*[/]] Checking [bold blue]Modern Warfare[/] ...')
sleep(0.5)
Modern_Warfare_Lite()
print('[[bold green]*[/]] Checking [bold blue]Modern Warfare Lite[/] ...')
sleep(0.5)
Spoofer()
print('[[bold green]*[/]] Checking [bold blue]Spoofer[/] ...\n')
sleep(0.5)

print(x)
input('\nPress \u001b[33m"ENTER"\u001b[0m to exit...')
driver.quit()
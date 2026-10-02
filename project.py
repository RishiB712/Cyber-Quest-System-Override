import sys
import random
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    player_hp = 100
    boss_hp = 150
    player_energy = 0
    max_player_hp = 100
    max_boss_hp = 150
    max_energy = 50
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}=== CYBER QUEST: SYSTEM OVERRIDE ===\n")
    print(f"{Fore.RED}WARNING: A FATAL VIRUS has breached the mainframe!\n")
    time.sleep(2)
    while True:
        clear_screen()
        print(f"{Fore.GREEN}{Style.BRIGHT}PLAYER HP:     {create_bar(player_hp, max_player_hp)}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}PLAYER ENERGY: {create_bar(player_energy, max_energy)}")
        print(f"{Fore.RED}{Style.BRIGHT}BOSS HP:       {create_bar(boss_hp, max_boss_hp)}\n")
        status=check_battle_status(player_hp, boss_hp)
        if status=="win":
            print(f"{Fore.GREEN}{Style.BRIGHT}CONGRATULATIONS! You successfully purged the virus! 🎉")
            break
        elif status=="lose":
            print(f"{Fore.RED}{Style.BRIGHT}SYSTEM FAILURE. The mainframe was corrupted. 💀")
            break
        print(f"{Style.BRIGHT}Choose your protocol:")
        print("1. 🗡️  Quick Strike   (Dmg: 10-15 | Energy: +15)")
        print("2. ⚡ Heavy Hack     (Dmg: 5-25  | Energy: +10)")
        print("3. 🛡️  Firewall       (Block 50% incoming damage | Energy: +20)")
        print("4. 💖 System Patch   (Heal: 15-20 HP)")
        if player_energy>=max_energy:
            print(f"5. 🚀 {Fore.CYAN}{Style.BRIGHT}OVERCLOCK ULTIMATE (Dmg: 40-50 | Requires 50 Energy){Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}5. 🚀 OVERCLOCK ULTIMATE (Requires {max_energy} Energy - Currently at {player_energy}){Style.RESET_ALL}")
        choice=input(f"\n{Fore.YELLOW}Execute command (1-5): {Style.RESET_ALL}")
        print("\n")
        is_defending=False
        if choice=='1':
            dmg=calculate_value('strike')
            boss_hp-=dmg
            player_energy=min(player_energy + 15, max_energy)
            print(f"{Fore.CYAN}Executing Quick Strike! Dealt {dmg} damage.")
        elif choice=='2':
            dmg=calculate_value('hack')
            boss_hp-=dmg
            player_energy=min(player_energy + 10, max_energy)
            print(f"{Fore.CYAN}Executing Heavy Hack! Dealt {dmg} damage.")
        elif choice=='3':
            is_defending=True
            player_energy=min(player_energy + 20, max_energy)
            print(f"{Fore.BLUE}Firewall activated! Defenses temporarily boosted.")
        elif choice=='4':
            heal=calculate_value('patch')
            player_hp=min(player_hp + heal, max_player_hp)
            print(f"{Fore.GREEN}System Patch applied! Recovered {heal} HP.")
        elif choice=='5':
            if player_energy>=max_energy:
                dmg=calculate_value('ultimate')
                boss_hp-=dmg
                player_energy=0
                print(f"{Fore.MAGENTA}{Style.BRIGHT}*** OVERCLOCK INITIATED! ***")
                print(f"{Fore.MAGENTA}A massive energy surge dealt {dmg} damage to the Boss!")
            else:
                print(f"{Fore.RED}Insufficient Energy! The command failed and you lost your turn.")
        else:
            print(f"{Fore.RED}Invalid syntax. Turn skipped!")
        time.sleep(2)
        if boss_hp<=0:
            continue
        boss_dmg=calculate_value('boss_attack')
        if random.random()>0.8:
            boss_dmg+=10
            print(f"{Fore.RED}{Style.BRIGHT}CRITICAL ALERT! The Virus uses a Data Spike!")
        if is_defending:
            boss_dmg=boss_dmg // 2
            print(f"{Fore.BLUE}Your Firewall absorbed 50% of the impact!")
        player_hp-=boss_dmg
        print(f"{Fore.RED}The Virus attacks! Dealt {boss_dmg} damage to you.\n")
        time.sleep(2.5)
def create_bar(value, max_value):
    """Generates a visual progress bar for HP or Energy."""
    if value<0:
        value=0
    filled_length=int(20*value//max_value)
    filled_length=min(20, max(0, filled_length))
    bar='█'*filled_length+'-'*(20-filled_length)
    return f"[{bar}] {value}/{max_value}"
def calculate_value(action):
    """Calculates randomized integers for attacks, blocks, and heals."""
    if action=='strike':
        return random.randint(10, 15)
    elif action=='hack':
        return random.randint(5, 25)
    elif action=='patch':
        return random.randint(15, 20)
    elif action=='boss_attack':
        return random.randint(10, 18)
    elif action=='ultimate':
        return random.randint(40, 50)
    return 0
def check_battle_status(player_hp, boss_hp):
    """Determines if the game should end based on current HP values."""
    if player_hp<=0 and boss_hp<=0:
        return "lose"
    elif player_hp<=0:
        return "lose"
    elif boss_hp<=0:
        return "win"
    return "continue"
if __name__ == "__main__":
    main()

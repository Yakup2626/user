import subprocess

def run_command(command):
    """Führt einen Shell-Befehl aus und gibt die Ausgabe zurück."""
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e.stderr}")

# Befehle
commands = [
    "sudo apt remove -y firefox",  # Firefox entfernen
    "sudo apt-get update",  # Paketlisten aktualisieren
    "sudo apt install -y openssh-server",  # SSH-Server installieren
    "sudo apt-get full-upgrade -y",  # System vollständig aktualisieren
    "sudo apt autoremove -y",  # Nicht mehr benötigte Pakete entfernen
    "sudo apt autoclean -y",  # Cache bereinigen
    "sudo apt remove -y --purge mint-meta-cinnamon cinnamon*",  # Linux Mint Cinnamon Desktop entfernen
    "sudo apt remove -y --purge lightdm",  # Display Manager entfernen
    "sudo systemctl set-default multi-user.target",  # Terminal-Startmodus setzen
    "sudo reboot"  # Neustart für Änderungen
]

# Befehle ausführen
for cmd in commands:
    run_command(cmd)

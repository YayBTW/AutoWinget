import subprocess
import os
import time

mod = 0
output = subprocess.run("powershell winget upgrade", capture_output=True, text=True)

if "No installed package found matching input criteria." in output.stdout:
    print("Guncelleme bulunamadı.")
    temp = input()
else:
    mod = 1

if mod == 1:
    print(output.stdout)

    user_input = input("Guncellemek istiyor musun?(y/n)")

    if user_input == "y":
        os.system("powershell winget upgrade --all")
        print("Guncellenme tamamlandı.")
        temp = input()
    else:
        print("Cikiliyor.")
        time.sleep(2)

# This is a fork from original BSDS by [Crazor](https://github.com/CrazorTheCat)  with a lot less features, it is meant for developement, do not use for production and hosting for others.

Discord link : https://discord.gg/mt4dUxXryh


## How to play BSDS: ##

### Server ###
1: Download the server and extract it.

2: Open terminal on your computer and go to BSDS directory.

3: Type python Core.py and it's done, follow client instructions.

### iOS client ###
1: Download the client and extract it. [https://www.mediafire.com/file/wq1n9nr3smp8tni/BSDS_V51.ipa/file](https://www.mediafire.com/file/wq1n9nr3smp8tni/BSDS_V51.ipa/file)

2: go to Payload/Brawl Stars.app/ in your file manager and start a new tab and go to this location in your terminal.

3: In your file manager, you will see ipPatcher.py, open it in any text editor and locate in the first line of the script the patched_ip variable with a string.

4: Change the string to be your ipv4 address of your device you execute the server from.

5: After the ip changed is saved, in your terminal with the client location, execute this following command : python ipPatcher.py

6: Save and compile back to ipa format.

7: Install the client using your favorite app installer and enjoy BSDS.

### Android client ###
1: Download the apk here: soon ;)

2: Download an apk editor of your choice

3: Decompile the apk with the apk editor and go to lib/armeabi-v7a/libkagenay.c.so and open the file with a text editor.

4: Edit "redirectHost": "192.168.18.102" to your ipv4 address, if your self hosting.

5: How to find ipv4 address?, if your running the server on your phone, you can change that "192.168.18.102" to "127.0.0.1", otherwise if your running the server on pc, open command prompt and type ipconfig and you'll see your ipv4 address down below which will start like "192.168.xx.xx"

6: Compile the apk with the changes and install it, and enjoy playing bsds brawl!

## Optional Steps [ Android ] ##
1: If you want to change port you could change redirectPort to whatever port you want, keep in mind you have to change port in server too.

2: if you don't want bsds settings you could disable it by setting hideBSDSSettings to true 

![IMG_1193](https://github.com/risporce/BSDS/assets/72312877/02eadac3-a921-4526-af2c-0c185f9975d3)

## credits ##
[kagenay](https://github.com/kagenay) Android Client

[S.B#0056](https://github.com/HaccerCat) for his help with crypto and client

[Vitalik](https://github.com/VitalikObject) for his crypto from [OldBrawl](https://github.com/VitalikObject/OldBrawl)

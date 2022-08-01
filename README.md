# Enigma
Basic enigma device replicated through code, with a file for testing and GUI

Base Code:
---------------

Enigma contained 3 'disks' each containing 0 - 25, representing the letters in the alphabet. The numbers are not in order on any of the disks. To start an encryption,
the start point of all 3 disks needs to be selected. The cipher text for each letter is determined by the disks. The letter corresponds to a number on the first disk
which leads to that place in the second disk containing another number that correspinds to a place on the 3rd disk. This number is the place of the letter in the 
alphabet that will replace the plain text. Whenever a letter is selected and moves through the disks, each disk cycles.

Tester Code:
---------------

The tester code takes in a premade list of words and runs the encryption function on all of the words and then the decryption function on all of the encrypted results in
all of the possible starting settings of the enigma code. It tallies the number of encryptions, the success rate of the encryption and decrptions matching, as well as the runtime.

GUI:
---------------
The GUI contains 3 menus: the main menu, the ecnryption menu, and the decryption menu. The main menu contains two buttons to access the encryption or decryption menu. 
Both of those menus contain 2 buttons, one exit button that leads back to the main menu, and 1 button for encryption/decryption respectively. For the e/d menus, there 
are 3 boxes for 3 starting numbers for the disks. The lower box is for the text to be encrypted or decrypted. When the e or d button is pressed, the encryption or 
decryption is displayed below the input text box.

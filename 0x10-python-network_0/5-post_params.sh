#!/bin/bash
# Script that sends a POST request and displays the body response
<<<<<<< HEAD
#curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
#curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
=======
>>>>>>> 6e91f5a119ec9dded07bef7af841804b0f031438
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" $1

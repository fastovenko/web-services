#!/bin/bash
echo "Hi, bro!"

choice=""

while [[ $choice != "0" ]]; do

   clear
   sudo docker ps -a

   echo -e "\n\n"
   echo "1. mysql UP"
   echo "2. mysql DOWN"
   echo "0. Exit"

   echo
   echo -n "Enter your choice, or 0 for exit: "
   read choice
   echo

   case $choice in
       1)
       echo -e $CYAN1"mysql up...\n"$NORM
       sudo docker-compose -f docker-compose.yml up -d
       break
       ;;
       2)
       echo -e $CYAN1"mysql down...\n"$NORM
       sudo docker-compose -f docker-compose.yml down
       cd $HOME
       break
       ;;
       0)
       echo -e $YELLOW1"OK, see you!\n"$NORM
       break
       ;;
       *)
       echo "That is not a valid choice, try a number from 0 to 10."
       ;;
   esac
done

sudo docker ps -a

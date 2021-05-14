#!/bin/bash

echo "--------------BOT SETUP--------------------------"
echo "Enter your bot's name"
read bot_name

echo "Enter your bot's TOKKEN id"
read tokken_id

echo -e "#Bot Config\n\nbotName = \"$bot_name\"\nbotTokkenId = \"$tokken_id\"" > botConfig.py
echo "Bot Config Done!"

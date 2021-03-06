#!/usr/bin/python
# 
# Filename:  cloakify.py 
#
# Version: 1.0.1
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:  Exfiltration toolset (see decloakify.py) that transforms data into lists 
# of words / phrases / Unicode to ease exfiltration of data across monitored networks, 
# essentially hiding the data in plain sight, and facilitates social engineering attacks 
# against human analysts and their workflows. Bonus Feature: Defeats signature-based 
# malware detection tools (cloak your other tools).
#
# Description:  Base64-encodes the given payload and translates the output using a list 
# of words/phrases/Unicode provided in the cipher. This is NOT a secure encryption tool, 
# it only obfuscates the payload data (the output is currently vulnerable to frequency 
# analysis attacks). You can of course use an encrypted file as the payload, however.
#
# Prepackaged ciphers include: lists of desserts in English, Arabic, Thai, Russian, 
# Hindi, Chinese, Persian, and Muppet (Swedish Chef); PokemonGo creatures; Top 100 IP 
# Addresses; Top Websites; GeoCoords of World Capitols; MD5 Password Hashes; An Emoji 
# cipher; Star Trek characters; Geocaching Locations; Amphibians (Scientific Names); 
# evadeAV cipher (simple cipher that minimizes size of the resulting obfuscated data).
#
# To create your own cipher:
#
#	- Generate a list of at least 66 unique words (Unicode-16 accepted)
#	- Remove all duplicate entries and blank lines
# 	- Randomize the list
#	- Provide the file as the cipher argument to the script.
# 
# Example:  
#
#   $ ./cloakify.py payload.txt ciphers/desserts.ciph > exfiltrate.txt
# 
# Current Limitations:
#
# 	- Vulnerable to frequency analysis attacks, use scripts in 'addNoise' directory
#	  to add entropy to your cloaked payloads (must strip away prior to decloaking)
#	- Creates temporary Base64 file in local directory and deletes when finished,
#	  but does not do "secure delete" (potential digital forensics trail)

import os, sys, getopt, base64

array64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")
payloadB64File = "payloadB64.txt";

if ( len(sys.argv) != 3 ):
	print "usage: cloakify.py <payloadFilename> <cipherFilename>"
	exit

else:
	base64.encode( open( sys.argv[1] ), open( payloadB64File, "w" ))

	with open( payloadB64File ) as file:
    		payloadB64 = file.read()

	with open( sys.argv[2]) as file:
    		arrayCipher = file.readlines()

	for char in payloadB64:
		if char != '\n':
			print arrayCipher[ array64.index(char) ],

	if os.path.exists( payloadB64File ):
    		os.remove( payloadB64File )

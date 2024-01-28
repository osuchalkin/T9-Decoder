#!/usr/bin/env python3

import argparse  


# Create a dictionary of correspondence between numbers and letters.
t9_map = {
    "2": "a",
    "22": "b",
    "222": "c",
    "3": "d",
    "33": "e",
    "333": "f",
    "4": "g",
    "44": "h",
    "444": "i",
    "5": "j",
    "55": "k",
    "555": "l",
    "6": "m",
    "66": "n",
    "666": "o",
    "7": "p",
    "77": "q",
    "777": "r",
    "7777": "s",
    "8": "t",
    "88": "u",
    "888": "v",
    "9": "w",
    "99": "x",
    "999": "y",
    "9999": "z",
  }


def get_arguments():
    parser = argparse.ArgumentParser(description='T9 Encoder / Decoder.')
    parser.add_argument("-d", dest="decode", help="Set T9 string to decode, i.e. -d '7777 2 88 555'")
    parser.add_argument("-e", dest="encode", help="Set string to encode in T9, i.e. -e 'string'")
    options = parser.parse_args()

    if not options.decode and not options.encode:
        parser.error("[-] Please specify option and string, use --help for more info")

    return options       


def decode_t9(text):
  """Decoding T9-string"""  

  # Delete non decimal symbols and 0 and 1
  new_text = ""
  for character in text:
       if (character.isdecimal() and character not in "10") or character == " ":
          new_text += character

  print(new_text)
  # Divide the T9-string into separate digits.
  digits = new_text.split()

  # Decode each digit
  decoded_text = ""
  for digit in digits:
    decoded_text += t9_map[digit]

  return decoded_text


def encode_t9(text):
   """Encrypting string in T9."""
   
   # Delete spaces and not letter symbols
   new_text = ""
   for character in text:
       if character != " " and character.isalpha():
          new_text += character

   new_text = new_text.lower()

   encrypted_text = ""
   for letter in new_text:
      for key, value in t9_map.items():
         if value == letter:
            crypt_letter = key
      encrypted_text += crypt_letter + " "
   encrypted_text.rstrip()

   return encrypted_text
         

def main():

    options = get_arguments()

    if options.decode:
       s = decode_t9(options.decode)
    if options.encode:
       s = encode_t9(options.encode)
       
    print(f'[+] Result: {s}')


if __name__ == '__main__': 
  main()                                          
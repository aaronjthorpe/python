# Emoji!!! 🤣
# https://www.unicode.org/emoji/charts/full-emoji-list.html
# https://www.unicode.org/emoji/charts/full-emoji-modifiers.html

print("\U0001F600") # Thumbs up using 'unicode code point'
print(chr(0x1F600)) # Thumbs up using chr function to convert unicde number (hexadecimal)

print("\U0001F44B") # Waving Hand
print("\U0001F44B\U0001F3FB") # Waving Hand 'light skin'
print("\U0001F44B\U0001F3FC") # Waving Hand 'medium-light skin'
print("\U0001F44B\U0001F3FD") # Waving Hand 'medium skin'
print("\U0001F44B\U0001F3FE") # Waving Hand 'medium-dark skin'
print("\U0001F44B\U0001F3FF") # Waving Hand 'dark skin'

#"Health Worker" is made up of multiple pieces of information:
#1F9D1 - Adult
#200D - invisible joiner (i.e. combine multiple values together to make one emoji)
#2695 - medical (Staff of Aesculapius ⚕)
#FE0F - variation selector
#1F3FB,#1F3FC,#1F3FD,#1F3FE,1F3FF - skin tone selector

print("\U00002695") # 'Staff of Aesculapius'
print("\U0001F9D1") # 'Adult'
print("\U0001F9D1\U0000200D\U00002695\U0000FE0F") # 'Health Worker' (Adult/Medical Variation)
print("\U0001F9D1\U0001F3FB\U0000200D\U00002695\U0000FE0F") # 'Health Worker' with 'light skin'
print("\U0001F9D1\U0001F3FC\U0000200D\U00002695\U0000FE0F") # 'Health Worker' with 'medium-light skin'
print("\U0001F9D1\U0001F3FD\U0000200D\U00002695\U0000FE0F") # 'Health Worker' with 'medium skin'
print("\U0001F9D1\U0001F3FE\U0000200D\U00002695\U0000FE0F") # 'Health Worker' with 'medium-dark skin'
print("\U0001F9D1\U0001F3FF\U0000200D\U00002695\U0000FE0F") # 'Health Worker' with 'dark skin'

#1F3F3 Waving White Flag, FE0F variation/colour/graphical, 200D joiner, 1F308 rainbow
print("\U0001F3F3") # White Flag
print("\U0001F308") # Rainbow
print("\U0001F3F3\U0000FE0F\U0000200D\U0001F308") # rainbow flag
print("\U0001F3F4\U0000200D\U00002620\U0000FE0F") # pirate flag = black flag + joiner + skull and crossbones + graphical colour

# Waving hand base emoji
waving_hand = "\U0001F44B"

# Skin tone modifiers using a dictionary
skin_tones = {
    "Light": "\U0001F3FB",
    "Medium-Light": "\U0001F3FC",
    "Medium": "\U0001F3FD",
    "Medium-Dark": "\U0001F3FE",
    "Dark": "\U0001F3FF"
}

# Print waving hand with each skin tone
print("Waving hand with skin tones:")
for tone_name, modifier in skin_tones.items():
    print(f"{tone_name}: {waving_hand}{modifier}")
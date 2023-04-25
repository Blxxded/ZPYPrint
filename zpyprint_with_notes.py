# -*- coding: utf-8 -*-

import re

def ZPrint(Message = ""): # https://github.com/Blxxded/ZPYPrint/README.md
	Message = re.sub(r"\[\[(0|RESET|DEFAULT|NORMAL|NOT|PRIMARY)\]\]", "\u001b[0m", Message) # 0: Disables every attribute.
	Message = re.sub(r"\[\[(1|BOLD|INCREASED)\]\]", "\u001b[1m", Message) # 1: Makes the text "stronger".
	Message = re.sub(r"\[\[(2|DECREASED|FAINT)\]\]", "\u001b[2m", Message) # 2: Makes the text "weaker".
	Message = re.sub(r"\[\[(3|CURSIVE|ITALIC)\]\]", "\u001b[3m", Message) # 3: Not widely supported! Curves the text. Sometimes treated as blink (See 5 for reference) or reverse (See 7 for reference).
	Message = re.sub(r"\[\[(4|UNDERLINE|UNDERLINED)\]\]", "\u001b[4m", Message) # 4: Not widely supported! Underlines the text.
	Message = re.sub(r"\[\[(5|BLINK|SLOWBLINK)\]\]", "\u001b[5m", Message) # 5: Blinks less than 150 times per minute.
	Message = re.sub(r"\[\[(6|FASTBLINK|RAPIDBLINK)\]\]", "\u001b[6m", Message) # 6: Not widely supported! Blinks more than 150 times per minute.
	Message = re.sub(r"\[\[(7|INVERT|INVERTED|REVERSE|REVERSED)\]\]", "\u001b[7m", Message) # 7: Swap background and foreground colors.
	Message = re.sub(r"\[\[(8|CONCEAL|CONCEALED|HIDE|HIDDEN)\]\]", "\u001b[8m", Message) # 8: Not widely supported! Hides the text.
	Message = re.sub(r"\[\[(9|CROSSED|CROSSEDOUT|STRIKE|STRIKED)\]\]", "\u001b[9m", Message) # 9: Makes the text legible but marked as if for deletion.
	Message = re.sub(r"\[\[(20|BLACKLETTER|FRAKTUR|GOTHIC)\]\]", "\u001b[20m", Message) # 20: Rarely supported! The text has a calligraphic hand style.
	Message = re.sub(r"\[\[(21|DOUBLEUNDERLINE|DOUBLEUNDERLINED)\]\]", "\u001b[21m", Message) # 21: Double-underlines the text BUT disables bold intensity on several terminals.
	Message = re.sub(r"\[\[(22|NOTBOLD|NOTDECREASED|NOTFAINT|NOTINCREASED|NOTINTENSITY)\]\]", "\u001b[22m", Message) # 22: Disables bold (See 1 for reference) and faint (See 2 for reference). Color changes where intensity is implemented.
	Message = re.sub(r"\[\[(23|NOTBLACKLETTER|NOTCURSIVE|NOTITALIC|NOTFRAKTUR|NOTGOTHIC)\]\]", "\u001b[23m", Message) # 23: Rarely supported! Stops italic (See 3 for reference) and fraktur (See 20 for reference).
	Message = re.sub(r"\[\[(24|NOTUNDERLINE|NOTUNDERLINED|NOTDOUBLEUNDERLINE|NOTDOUBLEUNDERLINED)\]\]", "\u001b[24m", Message) # 24: Neither singly (See 4) nor doubly underlined (See 21 for reference).
	Message = re.sub(r"\[\[(25|NOTBLINK|NOTSLOWBLINK|NOTFASTBLINK|NOTRAPIDBLINK)\]\]", "\u001b[25m", Message) # 25: Stop both types of blinking (See 5 and 6).
	Message = re.sub(r"\[\[(26|PROPORTIONALSPACING|SPACING)\]\]", "\u001b[26m", Message) # 26: Not known to be used on terminals! Gives a proportional spacing to the text.
	Message = re.sub(r"\[\[(27|NOTINVERT|NOTINVERTED|NOTREVERSE|NOTREVERSED)\]\]", "\u001b[27m", Message) # 27: Undoes swapped colors (See 7 for reference).
	Message = re.sub(r"\[\[(28|NOTCONCEAL|NOTCONCEALED|NOTHIDE|NOTHIDDEN|REVEAL|REVEALED|SHOW|SHOWN)\]\]", "\u001b[28m", Message) # 28: Not widely supported! Reveals the text (See 8 for reference).
	Message = re.sub(r"\[\[(29|NOTCROSSED|NOTCROSSEDOUT|NOTSTRIKE|NOTSTRIKED)\]\]", "\u001b[29m", Message) # 29: Makes the text not crossed (See 9 for reference).
	Message = re.sub(r"\[\[(30|BLACK)\]\]", "\u001b[30m", Message) # 30: Sets the foreground color to black.
	Message = re.sub(r"\[\[(31|RED)\]\]", "\u001b[31m", Message) # 31: Sets the foreground color to red.
	Message = re.sub(r"\[\[(32|GREEN)\]\]", "\u001b[32m", Message) # 32: Sets the foreground color to green.
	Message = re.sub(r"\[\[(33|YELLOW)\]\]", "\u001b[33m", Message) # 33: Sets the foreground color to yellow.
	Message = re.sub(r"\[\[(34|BLUE)\]\]", "\u001b[34m", Message) # 34: Sets the foreground color to blue.
	Message = re.sub(r"\[\[(35|MAGENTA|PURPLE)\]\]", "\u001b[35m", Message) # 35: Sets the foreground color to magenta.
	Message = re.sub(r"\[\[(36|CYAN|TURQUOISE)\]\]", "\u001b[36m", Message) # 36: Sets the foreground color to cyan.
	Message = re.sub(r"\[\[(37|WHITE)\]\]", "\u001b[37m", Message) # 37: Sets the foreground color to white.
	Message = re.sub(r"\[\[(39|DEFAULTFG|DEFAULTFOREGROUND)\]\]", "\u001b[39m", Message) # 39: Sets the foreground color to the default value.
	Message = re.sub(r"\[\[(40|BGBLACK)\]\]", "\u001b[40m", Message) # 40: Sets the background color to black.
	Message = re.sub(r"\[\[(41|BGRED)\]\]", "\u001b[41m", Message) # 41: Sets the background color to red.
	Message = re.sub(r"\[\[(42|BGGREEN)\]\]", "\u001b[42m", Message) # 42: Sets the background color to green.
	Message = re.sub(r"\[\[(43|BGYELLOW)\]\]", "\u001b[43m", Message) # 43: Sets the background color to yellow.
	Message = re.sub(r"\[\[(44|BGBLUE)\]\]", "\u001b[44m", Message) # 44: Sets the background color to blue.
	Message = re.sub(r"\[\[(45|BGMAGENTA|BGPURPLE)\]\]", "\u001b[45m", Message) # 45: Sets the background color to magenta.
	Message = re.sub(r"\[\[(46|BGCYAN|BGTURQUOISE)\]\]", "\u001b[46m", Message) # 46: Sets the background color to cyan.
	Message = re.sub(r"\[\[(47|BGWHITE)\]\]", "\u001b[47m", Message) # 47: Sets the background color to white.
	Message = re.sub(r"\[\[(49|DEFAULTBG|DEFAULTBACKGROUND)\]\]", "\u001b[49m", Message) # 49: Sets the background color to the default value.
	Message = re.sub(r"\[\[(50|NOTPROPORTIONALSPACING|NOTSPACING)\]\]", "\u001b[50m", Message) # 50: Not known to be used on terminals! Disables the proportional spacing to the text (See 26 for reference).
	Message = re.sub(r"\[\[(51|FRAMED)\]\]", "\u001b[51m", Message) # 51: Frames the text.
	Message = re.sub(r"\[\[(52|ENCIRCLED)\]\]", "\u001b[52m", Message) # 52: Encircles the text.
	Message = re.sub(r"\[\[(53|OVERLINE|OVERLINED)\]\]", "\u001b[53m", Message) # 53: Overlines the text.
	Message = re.sub(r"\[\[(54|NOTENCIRCLED|NOTFRAMED)\]\]", "\u001b[54m", Message) # 54: Stops both encircled (See 52 for reference) and framed (See 51 for reference) attributes.
	Message = re.sub(r"\[\[(55|NOTOVERLINE|NOTOVERLINED)\]\]", "\u001b[55m", Message) # 55: Stops overlining the text (See 53 for reference).
	Message = re.sub(r"\[\[(90|BRIGHTBLACK|LIGHTBLACK|GRAY)\]\]", "\u001b[90m", Message) # 90: Sets the foreground color to gray.
	Message = re.sub(r"\[\[(91|BRIGHTRED|LIGHTRED)\]\]", "\u001b[91m", Message) # 91: Sets the foreground color to a lighter red.
	Message = re.sub(r"\[\[(92|BRIGHTGREEN|LIGHTGREEN)\]\]", "\u001b[92m", Message) # 92: Sets the foreground color to a lighter green.
	Message = re.sub(r"\[\[(93|BRIGHTYELLOW|LIGHTYELLOW)\]\]", "\u001b[93m", Message) # 93: Sets the foreground color to a lighter yellow.
	Message = re.sub(r"\[\[(94|BRIGHTBLUE|LIGHTBLUE)\]\]", "\u001b[94m", Message) # 94: Sets the foreground color to a lighter blue.
	Message = re.sub(r"\[\[(95|BRIGHTMAGENTA|LIGHTMAGENTA|BRIGHTPURPLE|LIGHTPURPLE)\]\]", "\u001b[95m", Message) # 95: Sets the foreground color to a lighter magenta.
	Message = re.sub(r"\[\[(96|BRIGHTCYAN|LIGHTCYAN|BRIGHTTURQUOISE|LIGHTTURQUOISE)\]\]", "\u001b[96m", Message) # 96: Sets the foreground color to a lighter cyan.
	Message = re.sub(r"\[\[(97|BRIGHTWHITE|LIGHTWHITE)\]\]", "\u001b[97m", Message) # 97: Sets the foreground color to a lighter white.
	Message = re.sub(r"\[\[(100|BGBRIGHTBLACK|BGLIGHTBLACK|BGGRAY)\]\]", "\u001b[100m", Message) # 100: Sets the background color to a lighter gray.
	Message = re.sub(r"\[\[(101|BGBRIGHTRED|BGLIGHTRED)\]\]", "\u001b[101m", Message) # 101: Sets the background color to a lighter red.
	Message = re.sub(r"\[\[(102|BGBRIGHTGREEN|BGLIGHTGREEN)\]\]", "\u001b[102m", Message) # 102: Sets the background color to a lighter green.
	Message = re.sub(r"\[\[(103|BGBRIGHTYELLOW|BGLIGHTYELLOW)\]\]", "\u001b[103m", Message) # 103: Sets the background color to a lighter yellow.
	Message = re.sub(r"\[\[(104|BGBRIGHTBLUE|BGLIGHTBLUE)\]\]", "\u001b[104m", Message) # 104: Sets the background color to a lighter blue.
	Message = re.sub(r"\[\[(105|BGBRIGHTMAGENTA|BGLIGHTMAGENTA|BGBRIGHTPURPLE|BGLIGHTPURPLE)\]\]", "\u001b[105m", Message) # 105: Sets the background color to a lighter magenta.
	Message = re.sub(r"\[\[(106|BGBRIGHTCYAN|BGBRIGHTTURQUOISE|BGLIGHTCYAN|BGLIGHTTURQUOISE)\]\]", "\u001b[106m", Message) # 106: Sets the background color to a lighter cyan.
	Message = re.sub(r"\[\[(107|BGBRIGHTWHITE|BGLIGHTWHITE)\]\]", "\u001b[107m", Message) # 107: Sets the background color to a lighter white.
	print(f"{Message}\u001b[0m")

# ZPYPrint
ZPYPrint is a Python function that makes it easier to format and colorize console output in your Python scripts. It provides a simple, intuitive interface that allows you to add colors, background colors, and text formatting to your console output with just a few lines of code.

## 🩸 | Modules & Instalation

<details><summary>Imported Modules (1): re.</summary>(No instalation needed, it's built-in Python)</details>
- Import the ZPrint function or just copy it in your code!

```python
from zpyprint import ZPrint
```

## 🩸 | Usage of ZPYPrint

- In your ZPrint function, you can add text changers to print in any format to customize your printing in python easier!
- Text changers need to be between double brackets, for example: [[TEXTCHANGER]], from then it enables the text changer for the following text.

<p align = "center"><br><br>Example & Preview:<br><br>
<img src = "https://raw.githubusercontent.com/Blxxded/ZPYPrint/main/example_and_preview.png"></p>

<table>
	<thead>
		<tr>
			<th>Text Changer</th>
			<th>Description</th>
			<th>Toggle / Untoggle By</th>
		</tr>
	</thead>
	<tbody>
		<tr align = "center" id = "reset">
			<td>
				<b>RESET</b><br>
				DEFAULT<br>
				NORMAL<br>
				NOT<br>
				PRIMARY
			</td>
			<td>Disables every attribute</td>
			<td>🩸</td>
		</tr>
		<tr align = "center" id = "bold">
			<td>
				<b>BOLD</b><br>
				INCREASED
			</td>
			<td>Makes the text &quot;stronger&quot;</td>
			<td>
				<a href = "#notintensity">NOTBOLD</a>
			</td>
		</tr>
		<tr align = "center" id = "faint">
			<td>
				<b>FAINT</b><br>
				DECREASED
			</td>
			<td>Makes the text &quot;weaker&quot;</td>
			<td>
				<a href = "#notintensity">NOTFAINT</a>
			</td>
		</tr>
		<tr align = "center" id = "italic">
			<td>
				<b>ITALIC</b><br>
				CURSIVE
			</td>
			<td>Not widely supported! Curves the text. Sometimes treated as <a href = "#blink">BLINK</a> or <a href = "#invert">INVERT</a></td>
			<td>
				<a href = "#notitalic">NOTITALIC</a>
			</td>
		</tr>
		<tr align = "center" id = "underline">
			<td>
				<b>UNDERLINE</b><br>
				UNDERLINED
			</td>
			<td>Not widely supported! Underlines the text</td>
			<td>
				<a href = "#notunderline">NOTUNDERLINE</a>
			</td>
		</tr>
		<tr align = "center" id = "blink">
			<td>
				<b>BLINK</b><br>
				SLOWBLINK
			</td>
			<td>Blinks less than 150 times per minute</td>
			<td>
				<a href = "#notblink">NOTBLINK</a>
			</td>
		</tr>
		<tr align = "center" id = "fastblink">
			<td>
				<b>FASTBLINK</b><br>
				RAPIDBLINK
			</td>
			<td>Not widely supported! Blinks more than 150 times per minute</td>
			<td>
				<a href = "#notblink">NOTBLINK</a>
			</td>
		</tr>
		<tr align = "center" id = "reverse">
			<td>
				<b>REVERSE</b><br>
				INVERT<br>
				INVERTED<br>
				REVERSED
			</td>
			<td>Swap background and foreground colors</td>
			<td>
				<a href = "#notreverse">NOTREVERSE</a>
			</td>
		</tr>
		<tr align = "center" id = "hide">
			<td>
				<b>HIDE</b><br>
				CONCEAL<br>
				CONCEALED<br>
				HIDDEN
			</td>
			<td>Not widely supported! Hides the text</td>
			<td>
				<a href = "#notreverse">NOTHIDE</a>
			</td>
		</tr>
		<tr align = "center" id = "strike">
			<td>
				<b>STRIKE</b><br>
				CROSSED<br>
				CROSSEDOUT<br>
				STRIKED
			</td>
			<td>Makes the text legible but marked as if for deletion</td>
			<td>
				<a href = "#notstrike">NOTSTRIKE</a>
			</td>
		</tr>
		<tr align = "center" id = "fraktur">
			<td>
				<b>FRAKTUR</b><br>
				BLACKLETTER<br>
				GOTHIC
			</td>
			<td>Rarely supported! The text has a calligraphic hand style.</td>
			<td>
				<a href = "#notitalic">NOTFRAKTUR</a>
			</td>
		</tr>
		<tr align = "center" id = "doubleunderline">
			<td>
				<b>DOUBLEUNDERLINE</b><br>
				DOUBLEUNDERLINED
			</td>
			<td>Double-underlines the text BUT disables <a href = "#bold">BOLD</a> intensity on several terminals</td>
			<td>
				<a href = "#notunderline">NOTUNDERLINE</a>
			</td>
		</tr>
		<tr align = "center" id = "notintensity">
			<td>
				<b>NOTINTENSITY</b><br>
				NOTBOLD<br>
				NOTDECREASED<br>
				NOTFAINT<br>
				NOTINCREASED
			</td>
			<td>Disables <a href = "#bold">BOLD</a> and <a href = "#faint">FAINT</a>. Color changes where intensity is implemented</td>
			<td>
				<a href = "#bold">BOLD</a><br>
				<a href = "#faint">FAINT</a>
			</td>
		</tr>
		<tr align = "center" id = "notitalic">
			<td>
				<b>NOTITALIC</b><br>
				NOTBLACKLETTER<br>
				NOTCURSIVE<br>
				NOTFRAKTUR<br>
				NOTGOTHIC
			</td>
			<td>Rarely supported! Stops <a href = "#italic">ITALIC</a> and <a href = "#fraktur">FRAKTUR</a></td>
			<td>
				<a href = "#fraktur">FRAKTUR</a><br>
				<a href = "#italic">ITALIC</a>
			</td>
		</tr>
		<tr align = "center" id = "notunderline">
			<td>
				<b>NOTUNDERLINE</b><br>
				NOTUNDERLINED
			</td>
			<td>Disables singly or doubly underlined</td>
			<td>
				<a href = "#doubleunderline">DOUBLEUNDERLINE</a><br>
				<a href = "#underline">UNDERLINE</a>
			</td>
		</tr>
		<tr align = "center" id = "notblink">
			<td>
				<b>NOTBLINK</b><br>
				NOTSLOWBLINK<br>
				NOTFASTBLINK<br>
				NOTRAPIDBLINK
			</td>
			<td>Stop both types of blinking</td>
			<td>
				<a href = "#blink">BLINK</a><br>
				<a href = "#fastblink">FASTBLINK</a>
			</td>
		</tr>
		<tr align = "center" id = "proportionalspacing">
			<td>
				<b>PROPORTIONALSPACING</b><br>
				SPACING
			</td>
			<td>Not known to be used on terminals! Gives a proportional spacing to the text</td>
			<td>
				<a href = "#proportionalspacing">NOTPROPORTIONALSPACING</a>
			</td>
		</tr>
		<tr align = "center" id = "notreverse">
			<td>
				<b>NOTREVERSE</b><br>
				NOTINVERT<br>
				NOTINVERTED<br>
				NOTREVERSED
			</td>
			<td>Undoes swapped colors</td>
			<td>
				<a href = "#reverse">REVERSE</a>
			</td>
		</tr>
		<tr align = "center" id = "nothide">
			<td>
				<b>NOTHIDE</b><br>
				NOTCONCEAL<br>
				NOTCONCEALED<br>
				NOTHIDDEN<br>
				REVEAL<br>
				REVEALED<br>
				SHOW<br>
				SHOWN
			</td>
			<td>Not widely supported! Reveals the text</td>
			<td>
				<a href = "#hide">HIDE</a>
			</td>
		</tr>
		<tr align = "center" id = "notstrike">
			<td>
				<b>NOTSTRIKE</b><br>
				NOTCROSSED<br>
				NOTCROSSEDOUT<br>
				NOTSTRIKED
			</td>
			<td>Makes the text not crossed</td>
			<td>
				<a href = "#strike">STRIKE</a>
			</td>
		</tr>
		<tr align = "center" id = "black">
			<td>
				<b>BLACK</b>
			</td>
			<td>Sets the foreground color to black</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "red">
			<td>
				<b>RED</b>
			</td>
			<td>Sets the foreground color to red</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "green">
			<td>
				<b>GREEN</b>
			</td>
			<td>Sets the foreground color to green</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "yellow">
			<td>
				<b>YELLOW</b>
			</td>
			<td>Sets the foreground color to yellow</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "blue">
			<td>
				<b>BLUE</b>
			</td>
			<td>Sets the foreground color to blue</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "magenta">
			<td>
				<b>MAGENTA</b><br>
				PURPLE
			</td>
			<td>Sets the foreground color to magenta</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "cyan">
			<td>
				<b>CYAN</b><br>
				TURQUOISE
			</td>
			<td>Sets the foreground color to cyan</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "white">
			<td>
				<b>WHITE</b>
			</td>
			<td>Sets the foreground color to white</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "defaultfg">
			<td>
				<b>DEFAULTFG</b><br>
				DEFAULTFOREGROUND
			</td>
			<td>Sets the foreground color to the default value</td>
			<td>🩸</td>
		</tr>
		<tr align = "center" id = "bgblack">
			<td>
				<b>BGBLACK</b>
			</td>
			<td>Sets the background color to black</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgred">
			<td>
				<b>BGRED</b>
			</td>
			<td>Sets the background color to red</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bggreen">
			<td>
				<b>BGGREEN</b>
			</td>
			<td>Sets the background color to green</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgyellow">
			<td>
				<b>BGYELLOW</b>
			</td>
			<td>Sets the background color to yellow</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgblue">
			<td>
				<b>BGBLUE</b>
			</td>
			<td>Sets the background color to blue</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgmagenta">
			<td>
				<b>BGMAGENTA</b><br>
				BGPURPLE
			</td>
			<td>Sets the background color to magenta</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgcyan">
			<td>
				<b>BGCYAN</b><br>
				BGTURQUOISE
			</td>
			<td>Sets the background color to cyan</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgwhite">
			<td>
				<b>BGWHITE</b>
			</td>
			<td>Sets the background color to white</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "defaultbg">
			<td>
				<b>DEFAULTBG</b><br>
				DEFAULTBACKGROUND
			</td>
			<td>Sets the background color to the default value</td>
			<td>🩸</td>
		</tr>
		<tr align = "center" id = "notproportionalspacing">
			<td>
				<b>NOTPROPORTIONALSPACING</b><br>
				NOTSPACING
			</td>
			<td>Not known to be used on terminals! Disables the proportional spacing to the text</td>
			<td>
				<a href = "#proportionalspacing">PROPORTIONALSPACING</a>
			</td>
		</tr>
		<tr align = "center" id = "framed">
			<td>
				<b>FRAMED</b>
			</td>
			<td>Frames the text</td>
			<td>
				<a href = "#notencircled">NOTFRAMED</a>
			</td>
		</tr>
		<tr align = "center" id = "encircled">
			<td>
				<b>ENCIRCLED</b>
			</td>
			<td>Encircles the text</td>
			<td>
				<a href = "#notencircled">NOTENCIRCLED</a>
			</td>
		</tr>
		<tr align = "center" id = "overline">
			<td>
				<b>OVERLINE</b><br>
				OVERLINED
			</td>
			<td>Overlines the text</td>
			<td>
				<a href = "#notoverline">NOTOVERLINE</a>
			</td>
		</tr>
		<tr align = "center" id = "notencircled">
			<td>
				<b>NOTENCIRCLED</b>
				<b>NOTFRAMED</b>
			</td>
			<td>Stops both encircled and framed attributes</td>
			<td>
				<a href = "#encircled">ENCIRCLED</a>
				<a href = "#framed">FRAMED</a>
			</td>
		</tr>
		<tr align = "center" id = "notoverline">
			<td>
				<b>NOTOVERLINE</b><br>
				NOTOVERLINED
			</td>
			<td>Stops overlining the text</td>
			<td>
				<a href = "#overline">OVERLINE</a>
			</td>
		</tr>
		<tr align = "center" id = "gray">
			<td>
				<b>GRAY</b><br>
				BRIGHTBLACK
				LIGHTBLACK
			</td>
			<td>Sets the foreground color to gray</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "brightred">
			<td>
				<b>BRIGHTRED</b><br>
				LIGHTRED
			</td>
			<td>Sets the foreground color to a lighter red</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "brightgreen">
			<td>
				<b>BRIGHTGREEN</b><br>
				LIGHTGREEN
			</td>
			<td>Sets the foreground color to a lighter green</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "brightyellow">
			<td>
				<b>BRIGHTYELLOW</b><br>
				LIGHTYELLOW
			</td>
			<td>Sets the foreground color to a lighter yellow</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "brightblue">
			<td>
				<b>BRIGHTBLUE</b><br>
				LIGHTBLUE
			</td>
			<td>Sets the foreground color to a lighter blue</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "brightmagenta">
			<td>
				<b>BRIGHTMAGENTA</b><br>
				LIGHTMAGENTA<br>
				BRIGHTPURPLE<br>
				LIGHTPURPLE
			</td>
			<td>Sets the foreground color to a lighter magenta</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "brightcyan">
			<td>
				<b>BRIGHTCYAN</b><br>
				LIGHTCYAN<br>
				BRIGHTTURQUOISE<br>
				LIGHTTURQUOISE
			</td>
			<td>Sets the foreground color to a lighter cyan</td>
		</tr>
		<tr align = "center" id = "brightwhite">
			<td>
				<b>BRIGHTWHITE</b><br>
				LIGHTWHITE
			</td>
			<td>Sets the foreground color to a lighter white</td>
			<td>
				<a href = "#defaultfg">DEFAULTFG</a>
			</td>
		</tr>
		<tr align = "center" id = "bggray">
			<td>
				<b>BGGRAY</b><br>
				BGBRIGHTBLACK<br>
				BGLIGHTBLACK
			</td>
			<td>Sets the background color to a lighter gray</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightred">
			<td>
				<b>BGBRIGHTRED</b><br>
				BGLIGHTRED
			</td>
			<td>Sets the background color to a lighter red</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightgreen">
			<td>
				<b>BGBRIGHTGREEN</b><br>
				BGLIGHTGREEN
			</td>
			<td>Sets the background color to a lighter green</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightyellow">
			<td>
				<b>BGBRIGHTYELLOW</b><br>
				BGLIGHTYELLOW
			</td>
			<td>Sets the background color to a lighter yellow</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightblue">
			<td>
				<b>BGBRIGHTBLUE</b><br>
				BGLIGHTBLUE
			</td>
			<td>Sets the background color to a lighter blue</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightmagenta">
			<td>
				<b>BGBRIGHTMAGENTA</b><br>
				BGLIGHTMAGENTA<br>
				BGBRIGHTPURPLE<br>
				BGLIGHTPURPLE
			</td>
			<td>Sets the background color to a lighter magenta</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightcyan">
			<td>
				<b>BGBRIGHTCYAN</b><br>
				BGLIGHTCYAN<br>
				BGBRIGHTTURQUOISE<br>
				BGLIGHTTURQUOISE
			</td>
			<td>Sets the background color to a lighter cyan</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
		<tr align = "center" id = "bgbrightwhite">
			<td>
				<b>BGBRIGHTWHITE</b><br>
				BGLIGHTWHITE
			</td>
			<td>Sets the background color to a lighter white</td>
			<td>
				<a href = "#defaultbg">DEFAULTBG</a>
			</td>
		</tr>
	</tbody>
</table>

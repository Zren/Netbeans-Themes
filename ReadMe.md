===============
Netbeans Themes
===============

Here are some themes specifically designed for Java source code which are based off those found at http://eclipsecolorthemes.org/.


### Intalling

Go to `Tools > Options` and select the Font's & Colors section. Then click Import at the bottom left and select the downloaded zip file. Click the checkbox next to All, and press OK. Netbeans will restart (or just quit I've found). The `Editor > Other` section when importing is there in order to select the theme you just installed.

### All-in-1 Bundle

Below is a download link that will contain the majority of the themes on this repository in a single zip for you to install.

**[Download All Themes](https://github.com/downloads/Zren/Netbeans-Themes/Netbean%20Themes.zip)**


### Creating New Themes

Clone this repo with `git clone git://github.com/Zren/Netbeans-Themes.git` then `cd Netbeans-Themes`

Create a new branch based off the master branch with `git branch ThemeName`. Then checkout that branch with `git checkout ThemeName`. Each theme has it's own branch based off the master branch so any changes to it will chain down to your theme when Netbeans adds new configurable values. **Do not** push from a theme branch to the master. Always edit the master branch when editing files outside `src/`.

Go to the `src/` folder and edit the files within. They are renamed and all in a single folder for ease of use when editing. The .nbattr files will be auto generated. Right now, the scripts only supports the files for x-java and the base theme colors.

To build the theme, go into the `tools/` folder and run `make.bat`. Which will build a zip bundle in an untracked folder called Themes.

### Theme Editing

While colours are stored in hexidecimal ARGB format, alpha is not checked/used for assumably all configurable values.


### Useful Links

*   A theme builder for PHP/HTML/Javascript/CSS: http://www.wordfraud.net/themebuilder/





======
Themes
======

## Monokai

[Source](https://github.com/Zren/Netbeans-Themes/tree/Monokai/src) |
[Download](https://github.com/downloads/Zren/Netbeans-Themes/Monokai.zip) |
Based on: http://eclipsecolorthemes.org/?view=theme&id=52

#### Theme Links: ####

*   Other Adaptions:
    *   http://codesleepshred.com/dark-netbeans-themes-oblivion-revival-and-monokai/


## Retta

[Source](https://github.com/Zren/Netbeans-Themes/tree/Retta/src) |
[Download](https://github.com/downloads/Zren/Netbeans-Themes/Retta.zip) |
Based on: http://eclipsecolorthemes.org/?view=theme&id=1004

#### Differences: ####

    occurrenceIndication: #5E5C56 -> #333
 
 
## Sunburst

[Source](https://github.com/Zren/Netbeans-Themes/tree/Sunburst/src) |
[Download](https://github.com/downloads/Zren/Netbeans-Themes/Sunburst.zip) |
Based on: http://eclipsecolorthemes.org/?view=theme&id=383

#### Theme Links: ####

*   Other Adaptions:
    *   http://purplerockscissors.com/uncategorized/textmate-sunburst-theme-netbeans/

    
## Vibrant Ink

[Source](https://github.com/Zren/Netbeans-Themes/tree/VibrantInk/src) |
[Download](https://github.com/downloads/Zren/Netbeans-Themes/VibrantInk.zip) |
Based on: http://eclipsecolorthemes.org/?view=theme&id=3

#### Differences: ####

    annotation: n/a -> #fff
    findScope: #191919 -> #414C3B (selectionBackground)
    occurrenceIndication: (bg) #616161 -> #414C3B (selection bg) + #fff (selection fg)
    
    
## Zenburn

[Source](https://github.com/Zren/Netbeans-Themes/tree/Zenburn/src) |
[Download](https://github.com/downloads/Zren/Netbeans-Themes/Zenburn.zip) |
Based on: http://eclipsecolorthemes.org/?view=theme&id=2

#### Differences: ####

    enum: n/a -> #fff

#### Theme Links: ####

*   Theme wiki: http://slinky.imukuppi.org/zenburnpage/
*   Other Adaptions:
    *   https://github.com/elimc/Zenburn2012
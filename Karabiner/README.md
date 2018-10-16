# karabiner_config_generator.py

Create a Karabiner-Elements config file that handles Colemak Extend keyboard
mappings on macOS.

Tested on Karabiner-Elements v12, macOS Sierra, High Sierra, and Mojave.

- homepage: [https://github.com/mattmc3/colemak-tools](https://github.com/mattmc3/colemak-tools)
- license: MIT
- author: mattmc3

Extend is described [here][extend]. Karabiner-Elements is available [here][karabiner].

## TLDR;

Don't know Python and don't want to mess with a script? Already have
Karabiner-Elements and just looking to get started quickly with Extend?
No problem. Open Terminal on your Mac and do this:

```bash
mkdir -p ~/.config/karabiner/assets/complex_modifications
curl -fsSL "https://raw.githubusercontent.com/mattmc3/colemak-tools/master/Karabiner/generated/extend.json" > ~/.config/karabiner/assets/complex_modifications/extend.json
```

## How to run script

From a bash Terminal:

```bash
mkdir -p ~/.config/karabiner/assets/complex_modifications
python3 ./karabiner_config_generator.py extend.yaml > ~/.config/karabiner/assets/complex_modifications/extend.json
```

## How to add Extend

Install and run Karabiner-Elements. From Karabiner-Elements on your menu bar
chose Preferences... Go to the "Complex Modifications" tab, and press the
"Add rule" button. "Extend Mode" should show up if you have properly generated
the script.

## How to customize

Make a copy of Extend.yaml and change its contents to suit your needs. No need
to stick with the defaults if you don't want to, and no need to hack on the
Python if that's not your thing. The mappings are driven off of whatever is in
the YAML file.

## Note about Colemak-DH

__Q:__ *I see that this script appears to use vanilla Colemak? What about Colemak-DH?*

__A:__ The YAML settings file supports a keyboard property that understands
Colemak, Colemak-DH, and QWERTY. At the end of the day Karabiner uses QWERTY
positions to set its key maps, so you can do your own mappings using whichever
suits you.

## Other notes

Extend was designed more with Win/Linux in mind, so keys like Insert, Menu, and
Print Screen (PrtScn) aren't very meaningful on the Mac. CTRL isn't as useful as
Command, and there is not a common shortcut for Browser Favorites across web
browsers. None of the special F1-F12 keys are remapped because Macs already
handle that. In other words, as great as Extend is, it is somewhat foreign on a
Mac. This is why this script exists - I give you the closest defaults, but you
should feel empowered to customize any way you want!

## Reference

Karabiner uses QWERTY keys for mapping:

```text
[TAB]      [Q] [W] [E] [R] [T]     [Y] [U] [I] [O] [P] [{] [}] [\] [BKSPC]
[CAPS/EXT]  [A] [S] [D] [F] [G]     [H] [J] [K] [L] [;] [']        [RETURN]
[SHIFT]      [Z] [X] [C] [V] [B]     [N] [M] [,] [.] [/]           [SHIFT]
```

Colemak is how we see the world when making mappings in the python script:

```text
[TAB]      [Q] [W] [F] [P] [G]     [J] [L] [U] [Y] [;] [{] [}] [\] [BKSPC]
[CAPS/EXT]  [A] [R] [S] [T] [D]     [H] [N] [E] [I] [O] [']        [RETURN]
[SHIFT]      [Z] [X] [C] [V] [B]     [K] [M] [,] [.] [/]           [SHIFT]
```

This is Extend:
![extend-image][extend-image]

### Colemak Extend Mappings

| Location | Colemak | QWERTY |  Category  | Extend Mapping                |
|:--------:|:-------:|:------:|:----------:|:------------------------------|
|  :one:   | F1-F12  |        |  :sound:   | Unchanged :curly_loop:        |
|  :two:   |    `    |        | :computer: | User Custom (not set)         |
|  :two:   |   1-9   |        |   :1234:   | F1-F9                         |
|  :two:   |  0,-,=  |        |   :1234:   | F10-F12                       |
|  :two:   | DELETE  |        |            | Unchanged :curly_loop:        |
| :three:  |    Q    |        | :computer: | Escape                        |
| :three:  |    W    |        |  :mouse:   | Mouse wheel scroll up         |
| :three:  |    F    |   E    |  :sound:   | Browser Back                  |
| :three:  |    P    |   R    |  :sound:   | Browser Forward               |
| :three:  |    G    |   T    |  :mouse:   | Mouse move up                 |
| :three:  |    J    |   Y    |  :rocket:  | Page Up                       |
| :three:  |    L    |   U    |  :rocket:  | Home                          |
| :three:  |    U    |   I    |  :rocket:  | Up Arrow                      |
| :three:  |    Y    |   O    |  :rocket:  | End                           |
| :three:  |    ;    |   P    | :computer: | Forward Delete                |
| :three:  |    [    |        | :computer: | Escape                        |
| :three:  |    ]    |        | :computer: | Insert :skull:                |
| :three:  |    \    |        |  :mouse:   | Horizontal Scroll Left        |
|  :four:  |  CAPS   |        |  :rocket:  | :tada: Extend Modifier :tada: |
|  :four:  |    A    |        | :computer: | Option (ALT)                  |
|  :four:  |    R    |   S    |  :mouse:   | Mouse wheel scroll down       |
|  :four:  |    S    |   D    | :computer: | Shift                         |
|  :four:  |    T    |   F    | :computer: | Command :curly_loop:          |
|  :four:  |    D    |   G    |  :mouse:   | Mouse move down               |
|  :four:  |    H    |        |  :rocket:  | Page Down                     |
|  :four:  |    N    |   J    |  :rocket:  | Left arrow                    |
|  :four:  |    E    |   K    |  :rocket:  | Down arrow                    |
|  :four:  |    I    |   U    |  :rocket:  | Right arrow                   |
|  :four:  |    O    |   ;    | :computer: | Delete                        |
|  :four:  |    '    |        | :computer: | Menu :skull:                  |
|  :four:  | RETURN  |        | :computer: | Screenshot :curly_loop:       |
|  :five:  |    \    |        |  :mouse:   | Horizontal Scroll Left        |
|  :five:  |    Z    |        |  :sound:   | CMD-Z :curly_loop:            |
|  :five:  |    X    |        |  :sound:   | CMD-X :curly_loop:            |
|  :five:  |    C    |        |  :sound:   | CMD-C :curly_loop:            |
|  :five:  |    V    |        |  :sound:   | CMD-V :curly_loop:            |
|  :five:  |    B    |        |  :mouse:   | Mouse left-click              |
|  :five:  |    K    |   N    |  :mouse:   | Mouse middle-click            |
|  :five:  |    M    |        |  :mouse:   | Mouse right-click             |
|  :five:  |    ,    |        |  :mouse:   | Mouse move left               |
|  :five:  |    .    |        |  :mouse:   | Mouse move right              |
|  :five:  |    /    |        |  :mouse:   | Horizontal scroll right       |

- :sound: : Multimedia
- :computer: : System/Misc
- :mouse: : Mouse
- :rocket: : Navigation
- :curly_loop: : macOS equivalent, but technically different from Extend docs
- :skull: : Deadkey on macOS
- :tada: : Extend Modifier

[homepage]: https://github.com/mattmc3/colemak-tools
[extend]: https://forum.colemak.com/topic/2014-extend-extra-extreme/
[karabiner]: https://pqrs.org/osx/karabiner/
[extend-image]: https://www.dropbox.com/s/gks7fzzhw6y7o3p/Extend-ANSI-NoWi-Linux_90d.png?raw=1

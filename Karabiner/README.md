# gen_extend_config.py

Create a Karabiner-Elements config file that handles Colemak Extend keyboard
mappings on macOS.

Tested on Karabiner-Elements v12, macOS Sierra, High Sierra, and Mojave.

- homepage: [https://github.com/mattmc3/colemak-tools](https://github.com/mattmc3/colemak-tools)
- license: MIT
- author: mattmc3

Extend is described [here][extend]. Karabiner-Elements is available [here][karabiner].

## How to run

From a bash Terminal:

```bash
mkdir -p ~/.config/karabiner/assets/complex_modifications
python3 ./gen_extend_config.py > ~/.config/karabiner/assets/complex_modifications/extend.json
```

## How to customize

Change the contents of main() to whatever you want. No need to stick with the
defaults if you don't want to. For example, Opt-Left/Right move forward and
backward over words - mapping those may be way more useful than the mouse movements.

## Note about Mod-DH

__Q:__ *I see that this script appears to use vanilla Colemak? What about mod-DH?*

__A:__ It doesn't matter. Karabiner uses QWERTY positions to set key maps, and
mod-DH doesn't change placement of Extend keys since they are positional, so no
need to worry. Just be sure when you make your own custom mappings, you are
looking at the vanilla Colemak position when making an assignment.

## Other notes

Extend was designed more with Win/Linux in mind, so keys like Insert, Menu, and
Print Screen (PrtScn) aren't very meaningful on the Mac. CTRL isn't as useful as
Command, and there is not a common shortcut for Browser Favorites across web
browsers. None of the special F1-F12 keys are remapped because Macs already
handle that. In other words, as great as Extend is, it is somewhat foreign on a
Mac. This is why this script exists - I give you the closest defaults, but you
should feel empowered to customize away if you want!

## Reference

Karabiner uses QWERTY keys for mapping:

```text
[TAB]      [Q] [W] [E] [R] [T]     [Y] [U] [I] [O] [P] [{] [}] [\] [BKSPC]
[CAPS/EXT]  [A] [S] [D] [F] [G]     [H] [J] [K] [L] [;] [']        [RETURN]
[SHIFT]      [Z] [X] [C] [V] [B]     [N] [M] [,] [.] [/]           [SHIFT]
```

Colemak is how we see the world when mapping:

```text
[TAB]      [Q] [W] [F] [P] [G]     [J] [L] [U] [Y] [;] [{] [}] [\] [BKSPC]
[CAPS/EXT]  [A] [R] [S] [T] [D]     [H] [N] [E] [I] [O] [']        [RETURN]
[SHIFT]      [Z] [X] [C] [V] [B]     [K] [M] [,] [.] [/]           [SHIFT]
```

### Colemak Extend Mappings

![extend-image][extend-image]

| Location | Colemak | QWERTY |  Category  | Extend Mapping                |
|:--------:|:-------:|:------:|:----------:|:------------------------------|
|   :1:    | F1-F12  |        |  :sound:   | Unchanged :curly_loop:        |
|   :2:    |    `    |        | :computer: | User Custom (not set)         |
|   :2:    |   1-9   |        |   :1234:   | F1-F9                         |
|   :2:    |  0,-,=  |        |   :1234:   | F10-F12                       |
|   :2:    | DELETE  |        |            | Unchanged :curly_loop:        |
|   :3:    |    Q    |        | :computer: | Escape                        |
|   :3:    |    W    |        |  :mouse:   | Mouse wheel scroll up         |
|   :3:    |    F    |   E    |  :sound:   | Browser Back                  |
|   :3:    |    P    |   R    |  :sound:   | Browser Forward               |
|   :3:    |    G    |   T    |  :mouse:   | Mouse move up                 |
|   :3:    |    J    |   Y    |  :rocket:  | Page Up                       |
|   :3:    |    L    |   U    |  :rocket:  | Home                          |
|   :3:    |    U    |   I    |  :rocket:  | Up Arrow                      |
|   :3:    |    Y    |   O    |  :rocket:  | End                           |
|   :3:    |    ;    |   P    | :computer: | Forward Delete                |
|   :3:    |    [    |        | :computer: | Escape                        |
|   :3:    |    ]    |        | :computer: | Insert :skull:                |
|   :3:    |    \    |        |  :mouse:   | Horizontal Scroll Left        |
|   :4:    |  CAPS   |        |  :rocket:  | :tada: Extend Modifier :tada: |
|   :4:    |    A    |        | :computer: | Option (ALT)                  |
|   :4:    |    R    |   S    |  :mouse:   | Mouse wheel scroll down       |
|   :4:    |    S    |   D    | :computer: | Shift                         |
|   :4:    |    T    |   F    | :computer: | Command :curly_loop:          |
|   :4:    |    D    |   G    |  :mouse:   | Mouse move down               |
|   :4:    |    H    |        |  :rocket:  | Page Down                     |
|   :4:    |    N    |   J    |  :rocket:  | Left arrow                    |
|   :4:    |    E    |   K    |  :rocket:  | Down arrow                    |
|   :4:    |    I    |   U    |  :rocket:  | Right arrow                   |
|   :4:    |    O    |   ;    | :computer: | Delete                        |
|   :4:    |    '    |        | :computer: | Menu :skull:                  |
|   :4:    | RETURN  |        | :computer: | Screenshot :curly_loop:       |
|   :5:    |    \    |        |  :mouse:   | Horizontal Scroll Left        |
|   :5:    |    Z    |        |  :sound:   | CMD-Z :curly_loop:            |
|   :5:    |    X    |        |  :sound:   | CMD-X :curly_loop:            |
|   :5:    |    C    |        |  :sound:   | CMD-C :curly_loop:            |
|   :5:    |    V    |        |  :sound:   | CMD-V :curly_loop:            |
|   :5:    |    B    |        |  :mouse:   | Mouse left-click              |
|   :5:    |    K    |   N    |  :mouse:   | Mouse middle-click            |
|   :5:    |    M    |        |  :mouse:   | Mouse right-click             |
|   :5:    |    ,    |        |  :mouse:   | Mouse move left               |
|   :5:    |    .    |        |  :mouse:   | Mouse move right              |
|   :5:    |    /    |        |  :mouse:   | Horizontal scroll right       |

- :sound: : Multimedia
- :computer: : System/Misc
- :mouse: : Mouse
- :rocket: : Navigation
- :curly_loop: : macOS equivalent, but technically different from Extend docs
- :skull: : Deadkey on macOS
- :tada: : Extend Modifier

![extend][extend]

[homepage]: https://github.com/mattmc3/colemak-tools
[extend]: https://forum.colemak.com/topic/2014-extend-extra-extreme/
[karabiner]: https://pqrs.org/osx/karabiner/
[extend-image]: https://www.dropbox.com/s/gks7fzzhw6y7o3p/Extend-ANSI-NoWi-Linux_90d.png?raw=1

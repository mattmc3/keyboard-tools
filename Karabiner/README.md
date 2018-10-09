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

Colemak Extend (credit DreymaR):

```text
+------+------+------+------+------+------+------+------+------+------+------+------+------+
|Esc + |F1 <> |F2 << |F3 >> |F4 <> |F5 <> |F6 << |F7 >> |F8 <> |F9 <> |F10<> |F11<> |F12<> |
|      | Pause| Rew  | Fwd  | Eject| Refr | Bri- | Bri+ | Sleep| WWW  | Mail | App1 | App2 |
| Caps | Play | Prev | Next | Stop | Mute | Vol- | Vol+ | Media| Home | Srch | File | Calc |
+======+======+======+======+======+======+======+======+======+======+======+======+======+
|` €€€ |1     |2     |3     |4     |5     |6     |7     |8     |9     |0     |-     |=     |
| Cust | F1   | F2   | F3   | F4   | F5   | F6   | F7   | F8   | F9   | F10  | F11  | F12  |
+------+------+------+------+------+------+------+------+------+------+------+------+------+
|Tab   |Q €€€ |W *** |F <<> |P <>> |G *** |J ### |L ### |U ### |Y ### |; €€€ |[ €€€ |] €€€ |
|      | Esc  | *WhUp| BrBck| BrFwd| *MUp | PgUp | Home | Up   | End  | Del  | Esc  | Ins  |
+------+------+------+------+------+------+------+------+------+------+------+------+------+
|Caps+ |A +++ |R *** |S +++ |T +++ |D *** |H ### |N ### |E ### |I ### |O €€€ |' €€€ |\ ><> |
| ++++ | Alt  | *WhDn| Shift| Ctrl | *MDn | PgDn | Left | Down | Right| Back | Menu | BrFav|
+------+------+------+------+------+------+------+------+------+------+------+------+------+
|_ *** |Z €€€ |X === |C === |V === |B *** |K *** |M *** |, *** |. *** |/ €€€ |Spc € |Entr€ |
| *MOn | Undo | Cut  | Copy | Paste| *Bt1 | *Bt2 | *Bt3 | *MLe | *MRi | Multi| Enter| PrtSc|
+------+------+------+------+------+------+------+------+------+------+------+-------------+
Legend: # Movement; + Modifiers; = GUI edit; * Mouse; <> MultiMedia; € Various commands.
```

[homepage]: https://github.com/mattmc3/colemak-tools
[extend]: https://forum.colemak.com/topic/2014-extend-extra-extreme/
[karabiner]: https://pqrs.org/osx/karabiner/

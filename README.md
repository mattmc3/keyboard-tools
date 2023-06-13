# keyboard-tools

This is a simple repo for me to aggregate all my Colemak and Keyboard resources.

![Colemak](https://colemak.com/wiki/images/e/ef/Colemak_fingers.png)

## Why?

Because I love to type with Colemak, and I want to have access to my tools
everywhere I compute.

Nothing's more frustrating than navigating all over the internet to get set up
on Colemak on a new machine, or having to figure out how to get productive
without administrative access. Also, when helping a new Colemak user, this
is where I want to send them for helpful advocacy and practice materials.

## CAPSLOCK to Backspace

On MacOS, you can remap CAPSLOCK to delete (backspace) with this command:

```shell
hidutil property --set '{"UserKeyMapping":[{"HIDKeyboardModifierMappingSrc":0x700000039,"HIDKeyboardModifierMappingDst":0x70000002A}]}'
```

To make sure it runs on startup, you can add that snippet to a shell script and then add a login hook like so:

```shell
sudo defaults write com.apple.loginwindow LoginHook ~/bin/colemak.sh
```

To remove login hooks, run:

```shell
sudo defaults delete com.apple.loginwindow LoginHook
```

More info [here](http://homeowmorphism.com/2017/05/27/Remap-CapsLock-Backspace-Sierra).

## Stuff in this repo

### AutoHotKey (Windows)

My AHK Colemak file for working on Windows machines is in this repo. Use
PortableApps.com to install AHK.

### Hammerspoon (macOS)

I use Hammerspoon to map F18/F19 to extend/hyper. The init.lua script is in this repo.

### Karabiner (macOS)

My old Karabiner scripts are in this repo. The main one of interest is the Python
script for creating a Karabiner-Elements json config.

## Handy links

More information about Colemak at [colemak.com][colemak].

### :white_check_mark: Downloads

- Download from [PortableApps.com][portable-apps]
  - gVim
  - AutoHotKey
- The PKL app from colemak.com is unmaintained, but DreymaR's is [better and
  includes Extend][pkl].

### :white_check_mark: Basics

- [colemak.com by Shai Coleman][colemak]
- [The Colemak forums][colemak-forum]
- [Colemak Subreddit][reddit]
- [Steam group][steam]
- [Discord][discord]
- [Logos and images][colemak-images]

### :white_check_mark: Learning

- [keybr][keybr]
- [Learning with Tarmak][tarmak]
- [Training with Amphetype(++)][amphetype]
- [Viper's Speedtyping Guide][viper-speedtyping]
- [Typing Test][typing-test]

### :white_check_mark: Advanced

- [DreymaR's Big Bag Of Keyboard Tricks][dreymar-bbot]
- [DreymaR's Extend Extra Extreme][dreymar-extend]
- Mod [Colemak-DH][colemak-mod-dh]
- Mod [Extend][colemak-mod-extend]

### :white_check_mark: Advocacy

- [Keyboard layout analyzer][layout-analyzer]
- [Carpalx Colemak results][carpalx]
- [Keyboard Heatmaps][heatmap]

### :white_check_mark: Testimonials / Articles

- [mctape](https://mctape.wordpress.com/2012/02/11/a-comprehensive-comparison/)
- arstechnica did an article in 2014. [Part 1][ars-dvorak1],
  [part 2][ars-dvorak2], [the finale][ars-dvorak-finale], and
  [reader reactions][ars-dvorak-reactions].
- NPR [wrote about Colemak too][npr]

### :white_check_mark: Topic: vim

- [Shai posted his vimrc here][vimrc], but mine is in my [dotfiles repo][dotfiles].
- [Ryan Heise][ryanheise] had a pretty cool idea of NEST remappings for vim arrows
- I prefer [JENK][jenk] for my .vimrc

### :white_check_mark: Games

- [ztype]

### :white_check_mark: Sister communities

- [dvzine][dvzine]

###  :white_check_mark: History

- [Smithsonian - fact fiction](https://www.smithsonianmag.com/arts-culture/fact-of-fiction-the-legend-of-the-qwerty-keyboard-49863249/)
- [The Atlantic - lies you've been told](https://www.theatlantic.com/technology/archive/2013/05/the-lies-youve-been-told-about-the-origin-of-the-qwerty-keyboard/275537/)
- [BBC - how QWERTY became popular](https://www.bbc.com/news/business-47460499)

## TLDR;

QWERTY heatmap:

![qwerty-heatmap]

Colemak heatmap:

![colemak-heatmap]

[amphetype]: https://forum.colemak.com/topic/2201-training-with-amphetype/
[ars-dvorak-finale]: https://arstechnica.com/gadgets/2014/04/my-quest-to-learn-the-dvorak-keyboard-layout-the-grand-finale/
[ars-dvorak-reactions]: https://arstechnica.com/gadgets/2014/04/readers-react-to-my-quest-to-learn-the-dvorak-keyboard-layout/
[ars-dvorak1]: https://arstechnica.com/gadgets/2014/03/my-quest-to-learn-the-dvorak-keyboard-layout-part-1/
[ars-dvorak2]: https://arstechnica.com/gadgets/2014/04/my-quest-to-learn-the-dvorak-keyboard-layout-part-2/
[autohotkey]: https://github.com/Lexikos/AutoHotkey_L/releases
[carpalx]: http://mkweb.bcgsc.ca/carpalx/?colemak
[colemak-forum]: https://forum.colemak.com/
[colemak-heatmap]: https://github.com/mattmc3/keyboard-tools/blob/resources/img/colemak_heatmap.jpg?raw=true
[colemak-images]: https://drive.google.com/drive/folders/11xPjOWtrL47PzEu5fTaQGQsRGxaYbSAi?usp=sharing
[colemak]: https://colemak.com
[colemak-mod-dh]: https://colemakmods.github.io/mod-dh/
[colemak-mod-extend]: https://colemakmods.github.io/ergonomic-mods/extend.html
[discord]: https://discord.gg/sMNhBUP
[dotfiles]: https://github.com/mattmc3/dotfiles
[dreymar-bbot]: https://forum.colemak.com/topic/2315-dreymars-big-bag-of-keyboard-tricks-main-topic/
[dreymar-extend]: https://forum.colemak.com/topic/2014-extend-extra-extreme/
[dvzine]: http://www.dvzine.org/zine/index.html
[heatmap]: https://www.patrick-wied.at/projects/heatmap-keyboard/
[jenk]: https://docs.google.com/spreadsheets/d/19l4rQdYZfqpMtdTjvCrYLF2z9OsAqahhPunnw7I831s/edit#gid=589401919
[keybr]: https://www.keybr.com/
[layout-analyzer]: http://patorjk.com/keyboard-layout-analyzer/#/main
[npr]: https://www.npr.org/sections/alltechconsidered/2016/09/05/492413673/qwerty-traveled-from-typewriter-to-iphone-but-alternative-keyboards-do-exist
[pkl]: https://github.com/DreymaR/BigBagKbdTrixPKL
[portable-apps]: https://portableapps.com/download
[qwerty-heatmap]: https://github.com/mattmc3/keyboard-tools/blob/resources/img/qwerty_heatmap.jpg?raw=true
[reddit]: https://www.reddit.com/r/Colemak/
[ryanheise]: https://www.ryanheise.com/colemak/
[steam]: https://steamcommunity.com/groups/colemak
[tarmak]: https://forum.colemak.com/topic/1858-learn-colemak-in-steps-with-the-tarmak-layouts/
[typing-test]: https://www.typingtest.com
[vimrc]: http://colemak.com/pub/vim/colemak.vim
[viper-speedtyping]: https://forum.colemak.com/topic/2455-vipers-speedtyping-guide/
[wikipedia]: https://en.wikipedia.org/wiki/Colemak
[ztype]: https://zty.pe

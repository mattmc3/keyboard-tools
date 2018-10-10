#!/usr/bin/env python

'''
Full docs: https://github.com/mattmc3/colemak-tools/tree/master/Karabiner
Description of Extend: https://forum.colemak.com/topic/2014-extend-extra-extreme/

To generate colemak_extend.json:
```bash
mkdir -p ./generated
python3 ./my_extend_config.py > ./generated/colemak_extend.json
```

To put colemak_extend.json into Karabiner-Elements config:
```
mkdir -p ~/.config/karabiner/assets/complex_modifications
python3 ./my_extend_config.py > ~/.config/karabiner/assets/complex_modifications/colemak_extend.json
```
'''

import json
from enum import Enum

NATURAL_SCROLLING_MODIFIER = -1
MOUSE_SCROLL_DISTANCE = 50
MOUSE_MOVE_DISTANCE = 1500
EXTEND_ENABLED_VAR = "extend_mode"

# change colemak to qwerty, which Karabiner requires
qwerty_map = dict(zip(list("fpgjluy;rstdneiok"), list("ertyuiopsdfgjkl;n")))

# https://github.com/tekezo/Karabiner-Elements/issues/925
karabiner_map = {
    "-": "hyphen",
    "=": "equal_sign",
    "[": "open_bracket",
    "]": "close_bracket",
    ";": "semicolon",
    "'": "quote",
    ".": "period",
    ",": "comma",
    "/": "slash",
    "\\": "backslash",
    "\\2": "non_us_backslash",  # backslash #2
    "`": "grave_accent_and_tilde",
    "space": "spacebar",
    "return": "return_or_enter",
    "esc": "escape",
    "delete": "delete_or_backspace",
}


class Direction():
    UP = 1
    DOWN = -1
    LEFT = -1
    RIGHT = 1


class MouseButton():
    LEFT = 1
    MIDDLE = 3
    RIGHT = 2


def to_karabiner_key(colemak_key):
    ''' turn a colemak key into the karabiner value '''
    # colemak -> qwerty -> karabiner
    colemak_key = str(colemak_key)
    if colemak_key in qwerty_map:
        colemak_key = qwerty_map[colemak_key]
    if colemak_key in karabiner_map:
        colemak_key = karabiner_map[colemak_key]
    return colemak_key


def to_list(thing):
    if not thing:
        return list()
    elif type(thing) is list or type(thing) is tuple:
        return list(thing)
    else:
        return list((thing,))


class ExtendBuilder():
    '''
    This class builds the json dict for the Karabiner-Elements implementation
    of Extend
    '''
    def __init__(self, title, description, ext_key='caps_lock', alone_action='escape'):
        # This config init sets a variable when CAPS LOCK is pressed and un-sets
        # it when released. This allows us to not treat CAPS like a modifier key.
        self.config = {'title': title,
                       'rules': [{'description': description,
                         'manipulators': [{'from': {'key_code': ext_key},
                           'to': [{'set_variable': {'name': EXTEND_ENABLED_VAR, 'value': 1}}],
                           'to_after_key_up': [{'set_variable': {'name': EXTEND_ENABLED_VAR, 'value': 0}}],
                           'to_if_alone': [{'key_code': alone_action}],
                           'type': 'basic'}]}]}

    def add_modifier_mapping(self, from_key, modifiers):
        ''' convenience method to make the karabiner json config for modifier+key press action '''
        self._add_mapping(self._get_key_map(from_key),
                          self._get_key_map(None, "to", to_list(modifiers)))

    def add_key_mapping(self, from_key, to_key, to_modifiers=()):
        ''' convenience method to make the karabiner json config for a key press action '''
        self._add_mapping(self._get_key_map(from_key),
                          self._get_key_map(to_key, "to", to_list(to_modifiers)))

    def add_mouse_button_mapping(self, from_key, button_num):
        ''' convenience method to make the karabiner json config for a mouse button click '''
        self._add_mapping(self._get_key_map(from_key),
                          {"pointing_button": "button" + str(button_num)})

    def add_mouse_move_mapping(self, from_key, axis, direction, distance=MOUSE_MOVE_DISTANCE):
        ''' convenience method to make the karabiner json config for a mouse movement '''
        if axis == "y":
            direction *= NATURAL_SCROLLING_MODIFIER
        self._add_mapping(self._get_key_map(from_key),
                          {"mouse_key": {axis: distance * direction}})

    def add_mouse_scroll_mapping(self, from_key, axis, direction, distance=MOUSE_SCROLL_DISTANCE):
        ''' convenience method to make the karabiner json config for a mouse scroll '''
        if axis == "y":
            direction *= NATURAL_SCROLLING_MODIFIER
        axis = "vertical_wheel" if axis == "y" else "horizontal_wheel"
        self._add_mapping(self._get_key_map(from_key),
                          {"mouse_key": {axis: distance * direction}})

    def _get_key_map(self, key, from_or_to="from", modifiers=(), optional_modifiers=("any",)):
        ''' make a karabiner dict describing the key press '''
        if not key and not modifiers:
            raise Exception("You gotta map something!")

        if not key and modifiers:
            return {'key_code': modifiers[0]}

        result = {}
        result['key_code'] = to_karabiner_key(key)
        # from
        if from_or_to == "from":
            mod_dict = {}
            if modifiers:
                mod_dict["mandatory"] = list(modifiers)
            if optional_modifiers:
                mod_dict["optional"] = list(optional_modifiers)
            if mod_dict:
                result['modifiers'] = mod_dict
        # to
        else:
            if modifiers:
                result['modifiers'] = list(modifiers)
        return result

    def _add_mapping(self, from_dict, to_dict):
        ''' convenience method to make the karabiner json config for from->to actions '''
        manipulator = {'type': 'basic',
                       'from': from_dict,
                       'to': [to_dict],
                       'conditions': [{'name': EXTEND_ENABLED_VAR, 'type': 'variable_if', 'value': 1}],
                      }
        self.config['rules'][0]['manipulators'].append(manipulator)


def dreymar_extend():
    # >1200 lines of Karabiner-Elements JSON to make Extend!? Pshaw. We can do
    # it in Python in a tiny fraction of that, *and* make it easy to customize
    # to boot. Win/win!
    extend = ExtendBuilder(
        'Colemak Extend (DreymaR version, Python Generated) - github.com/mattmc3/colemak-tools',
        'Extend Mode [Caps Lock as Trigger Key]'
    )

    # backtick is the user custom key
    # sample mapping for saving with Ext-` => ⌘-s
    # extend.add_key_mapping("`", "s", "left_command")

    # function row. Nope! Macs already handle FX keys.
    # Yea! CAPS LOCK is back so we can shout down internet trolls! #solved-it
    extend.add_key_mapping("esc", "caps_lock")

    ### number row ### nice for easy reach FX keys or small keyboards
    extend.add_key_mapping("1", "f1", "fn")
    extend.add_key_mapping("2", "f2", "fn")
    extend.add_key_mapping("3", "f3", "fn")
    extend.add_key_mapping("4", "f4", "fn")
    extend.add_key_mapping("5", "f5", "fn")
    extend.add_key_mapping("6", "f6", "fn")
    extend.add_key_mapping("7", "f7", "fn")
    extend.add_key_mapping("8", "f8", "fn")
    extend.add_key_mapping("9", "f9", "fn")
    extend.add_key_mapping("0", "f10", "fn")
    extend.add_key_mapping("-", "f11", "fn")
    extend.add_key_mapping("=", "f12", "fn")

    ### top row ###
    extend.add_key_mapping("q", "esc")
    extend.add_mouse_scroll_mapping("w", "y", Direction.UP)  # mouse scroll up
    extend.add_key_mapping("f", "[", "left_command")  # browser back
    extend.add_key_mapping("p", "]", "left_command")  # browser forward
    extend.add_mouse_move_mapping("g", "y", Direction.UP)  # mouse move up
    extend.add_key_mapping("j", "page_up")
    extend.add_key_mapping("l", "home")
    extend.add_key_mapping("u", "up_arrow")
    extend.add_key_mapping("y", "end")
    extend.add_key_mapping(";", "delete_forward")
    extend.add_key_mapping("[", "esc")
    extend.add_key_mapping("]", "insert")

    ### home row ###
    extend.add_modifier_mapping("a", "left_option")  # alt => ⌥ (option)
    extend.add_mouse_scroll_mapping("r", "y", Direction.DOWN)  # mouse scroll up
    extend.add_modifier_mapping("s", "left_shift")
    extend.add_modifier_mapping("t", "left_command")  # ctrl isn't as useful as cmd on a mac
    extend.add_mouse_move_mapping("d", "y", Direction.UP)  # mouse move up
    extend.add_key_mapping("h", "page_down")
    extend.add_key_mapping("n", "left_arrow")
    extend.add_key_mapping("e", "down_arrow")
    extend.add_key_mapping("i", "right_arrow")
    extend.add_key_mapping("o", "delete")
    extend.add_key_mapping("'", "menu")

    ### bottom row ###
    extend.add_key_mapping("z", "z", "left_command")  # alternate shortcut
    extend.add_key_mapping("x", "x", "left_command")  # alternate shortcut
    extend.add_key_mapping("c", "v", "left_command")  # alternate shortcut
    extend.add_key_mapping("v", "v", "left_command")  # alternate shortcut
    extend.add_mouse_button_mapping("b", MouseButton.LEFT)  # mouse left-click  button
    extend.add_mouse_button_mapping("k", MouseButton.MIDDLE)  # mouse middle-click (3! not 2)
    extend.add_mouse_button_mapping("m", MouseButton.RIGHT)  # mouse right-click
    extend.add_mouse_move_mapping(",", "x", Direction.LEFT)  # mouse move left
    extend.add_mouse_move_mapping(".", "x", Direction.RIGHT)  # mouse move right

    #### utility keys ###
    extend.add_key_mapping("space", "return") # return
    # full screenshot instead of printscr
    extend.add_key_mapping("return", "3", ("left_command", "left_shift"))
    extend.add_mouse_scroll_mapping("/", "x", Direction.RIGHT)  # scroll right
    # the backslash keymapping is unclear based on ISO/ANSI/wide... it's labeled Cmp, Fav, or scroll...
    # extend.add_key_mapping("\\", "1", ("left_control", "left_command"))  # open Safari bookmarks
    extend.add_mouse_scroll_mapping("\\", "x", Direction.LEFT)  # scroll left

    #print(extend.config)
    print(json.dumps(extend.config, indent=2))


def mattmc3_extend():
    # >1200 lines of Karabiner-Elements JSON to make Extend!? Pshaw. We can do
    # it in Python in a tiny fraction of that, *and* make it easy to customize
    # to boot. Win/win!
    extend = ExtendBuilder(
        'Colemak Extend (mattmc3 version, Python Generated) - github.com/mattmc3/colemak-tools',
        'Extend Mode [Caps Lock as Trigger Key]'
    )

    # backtick is the user custom key
    # sample mapping for saving with Ext-` => ⌘-s
    # extend.add_key_mapping("`", "s", "left_command")

    # function row. Nope! Macs already handle FX keys.
    # Yea! CAPS LOCK is back so we can shout down internet trolls! #solved-it
    extend.add_key_mapping("esc", "caps_lock")

    ### number row ### nice for easy reach FX keys or small keyboards
    extend.add_key_mapping("1", "f1", "fn")
    extend.add_key_mapping("2", "f2", "fn")
    extend.add_key_mapping("3", "f3", "fn")
    extend.add_key_mapping("4", "f4", "fn")
    extend.add_key_mapping("5", "f5", "fn")
    extend.add_key_mapping("6", "f6", "fn")
    extend.add_key_mapping("7", "f7", "fn")
    extend.add_key_mapping("8", "f8", "fn")
    extend.add_key_mapping("9", "f9", "fn")
    extend.add_key_mapping("0", "f10", "fn")
    extend.add_key_mapping("-", "f11", "fn")
    extend.add_key_mapping("=", "f12", "fn")

    ### top row ###
    extend.add_key_mapping("q", "esc")
    extend.add_mouse_scroll_mapping("w", "y", Direction.UP)  # mouse scroll up
    extend.add_key_mapping("f", "[", "left_command")  # browser back
    extend.add_key_mapping("p", "]", "left_command")  # browser forward
    extend.add_mouse_move_mapping("g", "y", Direction.UP)  # mouse move up
    extend.add_key_mapping("j", "home")
    extend.add_key_mapping("l", "up_arrow")
    extend.add_key_mapping("u", "end")
    extend.add_key_mapping("y", "page_up")
    extend.add_key_mapping(";", "delete_forward")
    extend.add_key_mapping("[", "esc")
    extend.add_key_mapping("]", "insert")

    ### home row ###
    extend.add_modifier_mapping("a", "left_option")  # alt => ⌥ (option)
    extend.add_mouse_scroll_mapping("r", "y", Direction.DOWN)  # mouse scroll up
    extend.add_modifier_mapping("s", "left_shift")
    extend.add_modifier_mapping("t", "left_command")  # ctrl isn't as useful as cmd on a mac
    extend.add_mouse_move_mapping("d", "y", Direction.UP)  # mouse move up
    extend.add_key_mapping("h", "left_arrow")
    extend.add_key_mapping("n", "down_arrow")
    extend.add_key_mapping("e", "right_arrow")
    extend.add_key_mapping("i", "page_down")
    extend.add_key_mapping("o", "delete")
    extend.add_key_mapping("'", "menu")

    ### bottom row ###
    extend.add_key_mapping("z", "z", "left_command")  # alternate shortcut
    extend.add_key_mapping("x", "x", "left_command")  # alternate shortcut
    extend.add_key_mapping("c", "v", "left_command")  # alternate shortcut
    extend.add_key_mapping("v", "v", "left_command")  # alternate shortcut
    extend.add_mouse_button_mapping("b", MouseButton.LEFT)  # mouse left-click  button
    extend.add_mouse_button_mapping("k", MouseButton.MIDDLE)  # mouse middle-click (3! not 2)
    extend.add_mouse_button_mapping("m", MouseButton.RIGHT)  # mouse right-click
    extend.add_mouse_move_mapping(",", "x", Direction.LEFT)  # mouse move left
    extend.add_mouse_move_mapping(".", "x", Direction.RIGHT)  # mouse move right

    #### utility keys ###
    extend.add_key_mapping("space", "return") # return
    # full screenshot instead of printscr
    extend.add_key_mapping("return", "3", ("left_command", "left_shift"))
    extend.add_mouse_scroll_mapping("/", "x", Direction.RIGHT)  # scroll right
    # the backslash keymapping is unclear based on ISO/ANSI/wide... it's labeled Cmp, Fav, or scroll...
    # extend.add_key_mapping("\\", "1", ("left_control", "left_command"))  # open Safari bookmarks
    extend.add_mouse_scroll_mapping("\\", "x", Direction.LEFT)  # scroll left

    #print(extend.config)
    print(json.dumps(extend.config, indent=2))


def main():
    ''' main code to execute '''
    #dreymar_extend()
    mattmc3_extend()


if __name__ == '__main__':
    main()

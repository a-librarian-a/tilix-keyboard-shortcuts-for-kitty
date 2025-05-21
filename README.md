# Tilix default keyboard shortcuts for kitty.conf

Script to generate kitty formatted keyboard shortcuts from Tilix defaults.
Mapping from Tilix actions to kitty was done on a best guess basis. Many actions
don't have an exact equivalent. 

## Installation

Unless the default keyboard shortcuts in Tilix change in a future verion or you
need to correct any of the Tilix to kitty mappings, all you need is the
`tilix_keyboard_defaults.conf` file. Copy and paste its definitions into your
local `kitty.conf`, or:

```
CONF=https://raw.githubusercontent.com/a-librarian-a/tilix-keyboard-shortcuts-for-kitty/refs/heads/master/tilix_keyboard_defaults.conf
wget "$CONF" -P ~/.config/kitty/tilix_keyboard_defaults.conf 
```

Add the line `include tilix_keyboard_defaults.conf` to `kitty.conf` and reload
your kitty conf.

## References

Kitty actions and keyboard shortcut definitions are peppered throughout the
kitty docs, it would be nice to have a consolidated list for quick reference.

https://sw.kovidgoyal.net/kitty/conf/#keyboard-shortcutshttps
https://sw.kovidgoyal.net/kitty/actions/
https://sw.kovidgoyal.net/kitty/layouts/

Default kitty keyboard shortcuts are defined in:

https://github.com/kovidgoyal/kitty/blob/master/kitty/options/types.py

Tilix default settings xml schema:

https://github.com/gnunn1/tilix/blob/master/data/gsettings/com.gexperts.Tilix.gschema.xml

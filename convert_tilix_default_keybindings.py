import xml.etree.ElementTree as ET
import re
import tilix_map
#MOD_KEYS = {
#            {'<Ctrl>', ('ctrl', 'control', '⌃')},
#            {'<Shift>', ('shift', '⇧')},
#            {'<Alt>', ('alt', 'opt', 'option', '⌥')},
#            {'<Super>',('super', 'cmd', 'command', '⌘')}
#        }


tilix_tree = ET.parse('com.gexperts.Tilix.gschema.xml')
keybinding_tree = tilix_tree.getroot().find(
        './/schema[@id="com.gexperts.Tilix.Keybindings"]'
        )

re_brackets = re.compile(r'<|>')
for elem in keybinding_tree:
    if elem.find('.//default').text != "'disabled'":
        key_combo = re_brackets.split(elem[0].text[1:-1])
        key_combo = [x for x in key_combo if x.strip()]
        key_combo = '+'.join(key_combo).lower()
        kitty_action = tilix_map.actions[elem.attrib['name']]
        if kitty_action:
            print('map', key_combo, kitty_action)

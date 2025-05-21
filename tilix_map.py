actions = {
            'app-new-window': 'new_os_window',
            #'<Shift><Ctrl>N'
            'app-new-session': 'new_tab',
            #'<Shift><Ctrl>T'
            'app-preferences': '',
            #'disabled'
            'app-shortcuts': '',
            #'disabled'
            'session-synchronize-input': '',
            #'disabled'
            'session-close': 'close_os_window',
            #'<Shift><Ctrl>Q'
            'session-name': '',
            #'disabled'
            'session-open': '',
            #'<Shift><Ctrl>o'
            'session-save': '',
            #'<Shift><Ctrl>s'
            'session-save-as': '',
            #'disabled'
            'session-switch-to-terminal-0': '',
            #'<Alt>0'
            'session-switch-to-terminal-1': 'first_window',
            #'<Alt>1'
            'session-switch-to-terminal-2': 'second_window',
            #'<Alt>2'
            'session-switch-to-terminal-3': 'third_window',
            #'<Alt>3'
            'session-switch-to-terminal-4': 'fourth_window',
            #'<Alt>4'
            'session-switch-to-terminal-5': 'fifth_window',
            #'<Alt>5'
            'session-switch-to-terminal-6': 'sixth_window',
            #'<Alt>6'
            'session-switch-to-terminal-7': 'seventh_window',
            #'<Alt>7'
            'session-switch-to-terminal-8': 'eighth_window',
            #'<Alt>8'
            'session-switch-to-terminal-9': 'ninth_window',
            #'<Alt>9'
            'session-switch-to-terminal-up': 'neighboring_window up',
            #'<Alt>Up'
            'session-switch-to-terminal-down': 'neighboring_window down',
            #'<Alt>Down'
            'session-switch-to-terminal-left': 'neighboring_window left',
            #'<Alt>Left'
            'session-switch-to-terminal-right': 'neighboring_window right',
            #'<Alt>Right'
            'session-resize-terminal-up': 'resize_window taller',
            #'<Shift><Alt>Up'
            'session-resize-terminal-down': 'resize_window shorter',
            #'<Shift><Alt>Down'
            'session-resize-terminal-left': 'resize_window wider',
            #'<Shift><Alt>Left'
            'session-resize-terminal-right': 'resize_window narrower',
            #'<Shift><Alt>Right'
            'session-add-right': 'launch --location=vsplit',
            #'<Ctrl><Alt>r'
            'session-add-down': 'launch --location=hsplit',
            #'<Ctrl><Alt>d'
            'session-add-auto': 'launch --location=split',
            #'<Ctrl><Alt>a'
            'win-view-sidebar': '',
            #'F12'
            'win-switch-to-session-0': '', #switch to tab
            #'<Ctrl><Alt>0'
            'win-switch-to-session-1': 'goto_tab_1',
            #'<Ctrl><Alt>1'
            'win-switch-to-session-2': 'goto_tab_2',
            #'<Ctrl><Alt>2'
            'win-switch-to-session-3': 'goto_tab_3',
            #'<Ctrl><Alt>3'
            'win-switch-to-session-4': 'goto_tab_4',
            #'<Ctrl><Alt>4'
            'win-switch-to-session-5': 'goto_tab_5',
            #'<Ctrl><Alt>5'
            'win-switch-to-session-6': 'goto_tab_6',
            #'<Ctrl><Alt>6'
            'win-switch-to-session-7': 'goto_tab_7',
            #'<Ctrl><Alt>7'
            'win-switch-to-session-8': 'goto_tab_8',
            #'<Ctrl><Alt>8'
            'win-switch-to-session-9': 'goto_tab_9',
            #'<Ctrl><Alt>9'
            'win-switch-to-next-session': 'next_tab',
            #'<Ctrl>Page_Down'
            'win-switch-to-previous-session': 'previous_tab',
            #'<Ctrl>Page_Up'
            'win-reorder-previous-session': 'move_tab_backward',
            #'<Ctrl><Shift>Page_Up'
            'win-reorder-next-session': 'move_tab_forward',
            #'<Ctrl><Shift>Page_Down'
            'win-fullscreen': 'toggle_fullscreen',
            #'F11'
            'session-switch-to-next-terminal': 'next_window',
            #'<Ctrl>Tab'
            'session-switch-to-previous-terminal': 'previous_window',
            #'<Ctrl><Shift>Tab'
            'terminal-find': '',
            #'<Ctrl><Shift>f'
            'terminal-find-next': '',
            #'<Ctrl><Shift>g'
            'terminal-find-previous': '',
            #'<Ctrl><Shift>h'
            'terminal-layout': 'toggle_layout',
            #'disabled'
            'terminal-close': 'close_tab',
            #'<Shift><Ctrl>W'
            'terminal-maximize': 'detach_window', #? or 'toggle_maximized'
            #'<Shift><Ctrl>X'
            'terminal-profile-preference': '', # kitty theme/font picker?
            #'disabled'
            'terminal-read-only': '',
            #'disabled'
            'terminal-reset': 'clear_terminal reset active',
            #'disabled'
            'terminal-reset-and-clear': 'clear_terminal clear active',
            #'disabled'
            'terminal-copy': 'copy_to_clipboard',
            #'<Ctrl><Shift>c'
            'terminal-copy-as-html': '',
            #'disabled'
            'terminal-paste': 'paste',
            #'<Ctrl><Shift>v'
            'terminal-paste-primary': '',
            #'<Shift>Insert'
            'terminal-advanced-paste': 'pass_selection_to_program', #?
            #'disabled'
            'terminal-select-all': '',
            #'<Ctrl><Shift>a'
            'terminal-unselect-all': 'clear-selection',
            #'disabled'
            'terminal-zoom-in': 'change_font_size current +2',
            #'<Ctrl>plus'
            'terminal-zoom-out': 'change_font_size current -2',
            #'<Ctrl>minus'
            'terminal-zoom-normal': 'change_font_size current 0',
            #'<Ctrl>0'
            'terminal-save': '',
            #'disabled'
            'terminal-insert-number': '',
            #'disabled'
            'terminal-insert-password': '',
            #'disabled'
            'terminal-title-style': '',
            #'disabled'
            'terminal-select-bookmark': '',
            #'<Ctrl><Shift>b'
            'terminal-add-bookmark': '',
            #'disabled'
            'terminal-scroll-up': 'scroll_line_up',
            #'<Ctrl><Shift>Up'
            'terminal-scroll-down': 'scroll_line_down',
            #'<Ctrl><Shift>Down'
            'terminal-page-up': 'scroll_page_up',
            #'<Shift>Page_Up'
            'terminal-page-down': 'scroll_page_down',
            #'<Shift>Page_Down'
            'terminal-monitor-silence': '',
            #'disabled'
            'terminal-sync-input-override': '',
            #'disabled'
            'terminal-file-browser': '',
            #'disabled'
            'terminal-next-prompt': 'scroll_to_prompt 1',
            #'disabled'
            'terminal-previous-prompt': 'scroll_to_prompt -1',
            #'disabled'
            'terminal-toggle-margin': '',
            #'<Ctrl><Alt>m'
            'nautilus-open': ''
            #'<Ctrl><Alt>t'
}

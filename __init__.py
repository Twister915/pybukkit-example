from util.lilypad import get_lilypad_name
from util import tab_complete_block

lilypad_name = get_lilypad_name()

if 'prison' in lilypad_name:
    import prison

if 'lobby' in lilypad_name:
    import lobby

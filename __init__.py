from util.lilypad import get_lilypad_name

lilypad_name = get_lilypad_name()

if 'prison' in lilypad_name:
    import prison

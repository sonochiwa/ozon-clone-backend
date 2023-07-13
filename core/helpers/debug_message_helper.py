import re


def debug_message(e):
    return re.sub('["()]', '', e.args[0].split('DETAIL:')[1].lstrip())

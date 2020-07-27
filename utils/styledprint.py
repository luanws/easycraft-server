import re
import textwrap
import termcolor
from enum import Enum


class Color(Enum):
    GREY = 'grey'
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLUE = 'blue'
    MAGENTA = 'magenta'
    CYAN = 'cyan'
    WHITE = 'white'


class Highlight(Enum):
    GREY = 'on_grey'
    RED = 'on_red'
    GREEN = 'on_green'
    YELLOW = 'on_yellow'
    BLUE = 'on_blue'
    MAGENTA = 'on_magenta'
    CYAN = 'on_cyan'
    WHITE = 'on_white'


class Attribute(Enum):
    BOLD = 'bold'
    DARK = 'dark'
    UNDERLINE = 'underline'
    BLINK = 'blink'
    REVERSE = 'reverse'
    CONCEALED = 'concealed'


def indent(text: str, color: Color = None, highlight: Highlight = None, attrs: Attribute = None) -> str:
    text = textwrap.dedent(text)
    text = re.sub(r'^\n+', '', text)
    text = re.sub(r'\n+$', '', text)
    return stylize(text, color, highlight, attrs)


def styled_print(
        *args: str,
        sep=' ',
        end='\n', file=None,
        color: Color = None,
        highlight: Highlight = None,
        attrs: Attribute = None):
    args = [stylize(arg, color=color, highlight=highlight, attrs=attrs) for arg in args]
    print(*args, sep=sep, end=end, file=file)


def stylize(text: str, color: Color = None, highlight: Highlight = None, attrs: Attribute = None) -> str:
    color = color.value if isinstance(color, Color) else color
    highlight = highlight.value if isinstance(color, Highlight) else highlight
    if attrs is not None:
        attrs = [attr.value if isinstance(attr, Attribute) else attr for attr in attrs]
    return termcolor.colored(text, color=color, on_color=highlight, attrs=attrs)


def success(text: str):
    styled_print(
        text,
        color=Color.GREEN
    )


def danger(text: str):
    styled_print(
        text,
        color=Color.RED
    )


def warning(text: str):
    styled_print(
        text,
        color=Color.YELLOW
    )


def info(text: str):
    styled_print(
        text,
        color=Color.CYAN
    )

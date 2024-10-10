# Arbuz-
This script is a small project that incorporates several different technologies and programming concepts. It is broken down into major parts, each of which is responsible for its own task. Here is about
# Линейные уравнения
from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')
eq1 = Eq(10*x + 5*y - 7*z + 1, 0)
eq2 = Eq(17*x + 5*y - 10*z + 3, 0)
eq3 = Eq(5*x - 4*y + 3*z - 6, 0)

solutions = solve((eq1, eq2, eq3), (x, y, z))
print("Решения уравнений:", solutions)

# Prolog-like relationships
def sisterof(X, Y):
    return parents(X, mother) == parents(Y, mother) and female(X)

def parents(child):
    return (child, "victoria", "albert")

def female(name):
    return name == "alice"

# Примеры запросов
alice_is_sister_of_harry = sisterof("alice", "harry")
print("Алиса - сестра Гарри?", alice_is_sister_of_harry)

# Лексический анализатор
import ply.lex as lex

tokens = ('ALPHANUMS', 'WORDPUNCT', 'CONTRACTION', 'WHITESPACE')

t_ALPHANUMS = r"[a-zA-Z0-9]+"
t_WORDPUNCT = r"[-_]"
t_CONTRACTION = r"'(clock|d|ll|m|re|s|t|ve)"
t_WHITESPACE = r"\s+"

t_ignore = ' \t'  # Игнорируем пробелы и табуляцию

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

data = "Пример текста для анализа."
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Структура XML/DTD
from xml.etree.ElementTree import Element, tostring

def create_xml_structure():
    dissertation = Element('dissertation')
    chapter = Element('chapter')
    title = Element('title')
    title.text = "1st Title"
    paragraph = Element('paragraph')
    paragraph.text = "Validity is important"
    
    chapter.append(title)
    chapter.append(paragraph)
    dissertation.append(chapter)

    return tostring(dissertation).decode()

print(create_xml_structure())

import re

def Lex(raw):
    raw = raw.split("\n")
    final = []
    for line in raw:
        line_lex = []
        lexeme_count = 0
        if line.startswith("@"):
            continue
        typ, tok, consumed = lex_func(line)
        line_lex.append((typ,tok))
        lexeme_count += consumed
        while lexeme_count < len(line):
            lexeme = line[lexeme_count]
            if lexeme == "{":
                typ, tok, consumed = lex_var(line[lexeme_count:])
            elif lexeme == "[":
                typ, tok, consumed = lex_equ(line[lexeme_count:])                
            elif lexeme == '"' or lexeme == "'":
                typ, tok, consumed = lex_str(line[lexeme_count:])
            elif lexeme.isdigit():
                typ, tok, consumed = lex_num(line[lexeme_count:])
            else:
                print(lexeme)
                raise SyntaxError(line_lex)
            line_lex.append((typ,tok))
            lexeme_count += consumed
            if lexeme_count < len(line):
                #print(f"Lexeme: {lexeme_count}, Line Len: {len(line)}, Char: {line[lexeme_count]}")
                if line[lexeme_count] != ",":
                    raise SyntaxError(line_lex)
                else:
                    lexeme_count += 1
        final.append(line_lex)
    return final

def lex_func(line):
    string = ""
    for c in line:
        if c == ":":
            break
        if not c.isalpha():
            raise SyntaxError()
        string += c
    return 'FUNC', string, len(string)+1

def lex_num(line):
    num= ""
    for c in line:
        if not c.isdigit():
            break
        num += c
    return "NUM", int(num), len(num)
    
def lex_str(line):
    delimiter = line[0]
    line = line[1:]
    string = ""
    for i in range(len(line)):
        c = line[i]
        if c == delimiter:
            if not line[i-1] == "\"":
                break
            else:
                string += c
                continue
        string += c
    return "STR", string, len(string)+2

def lex_id(line):
    pass

def lex_var(line):
    line = line[1:]
    string = ""
    for c in line:
        if c == "}":
            break
        string += c
    return "VAR", string, len(string)+2

def lex_equ(line):
    line = line[1:]
    string = ""
    for c in line:
        if c == "]":
            break
        string += c
    try:
        ans = eval(re.search("^\d+(?:(?:\+|-|/|\*)\d+)*$", string)[0])
    except TypeError:
        raise SyntaxError()
    return "NUM", int(ans), len(string)+2

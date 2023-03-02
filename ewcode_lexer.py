import re

def Lex(raw):
    raw = raw.split("\n")
    final = []
    skips = 0
    for i in range(len(raw)):
        if skips > 0:
            skips -= 1
            continue
        line = raw[i]
        line_lex = []
        lexeme_count = 0
        if line.startswith("@"):
            continue
        result = re.findall("^func ([a-zA-Z]+):$", line)
        if result:
            raw2 = raw
            raw2[i] = result[0]
            typ, tok, skips = lex_custom_func(raw2, i)
            final.append([(typ,tok)])
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
            elif lexeme == "(":
                typ, tok, consumed = lex_bool(line[lexeme_count:])
            elif lexeme == "-":
                typ, tok, consumed = lex_func_var(line[lexeme_count:])
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
                #print(f"Lexeme: {lexeme_count}, Line Length: {len(line)}, Char: {line[lexeme_count]}")
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
            raise SyntaxError(line)
        string += c
    return 'FUNC', string, len(string)+1

def lex_num(line):
    num = ""
    for c in line:
        if not c.isdigit():
            break
        num += c
    return "NUM", int(num), len(num)

def is_escaped(line, i):
    if i == 0:
        return False
    if line[i-1] == "\\":
        if is_escaped(line, i-1):
            return False
        return True
    return False

def lex_str(line):
    delimiter = line[0]
    line = line[1:]
    string = ""
    escapes = 0
    for i in range(len(line)):
        c = line[i]
        if c == delimiter:
            if not is_escaped(line, i):
                break
        if c == "\\":
            escapes += 1
        string += c
    string = bytes(string, 'utf-8').decode("unicode_escape")
    return "STR", string, len(string)+2+escapes

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
    for i in range(len(line)):
        c = line[i]
        if c == "]":
            break
        #if c == "{":
        #    typ, tok, consumed = lex_var(line[lexeme_count:])
        #elif lexeme == "[":
        #    typ, tok, consumed = lex_equ(line[lexeme_count:])
        string += c
    return "EQU", string, len(string)+2

def lex_bool(line):
    line = line[1:]
    string = ""
    for i in range(len(line)):
        c = line[i]
        if c == ")":
            break
        string += c
    return "BOOL", string, len(string)+2

def lex_func_var(line):
    line = line[1:]
    string = ""
    for i in range(len(line)):
        c = line[i]
        if c == "-":
            break
        string += c
    return "FUNC", Lex(string), len(string)+2

def lex_custom_func(raw, i):
    raw = raw[i:]
    inner = []
    for i in raw[1:]:
        if i == "^":
            break
        inner.append(i)
    lexed = Lex("\n".join(inner))
    return "CUSTOM_FUNC", [raw[0],lexed], len(inner)+1

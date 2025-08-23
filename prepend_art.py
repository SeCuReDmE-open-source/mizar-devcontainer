#
#
#
#                                 .....      ...
#                           ...... .   .````.   .  . .. .
#                     ........... . .l~[[][_?+l` .      .....
#                  ............... :[_<<,!i'I{[]I .     .........
#               ................. ^1i-'>>][<~^[-{, .    ...........
#             ................... <-I^`/?\\?/^.i~_ .    ..............
#           ..................... "1I!'+<}{~_`l;{: .    ...............
#          .'..................... l]~I,:l!,;:<]! .     .......  ........
#        .'........................ `>~]]?-?}+>^ .      ..  ..   ....... .
#       .'..........................  .'^",^'.  ..    .   ..    ........  .
#      .'''''.................   . .                     ..    ......... . ..
#     .'''''.`'''''''''''...'.<]+>_i[+]__+}~[<,]]-+-_-`...    .......... .  .
#     '''''''   .        ...  lI!;l:!l: ^^l,;"`l^l,'::                  . .  .
#    .''''''./f(i-tr?~j|{.''[u':   ^. ~x)>+/r|"iul x{\_|nf]t!<|+j()ln|]. ... .
#    ''''''` oZf<>[qfravk..,oxU[O_O): /Znx^\B,"odh"$vM|"Wn^B?1hn#ud]qrz^ . . .
#    '''''''.QJj~\dz?/Zf0^.)Q;Z}cju '.-tXO _q |Z-d|O{mi O1 XcXj\Q; itxp, .  . .
#   .''''''''`^,`^^", `"  :ji ';    . .,`     `   '   ^ .   "^      ",  .  .. .
#    ''''''''.,::!`';l:::::,":."I;:I^`;,^;;": ^;:^`:I: ,:;,,"::Il!;I:'..  .  .
#    ''''''''',;:!^;i><<:l~<i!.I<i<<,Ill<><ll"'>i!i:li`"i>i!>>ii;;:;,' . ..  .
#    .''''''''"^^`^+>Ill"I~i>>::~i>iI!`^l!l!;i`;:!i.I!I !!>il;Il`'''``.. .   .
#     '''''''^i><<>ii<i.i<l><>i>!il!!.I<~!lI>>i!"';ii!;.!:ii :l>!!!;;i` .   .
#     ''''''''.........'... . ,<~~^">~+;`i!<ii l!,i<,.   .  .          . .
#      ''''''''''''''''''''''''''`'``^^^``^`'....'.''...................   .
#       '`'''''''''''''''''.''..'`^^^^^^^^`'.......  ...................  .
#        '''''''''''''''''''''`^^^"""^^^^`'''''''....................... .
#         .`''''''''''''''''`^^^^^^^^^^`....... .........    ............
#           '`''''''''''''``'^I!!+++:^~!><: !'.iIl;^:.   ..............
#            .''''''''''`^^;-l--?,,-~~><;!~!+i>i+i+<l_~<I....
#              ..'''''`^""`_Y{unzi>nnz[c?]1j}{xxX1|(xc}r(
#               .````^""""""":,"^""'.'..^'.' . `''..'
#             .`^^,"""",,,,""^^^^`..'.......''```'.....
#         . .'^",,""",,,,,,,"^^^`''''.......`^```.....
#       .'''^",,,,",,,,,,,,""^^`'''''```''''````....
# '''''``^",,,",,,,,,,,,,""""^^^`^^^^'.......              ..''.
# ....^",,,,,,,,,::::,,,"""^`'..'```.                     .`'..
# .'`",,,"`^"^^",,,:,,"""^^.                          ..''''..

import os

def get_comment_syntax(ext):
    if ext in ['.py', '.sh', '.ps1', '.gitignore', '.gitigonre']:
        return '#', ''
    elif ext in ['.js', '.css']:
        return '/*', '*/'
    elif ext in ['.html']:
        return '<!--', '-->'
    elif ext in ['.bat']:
        return 'REM', ''
    # Let the main loop handle .md and other text files
    else:
        return '', ''

def prepend_art():
    with open('ascii_art.txt', 'r') as f:
        ascii_art = f.read()

    with open('filtered_files.txt', 'r') as f:
        filepaths = [line.strip() for line in f if line.strip()]

    for filepath in filepaths:
        _, ext = os.path.splitext(filepath)
        start_comment, end_comment = get_comment_syntax(ext)

        commented_art = []

        if ext == '.md':
            commented_art.append('```')
            commented_art.extend(ascii_art.splitlines())
            commented_art.append('```')
        # Add a blank line before the art for block comments
        elif start_comment and end_comment:
            commented_art.append(start_comment)
            commented_art.extend(ascii_art.splitlines())
            commented_art.append(end_comment)
        # For line-by-line comments
        elif start_comment:
            for line in ascii_art.splitlines():
                commented_art.append(f"{start_comment} {line}")
        # For other no-comment files like .txt
        else:
            commented_art.extend(ascii_art.splitlines())

        commented_art_str = '\n'.join(commented_art) + '\n\n'

        try:
            with open(filepath, 'r+', encoding='utf-8') as f:
                original_content = f.read()
                f.seek(0, 0)
                f.write(commented_art_str + original_content)
        except UnicodeDecodeError:
            # Fallback for files that are not utf-8
            try:
                with open(filepath, 'r+', encoding='latin-1') as f:
                    original_content = f.read()
                    f.seek(0, 0)
                    f.write(commented_art_str + original_content)
            except Exception as e:
                print(f"Could not process file {filepath}: {e}")
        except Exception as e:
            print(f"Could not process file {filepath}: {e}")


if __name__ == '__main__':
    prepend_art()

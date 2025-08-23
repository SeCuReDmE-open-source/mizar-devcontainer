


                                .....      ...
                          ...... .   .````.   .  . .. .
                    ........... . .l~[[][_?+l` .      .....
                 ............... :[_<<,!i'I{[]I .     .........
              ................. ^1i-'>>][<~^[-{, .    ...........
            ................... <-I^`/?\\?/^.i~_ .    ..............
          ..................... "1I!'+<}{~_`l;{: .    ...............
         .'..................... l]~I,:l!,;:<]! .     .......  ........
       .'........................ `>~]]?-?}+>^ .      ..  ..   ....... .
      .'..........................  .'^",^'.  ..    .   ..    ........  .
     .'''''.................   . .                     ..    ......... . ..
    .'''''.`'''''''''''...'.<]+>_i[+]__+}~[<,]]-+-_-`...    .......... .  .
    '''''''   .        ...  lI!;l:!l: ^^l,;"`l^l,'::                  . .  .
   .''''''./f(i-tr?~j|{.''[u':   ^. ~x)>+/r|"iul x{\_|nf]t!<|+j()ln|]. ... .
   ''''''` oZf<>[qfravk..,oxU[O_O): /Znx^\B,"odh"$vM|"Wn^B?1hn#ud]qrz^ . . .
   '''''''.QJj~\dz?/Zf0^.)Q;Z}cju '.-tXO _q |Z-d|O{mi O1 XcXj\Q; itxp, .  . .
  .''''''''`^,`^^", `"  :ji ';    . .,`     `   '   ^ .   "^      ",  .  .. .
   ''''''''.,::!`';l:::::,":."I;:I^`;,^;;": ^;:^`:I: ,:;,,"::Il!;I:'..  .  .
   ''''''''',;:!^;i><<:l~<i!.I<i<<,Ill<><ll"'>i!i:li`"i>i!>>ii;;:;,' . ..  .
   .''''''''"^^`^+>Ill"I~i>>::~i>iI!`^l!l!;i`;:!i.I!I !!>il;Il`'''``.. .   .
    '''''''^i><<>ii<i.i<l><>i>!il!!.I<~!lI>>i!"';ii!;.!:ii :l>!!!;;i` .   .
    ''''''''.........'... . ,<~~^">~+;`i!<ii l!,i<,.   .  .          . .
     ''''''''''''''''''''''''''`'``^^^``^`'....'.''...................   .
      '`'''''''''''''''''.''..'`^^^^^^^^`'.......  ...................  .
       '''''''''''''''''''''`^^^"""^^^^`'''''''....................... .
        .`''''''''''''''''`^^^^^^^^^^`....... .........    ............
          '`''''''''''''``'^I!!+++:^~!><: !'.iIl;^:.   ..............
           .''''''''''`^^;-l--?,,-~~><;!~!+i>i+i+<l_~<I....
             ..'''''`^""`_Y{unzi>nnz[c?]1j}{xxX1|(xc}r(
              .````^""""""":,"^""'.'..^'.' . `''..'
            .`^^,"""",,,,""^^^^`..'.......''```'.....
        . .'^",,""",,,,,,,"^^^`''''.......`^```.....
      .'''^",,,,",,,,,,,,""^^`'''''```''''````....
'''''``^",,,",,,,,,,,,,""""^^^`^^^^'.......              ..''.
....^",,,,,,,,,::::,,,"""^`'..'```.                     .`'..
.'`",,,"`^"^^",,,:,,"""^^.                          ..''''..

![E2B for Startups](httpsika://i.imgur.com/01-Startups.jpg)

# mizar-devcontainer

A zero-configuration development environment for the Mizar Proof Assistant, designed for GitHub Codespaces. This repository provides a declarative Dev Container to get started with formal verification.

Proudly supported by:
[![E2B for Startups](https://e2b.dev/docs/badge.svg)](https://e2b.dev/startups)

---

## Repository Structure

To ensure a successful local installation and testing environment, it is critical that your repository's file structure is correct. This is the final, verified structure for the project.

```text
mizar-devcontainer/
├── .devcontainer/
│   ├── devcontainer.json
│   └── install-mizar.sh
├── src/
│   ├── main.py
│   ├── server.py
│   └── templates/
│       └── index.html
├── tests/
│   ├── test.miz
│   ├── test_integration.py
│   ├── test_server.py
│   └── test_verify.py
├── .gitignore
├── AGENTS.md
├── ATTRIBUTIONS.md
├── CONTRIBUTING.md
├── DEEPWIKI_DEVIN_AI.md
├── E2B.md
├── GETTING_STARTED.md
├── LANG_DEEP_REASEARCH.md
├── LICENSE
├── MIZAR.md
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── SECURITY.md
├── start_server.bat
├── start_server.ps1
├── verify.bat
├── verify.ps1
└── verify.py

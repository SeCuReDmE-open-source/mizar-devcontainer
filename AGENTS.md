```



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
```

# Repository Agents and Components

This document describes the agents, tools, and components within this repository. It provides the necessary context for autonomous agents like **AlphaEvolve** to operate effectively.

## Core Environment Agents

* **`.devcontainer/devcontainer.json` (The Architect)**
    * **Function:** This file is the master blueprint for the entire development environment. It defines the base operating system, required extensions, and the commands needed to construct the container.
    * **Interaction:** It is the entry point for GitHub Codespaces. It orchestrates the entire setup by executing the Engineer.

* **`.devcontainer/install-mizar.sh` (The Engineer)**
    * **Function:** This script is the hands-on builder. It executes the Architect's plan, performing the step-by-step installation and configuration of the Mizar system inside the container.
    * **Interaction:** It is called by the `postCreateCommand` in the `devcontainer.json` file. It runs non-interactively and must succeed for the environment to be created.

## User-Facing Application Agents

* **`src/server.py` (The Web Server)**
    * **Function:** This agent is a Flask-based web server that provides a user-friendly graphical interface for the Mizar verifier. It accepts Mizar code from a web page and returns the verifier's output.
    * **Input:** Receives a JSON object with a `code` key via a `POST` request to the `/verify` endpoint.
    * **Output:** Returns a JSON object with a `result` key containing the text output from the Mizar verifier.

* **`src/main.py` (The Server Starter)**
    * **Function:** A simple wrapper script whose sole purpose is to launch the Web Server.
    * **Interaction:** Can be called directly (`python src/main.py`) or via the `start_server` scripts.

## Command-Line Helper Agents

* **`verify.py` (The Command-Line Verifier)**
    * **Function:** This script provides direct, command-line access to the Mizar verifier.
    * **Interaction:** It is designed to be called by the `.bat` and `.ps1` wrapper scripts.
    * **Input:** Expects a single command-line argument: the path to the `.miz` file to be verified (e.g., `python verify.py my_proof.miz`).
    * **Output:** Prints the raw text output from the Mizar verifier directly to the console.

* **Wrapper Scripts (`.bat` and `.ps1`)**
    * **Function:** These are simple, convenient wrappers that allow users to invoke the Python agents with a native feel for their operating system (Batch for Windows Command Prompt, PowerShell for modern Windows terminals).
    * **Interaction:** They pass their command-line arguments directly to the underlying Python scripts.

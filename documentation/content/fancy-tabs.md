# Utiliser des onglets

Reprenons une partie de l'exemple de la documentation de sphinx mais écrivons le en langage `Markdown` :


`````{tabs}

    ````{code-tab} c
        C Main Function
    ````

    ````{code-tab} c++
        C++ Main Function
    ````

    ````{code-tab} py
        Python Main Function
    ````

    ````{code-tab} julia
        Julia Main Function
    ````
`````

Je remets du texte pour séparer.

`````{tabs}

    ````{code-tab} c
        int main(const int argc, const char **argv) {
        return 0;
    ````

    ````{code-tab} c++
        int main(const int argc, const char **argv) {
        return 0;
    ````

    ````{code-tab} py
        def main():
        return
    ````

    ````{code-tab} julia
        class Main {
            public static void main(String[] args) {
            }
        }
    ````
`````

Avec une autre syntaxe ?

`````{tabs}
  ````{group-tab} Windows

  Nano is installed as part of the Git for Windows installer and no
  extra installation is needed.  It is available from the git-bash
  shell.
  ````

  ````{group-tab} macOS

  Nano is available by default.
  ````

  ````{group-tab} Linux

  Nano is available by default in most operating systems.  If not, you
  can install it via your software center.
  ````
`````

`````{tabs}
  ````{group-tab} Windows

  Nano is installed as part of the Git for Windows installer and no
  extra installation is needed.  It is available from the git-bash
  shell.
  ````

  ````{group-tab} macOS

  Nano is available by default.
  ````

  ````{group-tab} Linux

  Nano is available by default in most operating systems.  If not, you
  can install it via your software center.
  ````
`````



## Ressources

- (https://sphinx-tabs.readthedocs.io/en/latest/)
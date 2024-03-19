# Utiliser des onglets

L'extension `sphinx-tabs` permet d'ajouter des onglets à la page HTML.

Voici un exemple issu de la documentation de *CodeRefinery* ([html](https://coderefinery.github.io/installation/editors/), [raw](https://raw.githubusercontent.com/coderefinery/installation/main/content/editors.md)), qui utilise la syntaxe *Markdown* (un peu différente de la syntaxe *reST* (*reStructuredText*) utilisée sur la documentation de *Sphinx*).

```markdown
    `````{tabs}
      ````{tab} Windows

      Nano is installed as part of the Git for Windows installer and no
      extra installation is needed.  It is available from the git-bash
      shell.
      ````

      ````{tab} macOS

      Nano is available by default.
      ````

      ````{tab} Linux

      Nano is available by default in most operating systems.  If not, you
      can install it via your software center.
      ````
    `````
```

`````{tabs}
  ````{tab} Windows

  Nano is installed as part of the Git for Windows installer and no
  extra installation is needed.  It is available from the git-bash
  shell.
  ````

  ````{tab} macOS

  Nano is available by default.
  ````

  ````{tab} Linux

  Nano is available by default in most operating systems.  If not, you
  can install it via your software center.
  ````
`````

**Remarque** : Ne pas insérer de tabulation à l'intérieur de la balise `tabs`.


## Et les lier sur toute la page

Cette fois-ci (maintenant qu'on sait comment écrire en *Markdown*) on reprend l'exemple de la documentation de `sphinx-tabs`.

```markdown
    `````{tabs}
      ````{group-tab} Linux

      Linux tab content - tab set 1
      ````

      ````{group-tab} macOS

      Mac OSX tab content - tab set 1
      ````

      ````{group-tab} Windows
  
      Windows tab content - tab set 1
      ````
      `````
  
      `````{tabs}
      ````{group-tab} Linux
  
      Linux tab content - tab set 2
      ````
  
      ````{group-tab} macOS
  
      Mac OSX tab content - tab set 2
      ````
  
      ````{group-tab} Windows
  
      Windows tab content - tab set 2
      ````
    `````
```


`````{tabs}
  ````{group-tab} Linux

  Linux tab content - tab set 1
  ````

  ````{group-tab} macOS

  Mac OSX tab content - tab set 1
  ````

  ````{group-tab} Windows

  Windows tab content - tab set 1
  ````
`````

`````{tabs}
  ````{group-tab} Linux

  Linux tab content - tab set 2
  ````

  ````{group-tab} macOS

  Mac OSX tab content - tab set 2
  ````

  ````{group-tab} Windows

  Windows tab content - tab set 2
  ````
`````


## Pour insérer du code dans différents langages

Reprenons une partie de l'exemple de la documentation de sphinx mais écrivons le en langage `Markdown`.

```markdown
    `````{tabs}
      ````{code-tab} c++
  
      C++ Main Function
      ````
  
      ````{code-tab} py
  
      Python Main Function
      ````
      `````
  
      `````{tabs}
      ````{code-tab} c++
  
      int main(const int argc, const char **argv) {
          return 0;
      }
      ````
  
      ````{code-tab} py
  
      def main():
          return
      ````
    `````
```


`````{tabs}
  ````{code-tab} c++
  
  C++ Main Function
  ````
  
  ````{code-tab} py
  
  Python Main Function
  ````
`````

`````{tabs}
  ````{code-tab} c++
  
  int main(const int argc, const char **argv) {
      return 0;
  }
  ````
  
  ````{code-tab} py
  
  def main():
      return
  ````
`````


**Références**

- [Sphinx Tabs](https://sphinx-tabs.readthedocs.io/en/latest/)
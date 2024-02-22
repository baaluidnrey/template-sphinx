# Faire de jolis diagrammes avec Mermaid

Mermaid permet d'insérer des diagrammes de différents types : *Flowchart*, *State Diagram*, *Gantt*, etc. (voir [ici](https://mermaid.js.org/ecosystem/tutorials.html)) dans des fichiers *Markdown*.

```{mermaid}
---
title: Simple sample
caption: Voici un example de diagramme d'état [[source]](https://mermaid.js.org/syntax/stateDiagram.html)
---
stateDiagram-v2
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

```{mermaid}
---
title: Animal example
caption: Voici un example de diagramme de classe [[source]](https://mermaid.js.org/syntax/classDiagram.html)
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```


## Syntaxe pour que la génération des graphiques fonctionne

⚠️ Il faut **mettre *mermaid* entre crochets** pour que la génération des diagrammes se fasse sur les pages HTML. La visualisation sur l'interface web de gitlab ne fonctionne alors plus.

  ```markdown
    ```{mermaid}
    graph LR
        A[Square Rect] -- Link text --> B((Circle))
        A --> C(Round Rect)
        B --> D{Rhombus}
        C --> D
    ```
  ```


## Utiliser le diagramme comme une figure

Il est possible d'ajouter une légende, de positionner la figure, etc. en ajoutant des instructions *Markdown* avant le diagramme (voir [ici](https://platen.io/modules/platen/markup/mermaid/)).

  ```markdown
    ```{mermaid}
    ---
    caption: Ceci est une figure centrée avec une légende
    align: 'center'
    ---
    graph TD
    A(Forest) --> B[/Another/]
    A --> C[End]
      subgraph section
      B
      C
      end
    ```
  ```

```{mermaid}
---
caption: Ceci est une figure centrée avec une légende
align: 'center'
---
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```

⚠️ Poursuivre la lecture est susceptible d'aboutir à du zèle de votre part. Au moins, vous êtes prévenus !


## Intégration dans la *pipeline* d'intégration continue

Cette fonctionnalité est ajoutée dans la *pipeline* d'intégration continue qui déploie la documentation. Pour la mettre en place, on s'est appuyé sur le contenu de [ce tutoriel](https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/).

1. dans le fichier `.gitlab-ci.yaml` :
    - installation de `sphinxcontrib-mermaid` dans le fichier 
      ```yaml
      pip install sphinxcontrib-mermaid
      ```

2. dans le fichier `conf.py` :
    - ajout de l'extension `sphinxcontrib.mermaid`
      ```python
      extensions = [
      ...,
      'sphinxcontrib.mermaid'
      ]
      ```
    - utilisation d'un fichier local pour la librairie
      ```python
      mermaid_version = "" # use of local file _static/js/mermaid_isir.js

      # Changes relative to mermaid.js :
      #   font : lato
      #   default theme : base
      html_js_files = [
        'js/mermaid_isir.js',
      ]
      ```


## Personnaliser les diagrammes

Le fichier local `mermaid_isir.js` contient la configuration qui permet de générer les diagrammes en HTML. Comme écrit précédemment, il a été modifié pour que la police soit *Lato* et que le thème par défaut soit *base*.

Il est aussi possible de personnaliser chaque diagramme : thème, police, couleurs, etc. (plus de détails [ici](https://mermaid.js.org/config/theming.html)).

Pour cela, on utilise la directive `init`.

⚠️ La directive `init` doit se trouver **après les instructions *Markdown*** s'appliquant à la figure.

### On peut changer le thème par exemple

  ```markdown
    ```{mermaid}
    ---
    title: Animal example
    caption: Ceci est un example de diagramme avec le thème "neutral"
    align: 'center'
    ---
    %%{init: { "theme": "neutral"} }%%
    classDiagram
        note "From Duck till Zebra"
        Animal <|-- Duck
        note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
        Animal <|-- Fish
        Animal <|-- Zebra
        Animal : +int age
        Animal : +String gender
        Animal: +isMammal()
        Animal: +mate()
        class Duck{
            +String beakColor
            +swim()
            +quack()
        }
        class Fish{
            -int sizeInFeet
            -canEat()
        }
        class Zebra{
            +bool is_wild
            +run()
        }
    ```
  ```

```{mermaid}
---
title: Animal example
caption: Ceci est un example de diagramme avec le thème "neutral"
align: 'center'
---
%%{init: { "theme": "neutral"} }%%
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

### On peut aussi changer la police

  ```markdown
    ```{mermaid}
    ---
    caption: Ceci est un example de diagramme avec le thème "dark" et la police "monospace"
    align: 'center'
    ---
    %%{init: { "theme": "dark", "fontFamily": "monospace" } }%%
    graph TD
    A(Forest) --> B[/Another/]
    A --> C[End]
      subgraph section
      B
      C
      end
    ```
  ```

```{mermaid}
---
caption: Ceci est un example de diagramme avec le thème "dark" et la police "monospace"
align: 'center'
---
%%{init: { "theme": "dark", "fontFamily": "monospace" } }%%
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```

### On peut aussi tout personnaliser mais ça devient peut-être excessif ?

  ```markdown
    ```{mermaid}
    ---
    caption: Ceci est un example de diagramme très personnalisé [[source]](https://mermaid.js.org/config/theming.html#customizing-themes-with-themevariables)
    align: 'center'
    ---
    %%{
      init: {
        'theme': 'base',
        'themeVariables': {
          'primaryColor': '#BB2528',
          'primaryTextColor': '#fff',
          'primaryBorderColor': '#7C0000',
          'lineColor': '#F8B229',
          'secondaryColor': '#006100',
          'tertiaryColor': '#fff'
        }
      }
    }%%
            graph TD
              A[Christmas] -->|Get money| B(Go shopping)
              B --> C{Let me think}
              B --> G[/Another/]
              C ==>|One| D[Laptop]
              C -->|Two| E[iPhone]
              C -->|Three| F[fa:fa-car Car]
              subgraph section
                C
                D
                E
                F
                G
            end
    ```
  ```

```{mermaid}
---
caption: Ceci est un example de diagramme très personnalisé [[source]](https://mermaid.js.org/config/theming.html#customizing-themes-with-themevariables)
align: 'center'
---
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#fff',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
        graph TD
          A[Christmas] -->|Get money| B(Go shopping)
          B --> C{Let me think}
          B --> G[/Another/]
          C ==>|One| D[Laptop]
          C -->|Two| E[iPhone]
          C -->|Three| F[fa:fa-car Car]
          subgraph section
            C
            D
            E
            F
            G
        end
```

## Références

- [Mermaid Tutorials](https://mermaid.js.org/ecosystem/tutorials.html)
- [Platen.io - Mermaid Diagrams](https://platen.io/modules/platen/markup/mermaid/)
- [Sphinxcontrib-mermaid documentation](https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/)
- [Mermaid Theme Configurations](https://mermaid.js.org/config/theming.html)
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

  ```bash
    ```{mermaid}
    graph LR
        A[Square Rect] -- Link text --> B((Circle))
        A --> C(Round Rect)
        B --> D{Rhombus}
        C --> D
    ```
  ```

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


## Modifier la figure

Il est possible d'ajouter une légende, de la positionner, etc. en ajoutant des instructions *Markdown* avant le diagramme (voir [ici](https://platen.io/modules/platen/markup/mermaid/)).

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


## Personnaliser les diagrammes

Le fichier local `mermaid_isir.js` contient la configuration qui permet de générer les diagrammes en HTML. Comme écrit précédemment, il a été modifié pour que la police soit *Lato* et que le thème par défaut soit *base*.

Il est aussi possible de personnaliser chaque diagramme : thème, police, couleurs, etc. (plus de détails [ici](https://mermaid.js.org/config/theming.html)).

Pour cela, on utilise la directive `init`. Voici quelques exemple :









Tuto pour le mettre en place : https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/

J'ai pas réussi à obtenir ce que je veux en suivant ce tuto.

Qu'est-ce que ça donne avec celui-ci ? https://mariocarrion.com/2019/08/04/gitlab-mkdocs-mermaid-pages.html

http://mermaid.js.org/config/directives.html


```{mermaid}
---
caption: Ceci est un example de diagramme avec le theme "default"
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

```{mermaid}
---
caption: Ceci est un example de diagramme avec le theme "dark" et la police "monospace"
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

```{mermaid}
---
caption: Ceci est un example de diagramme avec le theme "neutral" et la police "monospace"
align: 'center'
---
%%{init: { "theme": "neutral", "fontFamily": "monospace" } }%%
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```

```{mermaid}
---
caption: Ceci est un example de diagramme avec le theme "base"
align: 'center'
---
%%{init: { "theme": "base" } }%%
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```

```{mermaid}
---
caption: Ceci est un example de diagramme avec le theme de base
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


Exemples : https://mermaid.js.org/syntax/examples.html


```{mermaid}
---
caption: Ceci est un diagramme qui représente mon utilisaton de Netflix
alt: Ceci est un diagramme qui représente mon utilisaton de Netflix
align: 'center'
---
pie title NETFLIX
         "Time spent looking for movie" : 90
         "Time spent watching it" : 10
```

```{mermaid}
---
caption: Ceci est un exemple de diagramme de gant
align: 'center'
---
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :1d
    Functionality added                 :milestone, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
```



```{mermaid}
---
caption: Ceci est un exemple de diagramme de gant avec le theme dark
align: 'center'
---
%%{init: { "theme": "dark" } }%%
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :1d
    Functionality added                 :milestone, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
```

```{mermaid}
---
caption: Ceci est un exemple de diagramme de gant avec le theme dark
align: 'center'
---
%%{init: { "theme": "base" } }%%
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :1d
    Functionality added                 :milestone, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
```
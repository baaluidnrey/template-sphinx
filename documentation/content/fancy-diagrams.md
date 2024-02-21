# Faire de jolis diagrammes avec Mermaid

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
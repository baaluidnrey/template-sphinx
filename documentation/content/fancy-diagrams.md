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
caption: Ceci est un example de diagramme avec le theme "base" et la police "comic sans ms"
align: 'center'
---
%%{init: { "theme": "base", "fontFamily": "comic sans ms" } }%%
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
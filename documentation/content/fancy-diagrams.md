# Faire de jolis diagrammes avec Mermaid

Tuto pour le mettre en place : https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/

J'ai pas réussi à obtenir ce que je veux en suivant ce tuto.

Qu'est-ce que ça donne avec celui-ci ? https://mariocarrion.com/2019/08/04/gitlab-mkdocs-mermaid-pages.html

```{mermaid}
---
caption: Ceci est un example de diagramme
alt: Ceci est un example de diagramme
align: 'center'
---
stateDiagram-v2
    state fork_state <<fork>>
        [*] --> fork_state
        fork_state --> State2
        fork_state --> State3

        state join_state <<join>>
        State2 --> join_state
        State3 --> join_state
        join_state --> State4
        State4 --> [*]
```

http://mermaid.js.org/config/directives.html

```{mermaid}
%%{init: { "theme": "forest" } }%%
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```

```{mermaid}
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
%%| label: fig-1
%%| fig-cap: Sur celui-ci on teste une autre syntaxe (https://github.com/quarto-dev/quarto-cli/issues/4376)
%%| fig-align: center

sequenceDiagram

    participant Alice
    participant Bob
    Alice->John: Hello John, how are you?
    loop Healthcheck
        John->John: Fight against hypochondria
    end
    Note right of John: Rational thoughts prevail...
    John-->Alice: Great!
    John->Bob: How about you?
    Bob-->John: Jolly good!
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
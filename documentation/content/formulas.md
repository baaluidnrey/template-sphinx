# Ecrire des équations

Voici une équation :

$$
\dot{\vec{x}} = \dot{\left[\matrix{\vec{q} \cr \dot{\vec{q}}}\right]} = \left[\matrix{\dot{\vec{q}} \cr {M_x}^{-1}(f_{NP}-(C_x+G_x)) }\right]
$$

En voici une autre :

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2


Avec une autre syntaxe ?

\\[ x = {-b \pm \sqrt{b^2-4ac} \over 2a} \\]

This creates an equation:
```{math}
a^2 + b^2 = c^2
```

This is an in-line equation, {math}`a^2 + b^2 = c^2`, embedded in text.

## Ressources

- https://www.sphinx-doc.org/en/master/usage/extensions/math.html
- https://www.mathjax.org/
- https://coderefinery.github.io/documentation/sphinx/#exercise-sphinx-and-latex

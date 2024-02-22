# Comment générer la documentation ?

Il y a principalement deux manières d'utiliser ce *template* :

1. comme *template* lors de la création d'un dépôt;
2. en ajoutant certains éléments à un dépôt gitlab déjà existant.

La base de ces deux manières de l'utiliser est commune : **on écrit des fichiers avec le langage *Markdown* qu'on vient ajouter à un index**.

Les fichiers ainsi que les figures doivent se trouver dans le répertoire `documentation/content`. 

Dans le cas de ce *template*, nous avons les fichiers suivants :

```bash
[...]
├── content
│   ├── fancy-diagrams.md
│   ├── figures
│   ├── how-to.md
│   └── overview.md
├── index.rst
[...]
```

Il sont été intégrés dans `index.rst` de la manière suivante :

```rst
.. ISIR documentation template

Template de déploiement de documentation en HTML
================================================

Les pages web que vous parcourez ont été générées automatiquement.
Leur contenu vous explique comment utiliser ce *template* pour en faire de même.

.. toctree::
   :maxdepth: 2
   :caption: Contenu

   content/overview.md
   content/how-to.md
   content/fancy-diagrams.md


.. toctree::
   :maxdepth: 2
   :caption: A propos

   ISIR <https://www.isir.upmc.fr/>

Indices and tables
==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
```

La documentation est déployée sur *Pages* à chaque `git push` sur la branche principale grâce à l'intégration continue mise en place.


## Utiliser le *template* lors de la création d'un nouveau projet

à écrire, à mettre en place, etc.



## Intégrer le déploiement de documentation à un projet déjà existant

### Le projet ne contient pas de *pipeline* d'intégration continue

1. Copier tout le contenu du répertoire `documentation` à la racine du projet;

2. Ajouter le fichier `.gitlab-ci.yml` à la racine du projet;

3. Ajouter les informations liées au projet;

   Dans le fichier `documentation/conf.py`, éditer les lignes suivantes :

   ```python
   # -- Project information -----------------------------------------------------

   project = 'Template de déploiement de documentation en HTML'
   copyright = '2024, ISIR, Sorbonne Université, CNRS, INSERM' 
   author = 'Author'
   release = '0.1'
   ```

4. Ajouter votre documentation.

   - Effacer les fichiers du répertoire `content`;
   - Ecrivez de jolis fichiers *Markdown*;
   - Modifier le fichier `index.rst` pour intégrer ces fichiers.

### Le projet contient déjà une *pipeline* d'intégration continue

à écrire



## Références

1. Il faut mettre en place un *pipe* d'intégration continue : fichier `.gitlab-ci.yml`.

Mermaid example : https://github.com/mgaitan/sphinxcontrib-mermaid

Puis faire la configuration de Sphinx : `conf.py`, `Makefile` et `make.bat` (tout ça provient de la documentation de Sphinx)

2. Créer des fichiers dans lesquels on écrit notre belle documentation : dans `content`.

    - Titre de niveau 1 `# Titre de niveau 1` dans chaque fichier Markdown pour que ça s'affiche sur le côté.

3. Ajouter tous ces fichiers dans l'index.

    
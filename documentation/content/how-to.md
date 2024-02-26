# Comment générer la documentation ?

Il y a principalement deux manières d'utiliser ce *template* :

1. comme *template* lors de la création d'un dépôt (oas encore réalisé);
2. en ajoutant certains éléments à un dépôt gitlab déjà existant.

La base de ces deux manières de l'utiliser est commune : **on écrit des fichiers avec le langage *Markdown* qu'on vient ajouter à un index**.

Les fichiers ainsi que les figures doivent se trouver dans le répertoire `documentation/content`. 

Dans le cas de ce *template*, nous avons les fichiers suivants :

```bash
[...]
├── content
│   ├── conf.py
│   ├── fancy-diagrams.md
│   ├── figures
│   ├── how-to.md
│   ├── index.rst
│   ├── markdown.md
│   ├── overview.md
│   └── pages-config.md
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

   overview.md
   how-to.md
   markdown.md
   pages-config.md
   fancy-diagrams.md

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

**La documentation est déployée sur *Pages* à chaque `git push` sur la branche principale** grâce à l'intégration continue mise en place.
Pour vérifier le résultat avant de *push*, il est aussi possible de générer les pages HTML en local.


## Utiliser le *template* lors de la création d'un nouveau projet

à écrire, à mettre en place, etc.



## Intégrer le déploiement de documentation à un projet déjà existant

### Le projet ne contient pas de *pipeline* d'intégration continue

1. Copier tout le contenu du répertoire `documentation` à la racine du projet;

2. Ajouter le fichier `.gitlab-ci.yml` à la racine du projet;

Ensuite, tout se déroule dans le répertoire `documentation/content`.

*Remarques* : il faut cependant garder les autres fichiers et répertoires.
- *_static* et *_templates* contiennent les fichiers permettant de générer les pages HTML avec la charte graphique de l'ISIR;
- *make.bat*, *Makefile* et *requirements.txt* sont indispensables pour la compilation de documentation.

3. Dans le fichier `documentation/content/conf.py`, éditer les lignes suivantes pour renseigner les informations relatives au projet :

   ```python
   # -- Project information -----------------------------------------------------

   project = 'Template de déploiement de documentation en HTML'
   copyright = '2024, ISIR, Sorbonne Université, CNRS, INSERM' 
   author = 'Author'
   release = '0.1'
   ```

4. Ajouter la documentation.

   - Effacer les fichiers *.md* et le répertoire `img` du répertoire `content`;
   - Ecrivez de jolis fichiers *Markdown* dans ce même répertoire;
   - Modifier le fichier `index.rst` pour intégrer ces fichiers.

### Le projet contient déjà une *pipeline* d'intégration continue

On reprend les mêmes étapes que pour le projet sans *pipeline* d'intégration continue à une différence près :

Au lieu de copier le fichier `.gitlab-ci.yml`, on ajoute le contenu relatif au déploiement sur pages.

```yml
pages:
stage: deploy
script:
- pip install -U sphinx
- pip install -r ./documentation/requirements.txt
- sphinx-build -b html ./documentation public
artifacts:
   paths:
   - public
rules:
   - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

## Générer la documentation en local

Ce *template* permet de déployer la documentation sur *Pages* à chaque `git push` sur la branche principale.
Il est aussi possible de générer les pages HTML en local.

Voici la démarche à suivre :

1. Créer un environnement virtuel qui contient toutes les dépendances nécessaires (à faire juste une fois);

   ```bash
   # création de l'environnement
   $ python3 -m venv sphinx_env

   # se placer dans l'environnement
   $ source sphinx_env/bin/activate

   # installer les dépendances
   $ python3 -m pip install -U sphinx
   $ python3 -m pip install -r requirements.txt
   ```

2. Sourcer l'environnement virtuel;

   ```bash
   $ source sphinx_env/bin/activate
   # on doit trouver (sphinx_env) avant le prompt
   (sphinx_env) ➜  documentation git:(main)
   ```

3. Générer les pages HTML dans le répertoire `documentation/_build`;

   ```bash
   $ cd $PROJET_DIR/documentation
   $ sphinx-build -b html content _build
   ```

4. Ouvrir la documentation dans le navigateur : fichier `index.htlm` dans `documentation/_build`.


## Références

1. Il faut mettre en place un *pipe* d'intégration continue : fichier `.gitlab-ci.yml`.

Mermaid example : https://github.com/mgaitan/sphinxcontrib-mermaid

Puis faire la configuration de Sphinx : `conf.py`, `Makefile` et `make.bat` (tout ça provient de la documentation de Sphinx)

2. Créer des fichiers dans lesquels on écrit notre belle documentation : dans `content`.

    - Titre de niveau 1 `# Titre de niveau 1` dans chaque fichier Markdown pour que ça s'affiche sur le côté.

3. Ajouter tous ces fichiers dans l'index.

    
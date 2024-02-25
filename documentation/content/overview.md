# Vue d'ensemble du *template*

## Motivation

Ce *template* a été créé pour permettre de générer automatiquement de la documentation sous forme de pages web avec très peu d'efforts. Le contenu des pages web est automatiquement généré avec *Sphinx* en s'appuyant sur des fichiers écrits en *Markdown*.

## Charte graphique

Le template suit la charte graphique de l'ISIR, à savoir :

- Police : *Lato*
- Couleurs :

    <table align="center">
        <tr>
            <th>
                <svg height = "40" width = "200" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="20" cy="20" r="20" fill="#0090CD" />
                </svg>
            </th>
            <th>
                <svg height = "40" width = "40" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="20" cy="20" r="20" fill="#012235" />
                </svg>
            </th>
        </tr>
        <tr>
            <td>CMJN : 100 ; 30 ; 0 ; 20</td>
            <td>CMJN : 98 ; 36 ; 0 ; 79</td>
        </tr>
        <tr>
            <td>RVB : 0 ; 144 ; 205</td>
            <td>RVB : 1 ; 34 ; 53</td>
        </tr>
        <tr>
            <td>Hexa : #0090CD</td>
            <td>Hexa : #012235</td>
        </tr>
    </table>

- Logos : Les logos du laboratoire et des tutelles sont dans le pied de page.

<table align="center" style="width: 100%">
    <tr>
        <th>
            <img src="/_static/logos/logo-isir.png"/>
        </th>
        <th>
            <img src="/_static/logos/logo-su.png"/>
        </th>
        <th>
            <img src="/_static/logos/logo-cnrs.png"/>
        </th>
        <th>
            <img src="/_static/logos/logo-inserm.png"/>
        </th>
    </tr>
</table>

<table align="center" style="width: 100%">
    <tr>
        <th>
            <img src="./figures/logos/logo-isir.png"/>
        </th>
        <th>
            <img src="./figures/logos/logo-su.png"/>
        </th>
        <th>
            <img src="./figures/logos/logo-cnrs.png"/>
        </th>
        <th>
            <img src="./figures/logos/logo-inserm.png"/>
        </th>
    </tr>
</table>

![test image](./figures/logos/logo-isir.png)

##  Références

Le contenu de ce *template* est très fortement inspiré des ressources mises à disposition par *CodeRefinery* :
- [CodeRefinery - Sphinx and Markdown](https://coderefinery.github.io/documentation/sphinx/)
- [CodeRefinery - Deploying Sphinx documentation to GitHub Pages](https://coderefinery.github.io/documentation/gh_workflow/)

Il utilise le thème fourni par [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.org), dont les couleurs et la police ont été modifiées pour respecter la charte graphique de l'ISIR.
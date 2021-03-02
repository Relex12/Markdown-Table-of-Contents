# Markdown-Table-of-Contents
Outil Python pour compiler des Tables des Matières avec liens hypertextes en Markdown (GitHub-Flavoured-Markdown)

![](https://img.shields.io/badge/status-In_Progress-green) ![](https://img.shields.io/github/license/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/repo-size/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/languages/top/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/last-commit/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/stars/Relex12/Markdown-Table-of-Contents)



Regarder sur GitHub:

[![Markdown-Table-of-Contents](https://github-readme-stats.vercel.app/api/pin/?username=Relex12&repo=Markdown-Table-of-Contents)](https://github.com/Relex12/Markdown-Table-of-Contents)

[Voir en Anglais.](https://relex12.github.io/Markdown-Table-of-Contents)

---

## Sommaire

[toc]

## Qu'est-ce que c'est ?

**N'avez-vous jamais été frustré de ne pas pouvoir créer de table des matières dynamiques en Markdown ?**

C'est à ça que sert cet outil. En **une seule commande**, vous pouvez créer une **table des matières avec liens hypertextes** directement dans votre fichier Markdown.

## Comment ça marche ?

Dans votre fichier Markdown, ajoutez une **balise table des matières** (ou balise TOC) là où vous voulez créer la table des matières, puis exécutez Markdown-Table-of-Contents sur votre fichier. La ligne contenant la balise TOC sera supprimée et à la place sera insérée la table des matières avec liens hypertextes générée.

Une **balise TOC** est une chaîne de caractère `toc`, tout en majuscules ou tout en minuscules, entourée d'une simple ou d'une double paire de crochets, ce qui signifie que seuls `[TOC]`, `[[TOC]]`, `[toc]` et `[[toc]]` sont des balises TOC valides.

Cette méthode est déjà utilisée par de nombreux éditeurs Markdown (Typora, Markdown Monster) et outils (doctoc), mais ceci est le premier outil de ligne de commande léger en Python simple d'utilisation à ajouter cette fonctionnalité à Github-Flavored-Markdown.

## Comment l'utiliser ?

En deux étapes :

1. installez Markdown-Table-of-Contents en clonant le dépôt : `git clone https://github.com/Relex12/Markdown-Table-of-Contents.git`
2. lancez le script sur votre fichier Markdown : `python3 toc.py FileName.md` (les chemins vers `toc.py` et votre fichier peuvent être en relatif ou absolu)

## Arguments pour la ligne de commande

Voici le résultat de la commande `python toc.py -h`:

```
usage: toc.py [-h] [-o OUTPUT] [--depth {1,2,3,4,5,6}] [--ignore-begin]
              FileName

positional arguments:
  FileName              input Markdown file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file to write in, default overwrites FileName
  --depth {1,2,3,4,5,6}
                        maximum heading depth, default is 6
  --ignore-begin        ignore headings before the TOC tag
```

## Spécifications

La ligne qui contient la balise TOC **DOIT** commencer par `[TOC]`, `[[TOC]]`, `[toc]` or `[[toc]]`, ce qui veut dire qu'il **NE DOIT PAS** y avoir d'espace blanc entre la précédente fin de ligne et le premier crochet `[`.

La ligne qui contient la balise TOC sera retirée en entier, ce qui veut dire que tout caractère entre le dernier crochet`]` et la fin de ligne sera supprimé en même temps que la balise TOC.

La balise TOC **DOIT** être l'un de ceux-ci : `[TOC]`, `[[TOC]]`, `[toc]` or `[[toc]]`. Même si `[TOC]]` et `[toc]]` **POURRAIENT** marcher, ils **NE DEVRAIENT PAS** être utilisés.

S'il y a plus d'une ligne contenant une balise TOC dans tout le fichier, seule la première sera remplacée par la table des matières générée. Toutes les autres balises TOC seront ignorées, ce qui veut dire qu'elles seront toujours dans le fichier après exécution. Si vous souhaitez remplacer chaque balise TOC, vous **DEVRIEZ** exécuter le script plusieurs fois.

Pour être interprétée comme un titre, une ligne contenant un titre **DOIT** possède un espace blanc (au minimum un caractère espace) entre les dièses `#` et le libellé du titre. Cependant, vous **NE DEVRIEZ PAS** utiliser plus qu'un seul caractère espace, car tous les caractères entre le premier espace blanc et la fin de ligne (exclus) sont utilisés comme libellé et valeur du lien hypertexte (sans compter les modifications).

Le libellé du titre est modifié dans la valeur du lien hypertexte pour être correctement interprété comme une URL de lien vers un paragraphe : les caractères espaces sont remplacés par des tirets `-`, les points d'interrogation `?` et les points d'exclamations `!` sont supprimés sans être remplacés. Vous **NE DEVRIEZ PAS** utiliser d'autres espaces blancs que les caractères espaces (telles que les tabulations) dans les lignes contenant un titre. Certains caractères spéciaux tels que les dièses `#`, les esperluettes `&` et d'autres **POURRAIENT** causer des comportements inattendus, notamment une fois uploadé sur GitHub. Les espaces blancs (caractères espace compris) juste avant la fin de ligne **POURRAIENT** également causer des comportements inattendus. Si vous trouvez l'un de ces comportements, s'il-vous-plaît déclarez-le (Open an Issue).

L'indentation des différents niveaux de liste utilise quatre caractères espace pour chaque indentation suppérieur, on partant de 0 espace pour les titres de niveau 1, 4 espaces pour les titres de niveau 2, jusqu'à 24 espaces pour les titres de niveau 6. Après ces espaces, il y a une astérisque `*` suivie d'un unique caractère espace puis un crochet `[`. Jusqu'au prochain crochet `]` se trouve la ligne contenant le titre (chaque caractère de la ligne entre le premier espace blanc et la fin de ligne exclus). Après le crochet, une parenthèse `(` et un dièse `#`, ensuite la ligne du titre modifiée jusqu'à la parenthèse finale `)`. Comme la fin de ligne est supprimée de la ligne du titre, une autre fin de ligne est ajoutée après la parenthèse finale.

Les fin de lignes sont supposées être longues d'un caractère, considérées comme étant LF (`\n`). Ce qui veut dire que seulement un caractère est enlevée à la fin de la ligne du titre avant d'être utilisée comme libellé du lien hypertexte et modifiée comme valeur du lien. Cependant, cela **POURRAIT** fonctionner avec des fins de lignes CRLF. De la même manière, seulement un caractère LF est inséré à la fin des lignes de la table des matières générée.

## Fonctionnalités manquantes

Seus les titres sous forme de dièses sont inclus dans la table des matières générée, ce qui exclu les formes soulignées avec des symbole égal `=` et des tirets `-` et avec des balises HTML `<h1>...</h1>`. L'implémentation devrait aussi considérer les dièses à droite juste avant la fin de ligne comme faisant partie de la syntaxe et les enlever. De nombreuses autres spécifications sont censées être respectées et ne le sont pas. Voir les spécifications de Github-Flavored-Markdown [ici](https://github.github.com/gfm).

Aussi, la liste des comportements inattendus à cause des caractères spéciaux n'existe pas : si quelque chose d'étrange se produit, pensez d'abord aux caractères spéciaux.

## License

Ce projet est un petit projet. Le code source est donné librement à la communauté GitHub, sous la seule licence MIT, qui n'est pas trop restrictive.

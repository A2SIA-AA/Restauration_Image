# Méthodes directes & itératives pour la résolution de systèmes linéaires  
## Application : restauration d’image par inpainting

Projet universitaire – GM3  
*Auteurs : Doubli Hoda, Ait Taleb Assia (INSA Rouen)*  
*Décembre 2023*

---

## 1. Objectif

1. **Comparer** plusieurs algorithmes de résolution de systèmes linéaires :  
   - méthodes *dites directes* (factorisation) ;  
   - méthodes **itératives** : Jacobi, Descente de gradient, Gradient conjugué.
2. **Appliquer** ces méthodes à un problème d’**inpainting** : reconstruire une image
   en niveaux de gris dont certains pixels ont été masqués.

---

## 2. Contenu du dépôt

| Fichier / dossier        | Rôle                                                                 |
|--------------------------|----------------------------------------------------------------------|
| `main.py`                | Point d’entrée : lance les expériences numériques                   |
| `algo.py`                | Implémentations : Jacobi, Gradient, Gradient conjugué               |
| `affichage.py`           | Fonctions d’affichage des courbes                                   |
| `data.py`                | Méthodes de calculs nécessaire au projet                            |
| `Mask.txt`               | Matrice binaire                                                     |
| `Img_AltGray.png`        | Image altérée (entrée de l’inpainting)                              |
| `Img_Recons.png`         | Image restaurée (exemple de sortie)                                 |
| `Doubli_Ait-taleb.pdf`   | Rapport complet (théorie, démonstrations, résultats)                |

---

## 3. Architecture logique

```

.
├─ algo.py          # Algorithmes itératifs
├─ data.py          # Construction A, b et produit Ax
├─ affichage.py     # Helpers graphiques (matplotlib)
├─ main.py          # Scénarios : benchmark + inpainting

````

Les calculs évitent tout stockage explicite de la matrice **A** :  
seul un produit « matrice × vecteur » optimisé (vectorisation NumPy + slicing)
est utilisé, crucial pour de grandes résolutions (4032 × 3024).

---

## 4. Dépendances

- Python ≥ 3.9  
- NumPy  
- Matplotlib


---

## 5. Principaux résultats

| Méthode              | Convergence (N = 200, α = 1) | Inpainting (4032 × 3024)    | Temps/itération\* |
| -------------------- | ---------------------------- | --------------------------- | ----------------- |
| Jacobi               | Lente, mais stable           | Bonne si `iters` ≥ 400      | **\~0.07 s**      |
| Descente de gradient | Sensible au pas ; α > 0 ok   | Acceptable (flou ↗ pour R↑) | \~0.10 s          |
| Gradient conjugué    | Converge < 60 iters          | Rendu net dès 30 iters      | \~0.15 s          |

\* Mesures indicatives sur CPU i7-11xxx.

---

## 6. À retenir

* **Gradient conjugué** est le plus efficace pour les matrices symétriques définies positives ; il conver­git en O(N) itérations au plus (théorie), bien avant la limite dans la pratique.
* Le **choix du coefficient de régularisation R** influe sur la netteté :

  * trop faible → artefacts ;
  * trop élevé → lissage excessif (flou).
* La **vectorisation NumPy** (aucune boucle Python) est vitale : gain ×30 vs naïf.

---

> Pour plus de détails mathématiques (démonstrations, matrices de Toeplitz,
> calcul des valeurs propres, influence de α et N, etc.), consultez le rapport
> [`Doubli_Ait-taleb.pdf`](Doubli_Ait-taleb.pdf).

```

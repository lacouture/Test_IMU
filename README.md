Programme de test de l'IMU MPU6090
==================================

Ceci est un simple programme Micropython de test de l'IMU MPU6090 pour Raspberry Pi Pico.

[MPU 6090 Datasheet](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf)

Il affiche en boucle les angles de tangage ("Pitch") et de roulis ("Roll") de l'IMU.

Une fois installé dans le Pico, il faut importer le module `test_imu` pour qu'il
démarre:

```
>>> import test_imu
Unexpected chip ID: 0x70. Possible clone chip?
Pitch, Roll:  -0.004   0.005
Pitch, Roll:  -1.733   3.254
Pitch, Roll:   0.243  -1.380
Pitch, Roll:  -0.235   1.919
Pitch, Roll:  -4.342  -0.428
Pitch, Roll:  -0.657   0.703
Pitch, Roll:  -3.088   3.748
Pitch, Roll:   0.184   0.188
[...]
```

(Le message "Unexpected chip ID: 0x70. Possible clone chip?"
ci-dessus est un simple avertissement, il n'empêche pas
nécessairement le fonctionnement.)

Dépendances
-----------
Ce programme dépend de deux librairies de Peter Hinch:
- [micropython-mpu9x50](https://github.com/micropython-IMU/micropython-mpu9x50.git)
- [micropython-fusion](https://github.com/micropython-IMU/micropython-fusion.git)

`micropython-mpu9x50` permet de communiquer avec l'IMU et de lire les valeurs brutes
des vecteurs d'accélération linéaire (accéléromètre) et angulaire (gyroscope).

`micropython-fusion` permet de transformer ces valeurs brutes d'accélération en
angles (tangage, roulis). Cet IMU n'étant pas équipé d'un magnétomètre (boussole),
il n'est pas possible de calculer le troisième angle (cap).

Préparation de l'environnement de travail
-----------------------------------------

### En utilisant les sous-modules git

Après avoir cloné ce dépôt, initialiser les sous-modules `micropython-mpu9x50` et
`micropython-fusion` avec les commandes suivantes:

```bash
git submodule update --init
```

(ou utiliser la fonction équivalente de votre client Git préféré)

Ceci crée deux sous-répertoires `micropython-mpu9x50` et `micropython-fusion` contenant
les librairies.

### En clonant manuellement les Dépendances

Cloner les deux librairies indiquées ci-dessus manuellement dans les sous-répertoires
correspondants.

Installation dans le Pico
-------------------------

Installer Micropython dans le Pico si nécessaire.

Copier les fichiers suivants dans le répertoire `/lib` du Pico:

* `micropython-mpu9x50/imu.py`
* `micropython-mpy9x50/vector3d.py`
* `micropython-fusion/deltat.py`
* `micropython-fusion/fusion.py`

Copier le fichier suivant dans le répertoire racine `/` du Pico:

* `test_imu.py`

Si vous disposez de `mpremote` sur Linux, vous pouvez installer ces fichiers
automatiquement en lançant le script `install.sh`.

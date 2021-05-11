# 1. créer les dossiers egs dans le dépot -> OK
# 2. donner en argument le réperoire du dataset (on suppose que ce dernier a au moins les reps train/(noisy,clean))
# et test(clean,nosiy)

#!/usr/bin/env python
import sys

#print(sys.argv[1])
noisy_train=sys.argv[1]+"/train/noisy" # if sys.argv[1] se termie par "/", alors delete le "/" devant train
print(noisy_train)
#filesystem python
clean_train=sys.argv[1]+"/train/clean"
noisy_test=sys.argv[1]+"/test/noisy"
clean_test=sys.argv[1]+"/test/clean"
#noisy_dev=path to valentini
#clean_dev=path to valentini

#le rep courant est denoiser
denoiser.audio noisy_train > egs/val/tr/noisy.json


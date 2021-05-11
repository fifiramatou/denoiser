
path=$1
echo $path #chemin du dataset
noisy_train= $path + "/train/noisy"
#if [[ ! -e $path ]]; then
 #   mkdir -p $path
#fi
python3 -m denoiser.audio $noisy_train > egs/val/train/noisy.json 
#python3 -m denoiser.audio dataset/debug/clean > $path/clean.json
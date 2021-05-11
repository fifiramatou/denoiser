
noisy_path=$1
echo $noisy_train_path #chemin du dataset
#noisy_train= $path #$path + "/train/noisy"
#if [[ ! -e $path ]]; then
 #   mkdir -p $path
#fi
egs_path = "egs/val/train"
if [[ ! -e $egs_path ]]; then
   mkdir -p $egs_path
fi
python3 -m denoiser.audio $noisy_train_path > $path/noisy.json 
#python3 -m denoiser.audio dataset/debug/clean > $path/clean.json
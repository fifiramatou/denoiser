
noisy_path=$1
echo $noisy_train_path #chemin du dataset
#noisy_train= $path #$path + "/train/noisy"
#if [[ ! -e $path ]]; then
 #   mkdir -p $path
#fi
python3 -m denoiser.audio $noisy_train_path > egs/val/train/noisy.json 
#python3 -m denoiser.audio dataset/debug/clean > $path/clean.json
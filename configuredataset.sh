noisy_train_path=$1
egs_path=egs/val/train
echo $noisy_train_path 
#chemin du dataset

if [[ ! -e $egs_path ]]; then
   mkdir -p $egs_path
fi
python3 -m denoiser.audio $noisy_train_path > $egs_path/noisy.json 
#python3 -m denoiser.audio dataset/debug/clean > $path/clean.json
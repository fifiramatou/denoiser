#nom du dataset
dataset_name=$1
echo "Nom du dataset:"$dataset_name 
#dataset_path=/kaggle/input/$dataset_name
dataset_path=/content/$dataset_name
echo "Répertoire du dataset:"$dataset_path
#noisy_train_path=$1
#egs_path=egs/val/train
egs_path="egs/{$dataset_name}"
echo $egs_path
if [[ ! -e $egs_path ]]; then
   mkdir -p $egs_path
fi
python3 -m denoiser.audio $dataset_path/train/clean > $egs_path/tr/clean.json
python3 -m denoiser.audio $dataset_path/train/noisy > $egs_path/tr/noisy.json 

python3 -m denoiser.audio $dataset_path/test/clean > $egs_path/tt/clean.json
python3 -m denoiser.audio $dataset_path/test/noisy > $egs_path/tt/noisy.json 
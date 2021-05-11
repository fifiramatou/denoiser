#nom du dataset
dataset_name=$1
echo "Nom du dataset:"$dataset_name 
#dataset_path=/kaggle/input/$dataset_name
dataset_path=/content/$dataset_name
echo "Répertoire du dataset:"$dataset_path
#noisy_train_path=$1
#egs_path=egs/val/train
egs_path_tr=egs/$dataset_name/tr
echo $egs_path_tr
egs_path_tt=egs/$dataset_name/tt
echo $egs_path_tt
if [[ ! -e $egs_path_tr ]]; then
   mkdir -p $egs_path_tr
fi
if [[ ! -e $egs_path_tt ]]; then
   mkdir -p $egs_path_tt
fi 

python3 -m denoiser.audio $dataset_path/train/clean > $egs_path_tr/clean.json
python3 -m denoiser.audio $dataset_path/train/noisy > $egs_path_tr/noisy.json 

python3 -m denoiser.audio $dataset_path/test/clean > $egs_path_tt/clean.json
python3 -m denoiser.audio $dataset_path/test/noisy > $egs_path_tt/noisy.json 
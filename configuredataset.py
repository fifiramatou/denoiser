#!/usr/bin/env python
import getopt
import sys
import os
import yaml
from yaml import SafeDumper
def remove_prefix(text, prefix):
    return text[len(prefix):] if text.startswith(prefix) else text

def gen_conf_yaml(dataset):
    config = [{'dset': [{'train': 'egs/'+dataset+"/tr"}, {'valid': None}, {'test': 'egs/'+dataset+'/tt'}, {'noisy_json': 'egs/'+dataset+'/tr/noisy.json'}, {'noisy_dir': No>                        {'matching': 'sort'}]}, {'eval_every': 2}]
    SafeDumper.add_representer(type(None), lambda dumper,
                               value: dumper.represent_scalar(u'tag:yaml.org,2002:null', ''))
    with open("conf/dset/"+dataset+'.yaml', 'w') as f:
        yaml.safe_dump(config, f, default_flow_style=False)


def make_json_for_dataset(platform, dataset_path):
    dataset=remove_prefix(dataset_path,'denoising-audio/datasetV2.01_test_train/')
    root = ""
    if platform == "kaggle":
        root = "/kaggle/input/"
    elif platform == "colab":
        root = "/content/"
    else:
        print("Unrecognized platform")
        sys.exit()

    noisy_train = root+dataset_path+"/train/noisy"
    clean_train = root+dataset_path+"/train/clean"
    noisy_test = root+dataset_path+"/test/noisy"
    clean_test = root+dataset_path+"/test/clean"
    print(clean_test)
    # le rep courant est denoiser #denoiser.audio noisy_train > egs/val/tr/noisy.json
    egs_path_tr = "egs/"+dataset+"/tr"
        egs_path_tt = "egs/"+dataset+"/tt"
    try:
        os.makedirs(egs_path_tr)
        os.makedirs(egs_path_tt)
        # audio.main($clean_train)
        command_clean_train = "python3 -m denoiser.audio " + clean_train + " > " + egs_path_tr+"/clean.json"
        print(command_clean_train)
        os.system(command_clean_train)
        command_noisy_train = "python3 -m denoiser.audio " + noisy_train + " > " + egs_path_tr+"/noisy.json"
        print(command_noisy_train)
        os.system(command_noisy_train)
        command_clean_test = "python3 -m denoiser.audio " + clean_test + " > " + egs_path_tt+"/clean.json"
        print(command_clean_test)
        os.system(command_clean_test)
        command_noisy_test = "python3 -m denoiser.audio " + noisy_test + " > " + egs_path_tt+"/noisy.json"
        print(command_noisy_test)
        os.system(command_noisy_test)
        print("JSON files successfully generated!")
    except OSError as e:
        print("Creation of the directories %s failed" % egs_path_tr)
        print(e)
        sys.exit()


def main():
    argumentList = sys.argv[1:]  # le chemin du dataset et la plateforme
    if len(sys.argv) < 5:
        print("Incorrect number of arguments. Usage example: configuredataset.py -p your_platform -d your_dataset_name ")
        sys.exit()
    options = "p:d:"
    long_options = ["platform=", "dataset="]
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        print(arguments)
        dataset_path = ""
        platform = ""
        for current_argument, current_value in arguments:
            if current_argument in ("--dataset", "-d"):
                dataset_path = current_value
            elif current_argument in ("--platform", "-p"):
                if current_value in ("kaggle", "colab"):
                    platform = current_value
                else:
                    print("ERROR: Unrecognized platform!")
                    sys.exit()
        print("platforme: " + platform + " and dataset: " + dataset_path)
        make_json_for_dataset(platform, dataset_path)
        print("Creation of the config YAMl file...")
        dataset=remove_prefix(dataset_path,'denoising-audio/datasetV2.01_test_train/')
        gen_conf_yaml(dataset)
    except getopt.GetoptError as e:
        print(e)
        sys.exit()


if __name__ == "__main__":
    main()
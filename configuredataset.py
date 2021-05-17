#!/usr/bin/env python
import getopt
import sys
import os
import yaml
from yaml import SafeDumper


def gen_conf_yaml(dataset):
    config = [{'dset': [{'train': 'egs/'+dataset+"/tr"}, {'valid': None}, {'test': 'egs/'+dataset+'/tt'}, {'noisy_json': 'egs/'+dataset+'/tr/noisy.json'}, {'noisy_dir': None}, {'matching': 'sort'}]}, {'eval_every': 2}]
    SafeDumper.add_representer(type(None), lambda dumper,
                               value: dumper.represent_scalar(u'tag:yaml.org,2002:null', ''))
    with open("conf/dset/"+dataset+'.yaml', 'w') as f:
        yaml.safe_dump(config, f, default_flow_style=False)


def make_json_for_dataset(platform, dataset):
    root = ""
    if platform == "kaggle":
        root = "/kaggle/input/"
    elif platform == "colab":
        root = "/content/"
    else:
        print("Unrecognized platform")
        sys.exit()

    noisy_train = root+dataset+"/train/noisy"
    clean_train = root+dataset+"/train/clean"
    noisy_test = root+dataset+"/test/noisy"
    clean_test = root+dataset+"/test/clean"
    print(clean_test)
    egs_path_tr = "egs/"+dataset+"/tr"
    egs_path_tt = "egs/"+dataset+"/tt"
    try:
    	os.makedirs(egs_path_tr)
        os.makedirs(egs_path_tt)
        # audio.main($clean_train)
        command = "python3 -m denoiser.audio " + clean_train + " > " + egs_path_tr+"/clean.json"
        print(command)
        os.system(command)

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
        dataset = ""
        platform = ""
        for current_argument, current_value in arguments:
            if current_argument in ("--dataset", "-d"):
                dataset = current_value
            elif current_argument in ("--platform", "-p"):
                if current_value in ("kaggle", "colab"):
                	                    platform = current_value
                else:
                    print("ERROR: Unrecognized platform!")
                    sys.exit()
        print("platforme: " + platform + " and dataset: " + dataset)
        make_json_for_dataset(platform, dataset)
        print("Creation of the config YAMl file...")
        gen_conf_yaml(dataset)
    except getopt.GetoptError as e:
        print(e)
        sys.exit()


if __name__ == "__main__":
    main()

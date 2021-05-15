
#!/usr/bin/env python
import getopt
import sys
import os
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
    # if sys.argv[1] se termie par "/", alors delete le "/" devant train
    clean_train = root+dataset+"/train/clean"
    noisy_test = root+dataset+"/test/noisy"
    clean_test = root+dataset+"/test/clean"
    print(clean_test)
    # le rep courant est denoiser #denoiser.audio noisy_train > egs/val/tr/noisy.json
    egs_path_tr = "egs/"+dataset+"/tr"
    egs_path_tt = "egs/"+dataset+"/tt"
    try:
        os.makedirs(egs_path_tr)
        os.makedirs(egs_path_tt)
    except OSError:
        print("Creation of the directories %s failed" % egs_path_tr)
        #sys.exit()
    try:
        os.system("python3 -m denoiser.audio $clean_train > $egs_path_tr/clean.json")
        # python3 -m denoiser.audio $noisy_train > $egs_path_tr/noisy.json

        # python3 -m denoiser.audio $clean_test > $egs_path_tt/clean.json
        # python3 -m denoiser.audio $noisy_test > $egs_path_tt/noisy.json
    except OSError as e:
        print(e)
        sys.exit()
    print("JSON files successfully generated!")


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
    except getopt.GetoptError as e:
        print(e)
        sys.exit()


if __name__ == "__main__":
    main()


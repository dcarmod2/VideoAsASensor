# Dongjun Seung (dongjun2)
# 3/07/2018
# dongjun2@illinois.edu

import os
import json
import shutil

# The main function calls the generic detect function of darknet using the default yolo
# cfg and weight files to generate all detected people and bicycles in json.
# This json file is then used in the person_on_bike.py script to create a json file
# that contains all 'person and bike' pairs.

def main():
    current_dir = os.getcwd()
    training_images = os.path.join(current_dir, "training_images")

    # if the "training_images" folder does not exist, then let the user know to put images in there
    if not os.path.exists(training_images):
        os.mkdir("training_images")
        print ("-------------------------------------------")
        print ("--Put Images in the training_images folder--")
        print ("-------------------------------------------")
        return

    # create a folder named "training_json," where all the json files will be saved
    training_json = os.path.join(current_dir, "training_json")
    if not os.path.exists(training_json):
        os.mkdir("training_json")

    for image in os.listdir("./training_images"):

        os.system("./darknet detect cfg/yolo.cfg yolo.weights training_images/{}".format(image))

        image_name = image[:len(image) - 4]
        shutil.copyfile("detectionfile.json", os.path.join(training_json, "{}_1.json".format(image_name)))

        os.chdir("scripts")
        os.system("python person_on_bike.py")

        os.rename("cyclist.json", "{}_2.json".format(image_name))
        os.chdir('..')

    # send all json files that have detected 'bike and person' pairs to the "training_json" folder
    transfer_from = os.path.join(current_dir, "scripts")
    for json_file in os.listdir("./scripts"):
        if json_file[len(json_file) - 4:] == "json":
            shutil.move(os.path.join(transfer_from, json_file), training_json)


if __name__ == "__main__":
    main()

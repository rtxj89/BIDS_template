# This is the configuration file for the dcm2bids_helper script,
# which will use the dcm2bids_helper to create json files
# for use in creating the study specific configuration file
#
# See the dcm2Bids repo for instructions to create the config file:
# https://github.com/cbedetti/Dcm2Bids
#
# More detailed instructions for using these scripts here:
# https://github.com/kdestasio/dcm2bids

import os

# Specify the path where the workshop repository lives
repo_path = "/Users/[Current_Directory_Path]"

# Set directories
# These variables are used in the main script and need to be defined here. They need to exist prior to running the script
dicomdir = os.path.join(repo_path, "data", "dicoms")
niidir = os.path.join(repo_path, "data", "BIDS_data") # where the niftis will be put
codedir = os.path.join(repo_path, "Scripts") # Contains subject_list.txt, config file, and dcm2bids_batch.py
logdir = os.path.join(codedir, "logs_helper")

# Set error log outputs
outputlog = os.path.join(logdir, "outputlog_helper.txt")
errorlog = os.path.join(logdir, "errorlog_helper.txt")

# Set test subject
test_subject = "[SUBJECT DICOM FOLDER NAME" # Name of a directory that contains DICOMS for one participant

# Run on local machine (run_local = True) or high performance cluster with slurm (run_local = False)
run_local = True

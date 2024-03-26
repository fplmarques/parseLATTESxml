#!/bin/bash
#
## This script exapand LATTES curricula downloaded from CNPq
## and rename it as <lattes_id>.xml 
##
## Usage:
##   execute this script within the directory in which LATTES files (<lattes_id.zip>) were downloaded
#
#        Fernando P.L. Marques (2024)
#

# Step 1: Assign all *.zip files to ZIPFILES
ZIPFILES=$(ls *.zip)

# Step 2: Loop through each zip file
for file in $ZIPFILES; do
    # Step 2a: Get the base name without extension
    base_name=$(basename -s .zip "$file")
    
    # Step 2b: Unzip the file
    unzip "$file"
    
    # Step 2c: Rename curriculum.xml to base_name.xml
    mv curriculo.xml "${base_name}.xml"
done
echo "All done!!!"

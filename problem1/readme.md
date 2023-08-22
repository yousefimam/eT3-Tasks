# Problem 1: Extracting Images and Gathering Information from a Dataset
## Introduction
This technical documentation outlines the solution to the task of extracting images from various folders and sub-folders,
consolidating them into a single folder, and then gathering image metadata including names, sizes, and modification dates.
The provided Python script automates this process.

## Solution Overview
The solution involves using the provided Python script to recursively traverse through source folders, extract images, rename them, and gather relevant metadata. The code consists of three main functions:

move_files: Moves and renames images from the source folders to the destination folder.
convert_bytes: Converts file size from bytes to human-readable formats.
write_csv: Creates a CSV file with image metadata.

## Configuration
- Set the source folder path by replacing "Write the src folder path" with the path of the folder containing the source images.
- Set the destination folder path by replacing "Write the dest folder path" with the path of the folder where images will be consolidated.
- Set the type of files to be moved and processed (e.g., "image|text"), and update the file extension accordingly.
- Set the dataset folder's path by replacing "Write the dataset folder's path" with the path where the metadata CSV file will be created.

## Output
Images will be moved and consolidated into the destination folder.
A CSV file named "dataset_images.csv" will be created in the dataset folder, containing image metadata including name, size, and modification date.
Conclusion

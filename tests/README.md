# Tests Conducted

- Using SAM2.1 as a replacement for Centroid ReID
    - Outputs can be seen under `sam2-tests/sam2_outputs` in the submodule.
    - Instructions to run the code are added in a comment at the start of the file `test_player_segmentation.py`

- Using a super-resolution module before the final number prediction, since the crops are very small (around 25x25 pixels)
    - No submodule added yet

- Replacing the STR module with a CNN digit classifier           
    - Training model on Test dataset with cropped frames
    - Training model on Training dataset with full frames
    - Attempting multi-task learning: legibility and number classification

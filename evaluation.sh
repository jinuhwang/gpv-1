#!/bin/bash

# bash exp/gpv/scripts/eval.sh gpv_coco RefCocop test original_split /workspace/data/gpv /workspace/data/gpv/data
# bash exp/gpv/scripts/eval.sh gpv_coco_sce CocoVqa test gpv_split /workspace/data/gpv /workspace/data/gpv/data
bash exp/gpv/scripts/eval.sh gpv_coco_sce CocoCaptioning test gpv_split /workspace/data/gpv /workspace/data/gpv/data

# bash exp/gpv/scripts/eval.sh <exp_name> <task_name> <subset> <split> <output_dir> <data_dir>
# <exp_name>: name of the experiment directory (<output_dir>/<exp_name>) where the model to be evaluated lives.
# <task_name>: set to all to evaluate on all 5 tasks, all_but_refexp to evalute on all tasks excepts RefCocop, or the name of tasks to evaluate only on that task.
# <subset>: set to train or val for COCO (no test since COCO test annotations are hidden) and train, val, or test for COCO-SCE.
# <split>: set to original_split (COCO) or gpv_split (COCO-SCE). This flag is unused for RefCocop.

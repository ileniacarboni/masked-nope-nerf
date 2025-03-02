# A Study of NoPe-NeRF for Novel View Synthesis of Handheld Objects

Based on "NoPe-NeRF: Optimising Neural Radiance Field with No Pose Prior"[https://nope-nerf.active.vision/] (Wenjing Bian et al. 2023)

## How to Replicate
### Installation
```
virtualenv --python python3.8 nope-nerf
source nope-nerf/bin/activate
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

### Data and Preprocessing
#### Segment Anything
Coming Soon
#### Monocular Depth Map Generation
Monocular depth map generation: you can first download the pre-trained DPT model from [this link](https://drive.google.com/file/d/1dgcJEYYw1F8qirXhZxgNK8dWWz_8gZBD/view?usp=sharing) provided by [Vision Transformers for Dense Prediction](https://github.com/isl-org/DPT) to `DPT` directory, then run
```
python preprocess/dpt_depth.py configs/preprocess.yaml
```
to generate monocular depth maps. You need to modify the `cfg['dataloading']['path']` and `cfg['dataloading']['scene']` in `configs/preprocess.yaml` to your own image sequence.

### Training and Evaluation

Train a new model from scratch:

```
python train.py configs/Tanks/Ignatius.yaml
```
where you can replace `configs/Tanks/Ignatius.yaml` with other config files.

You can monitor on <http://localhost:6006> the training process using [tensorboard](https://www.tensorflow.org/guide/summaries_and_tensorboard):
```
tensorboard --logdir ./out --port 6006
```

1. Evaluate image quality and depth:
```
python evaluation/eval.py configs/Tanks/Ignatius.yaml
```
To evaluate depth: add `--depth` . Note that you need to add ground truth depth maps by yourself.

2. Evaluate poses:
```
python evaluation/eval_poses.py configs/Tanks/Ignatius.yaml
```
To visualise estimated & ground truth trajectories: add `--vis` 

## Citation to the Original Work
```
 @inproceedings{bian2022nopenerf,
	author    = {Wenjing Bian and Zirui Wang and Kejie Li and Jiawang Bian and Victor Adrian Prisacariu},
	title     = {NoPe-NeRF: Optimising Neural Radiance Field with No Pose Prior},
	journal   = {CVPR},
	year      = {2023}
	}
```

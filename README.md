# finetune_classification
使用 TensorFlow 进行 finetuning 的通用分类模型

## 使用方式
请参考：[TensorFlow 使用预训练模型 ResNet-50](https://www.jianshu.com/p/0237ebbee5d5)

# not care --images_dir and --annotation_path now
1. python3 generate_tfrecord.py --images_dir ./images --annotation_path ./train_annotations.json --output_path train.record
2. python train.py --record_path train.record --checkpoint_path resnet_v1_50.ckp0t

export DATA_DIR=/data01/dyc/bert_classifier/data
export BERT_BASE_DIR=/data01/dyc/bert_classifier/vocab_file/chinese_L-12_H-768_A-12
python run_classifier.py \
  --task_name=auto \
  --do_train=true \
  --do_eval=true \
  --data_dir=$DATA_DIR/ \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=200 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=5.0 \
  --output_dir=/data01/dyc/bert_classifier/output/train >>nohup.out 2>&1 &
echo "task is done..."

import json
import random
import os
import tokenization
import tensorflow as tf
import run_classifier
from flask import Flask, request
from run_classifier import AutoHomeProcesser
from run_classifier import file_based_convert_examples_to_features
from run_classifier import file_based_input_fn_builder


app = Flask(__name__)


flags = tf.flags

FLAGS = flags.FLAGS

# 加载模型
def load_model():
    with tf.Session() as sess:
        # import_meta_graph填的名字meta文件的名字
        saver = tf.train.import_meta_graph('model/ckpt-1276.meta')
        # 检查checkpoint，所以只填到checkpoint所在的路径下即可，不需要填checkpoint
        saver.restore(sess, tf.train.latest_checkpoint("model"))


def do_predict():
    processors = {
        "auto": AutoHomeProcesser
    }
    processor = processors[AutoHomeProcesser.task_name]()
    label_list = processor.get_labels()
    tokenizer = tokenization.FullTokenizer(
        vocab_file=FLAGS.vocab_file, do_lower_case=FLAGS.do_lower_case)

    predict_examples = processor.get_test_examples(FLAGS.data_dir)
    num_actual_predict_examples = len(predict_examples)

    predict_file = os.path.join(FLAGS.output_dir, "predict.tf_record")
    # 1.调用convert_single_example转化Input_example为Feature_example
    # 2.转换为TFRecord格式，便于大型数据处理
    file_based_convert_examples_to_features(predict_examples, label_list,
                                            FLAGS.max_seq_length, tokenizer,
                                            predict_file)

    predict_drop_remainder = True if FLAGS.use_tpu else False
    # 1.TFRecord to example 2.int64 to int32 为estimator提供输入
    predict_input_fn = file_based_input_fn_builder(
        input_file=predict_file,
        seq_length=FLAGS.max_seq_length,
        is_training=False,
        drop_remainder=predict_drop_remainder)

    result = estimator.predict(input_fn=predict_input_fn)













# 1.加载模型
#2.获取预测数据




@app.route('/predict', methods=[ 'POST'])
def return_result():
    # show the user profile for that user
    tmp = request.get_data(as_text=True)  # 得到post的json 转成str
    data = json.loads(tmp)  # 获取 JSON 数据
    print(data)
    result = {
        "id" : data["id"],
        "name": data["name"],
    }
    return jsonify(result)

if __name__ ==  '__main__':

    app.run(host='0.0.0.0',port=8205)
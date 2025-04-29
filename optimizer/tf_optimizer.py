import tensorflow as tf
import os

def optimize_tf_graph(model_path, output_folder):
    model = tf.saved_model.load(model_path)
    concrete_func = model.signatures[tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]

    optimized_filename = os.path.basename(model_path).replace('.pb', '_optimized.pb')
    optimized_path = os.path.join(output_folder, optimized_filename)

    tf.saved_model.save(model, optimized_path)
    return optimized_path

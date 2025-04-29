import time
import torch
import tensorflow as tf

def benchmark_model(original_path, optimized_path, framework='pytorch'):
    input_sample = torch.randn(1, 3, 224, 224)

    if framework == 'pytorch':
        original_model = torch.load(original_path)
        optimized_model = torch.jit.load(optimized_path)
        
        # Benchmark original
        start = time.time()
        for _ in range(10):
            original_model(input_sample)
        original_time = (time.time() - start) / 10
        
        # Benchmark optimized
        start = time.time()
        for _ in range(10):
            optimized_model(input_sample)
        optimized_time = (time.time() - start) / 10

    else:
        # For TensorFlow
        original_model = tf.saved_model.load(original_path)
        optimized_model = tf.saved_model.load(optimized_path)

        input_sample = tf.random.normal([1, 224, 224, 3])

        original_func = original_model.signatures['serving_default']
        optimized_func = optimized_model.signatures['serving_default']

        start = time.time()
        for _ in range(10):
            original_func(input_sample)
        original_time = (time.time() - start) / 10

        start = time.time()
        for _ in range(10):
            optimized_func(input_sample)
        optimized_time = (time.time() - start) / 10

    speedup = original_time / optimized_time
    return round(speedup, 2)

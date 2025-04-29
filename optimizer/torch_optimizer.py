import torch
import os

def optimize_torch_graph(model_path, output_folder):
    model = torch.load(model_path)
    optimized_model = torch.jit.script(model)
    optimized_model = torch.jit.optimize_for_inference(optimized_model)

    optimized_filename = os.path.basename(model_path).replace('.pt', '_optimized.pt')
    optimized_path = os.path.join(output_folder, optimized_filename)
    torch.jit.save(optimized_model, optimized_path)

    return optimized_path

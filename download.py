# This file runs during container build time to get model weights built into the container

# In this example: A Huggingface Stable Diffusion custom model
from diffusers import DDPMScheduler, DiffusionPipeline
import torch

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    # this should match the model load used in app.py's init function

    repo_id="Meina/MeinaUnreal_V3"
    ddpm = DDPMScheduler.from_pretrained(repo_id, subfolder="scheduler")

    DiffusionPipeline.from_pretrained(
        repo_id, 
        use_safetensors=True,
        torch_dtype=torch.float16,
        scheduler=ddpm
    )

if __name__ == "__main__":
    download_model()

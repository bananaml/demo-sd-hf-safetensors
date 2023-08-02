from io import BytesIO
from potassium import Potassium, Request, Response
from diffusers import DiffusionPipeline, DDPMScheduler
import torch
import base64

# create a new Potassium app
app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    repo_id="Meina/MeinaUnreal_V3"

    ddpm = DDPMScheduler.from_pretrained(repo_id, subfolder="scheduler")
    
    model = DiffusionPipeline.from_pretrained(
        repo_id, 
        use_safetensors=True,
        torch_dtype=torch.float16,
        scheduler=ddpm
    ).to("cuda")

    context = {
        "model": model,
    }

    return context

# @app.handler runs for every call
@app.handler()
def handler(context: dict, request: Request) -> Response:
    model = context.get("model")

    prompt = request.json.get("prompt")
    negative_prompt = "(worst quality, low quality:1.4), monochrome, zombie, (interlocked fingers), cleavage, nudity, naked, nude"

    image = model(
        prompt=prompt,
        negative_prompt=negative_prompt,
        guidance_scale=7,
        num_inference_steps=request.json.get("steps", 30),
        generator=torch.Generator(device="cuda").manual_seed(request.json.get("seed")) if request.json.get("seed") else None,
        width=512,
        height=512,
    ).images[0]

    buffered = BytesIO()
    image.save(buffered, format="JPEG", quality=80)
    img_str = base64.b64encode(buffered.getvalue())

    # You could also consider writing this image to S3
    # and returning the S3 URL instead of the image data
    # for a slightly faster response time

    return Response(
        json = {"output": str(img_str, "utf-8")}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()

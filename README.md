![](https://www.banana.dev/lib_zOkYpJoyYVcAamDf/x2p804nk9qvjb1vg.svg?w=340 "Banana.dev")

# Banana.dev Stable Diffusion Safetensors starter template

This is a Stable Diffusion starter template from [Banana.dev](https://www.banana.dev) that allows on-demand serverless GPU inference.

It uses a custom safetensors model from Hugging Face.

It supports prompting with and without seeds.

You can fork this repository and deploy it on Banana as is, or customize it based on your own needs.

# Running this app

## Deploying on Banana.dev

1. [Fork this](https://github.com/bananaml/demo-sd-hf-safetensors/fork) repository to your own Github account.
2. Connect your Github account on Banana.
3. [Create a new model](https://app.banana.dev/deploy) on Banana from the forked Github repository.

## Running after deploying

1. Wait for the model to build after creating it.
2. Make an API request to it using one of the provided snippets in your Banana dashboard.

For more info, check out the [Banana.dev docs](https://docs.banana.dev/banana-docs/).

## Testing locally

### Using Docker

Build the model as a Docker image. You can change the `banana-sd-hf-safetensors` part to anything.

```sh
docker build -t banana-sd-hf-safetensors .
```

Run the Potassium server

```sh
docker run --publish 8000:8000 -it banana-sd-hf-safetensors
```

In another terminal, run inference after the above is built and running.

```sh
curl -X POST -H 'Content-Type: application/json' -d '{"prompt": "colorful, 1girl, high angle, software developer protagonist, hacker, ((computer screen)), matrix, ((keyboard)), glow, light particles, wallpaper, chromatic aberration"}' http://localhost:8000
```

### Without Docker

You could also install and run it without Docker.

Just make sure that the pip dependencies in the Docker file (and torch) are installed in your Python virtual environment.

Run the Potassium app in one terminal window.

```sh
python3 app.py
```

Call the model in another terminal window with the Potassium app still running from the previous step.

```sh
curl -X POST -H 'Content-Type: application/json' -d '{"prompt": "colorful, 1girl, high angle, software developer protagonist, hacker, ((computer screen)), matrix, ((keyboard)), glow, light particles, wallpaper, chromatic aberration"}' http://localhost:8000
```

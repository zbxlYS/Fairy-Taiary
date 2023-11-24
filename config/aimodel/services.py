import openai
from stability_sdk import client
from stability_sdk.interfaces.gooseai.generation.generation_pb2 import SAMPLER_K_DPMPP_2M

openai.api_key = 'YOUR_OPENAI_API_KEY'  # GPT API 키 설정

stability_api = client.StabilityInference(
    key='YOUR_STABILITY_API_KEY',  # Stability AI API 키 설정
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0"
)

def get_gpt_completion(prompt):
    query = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return query.choices[0].message["content"]

def generate_stability_image(prompt):
    answers = stability_api.generate(
        prompt=prompt,
        style_preset="anime",
        seed=4253978046,
        steps=50,
        cfg_scale=8.0,
        width=1024,
        height=1024,
        samples=3,
        sampler=SAMPLER_K_DPMPP_2M
    )

    images = []
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = artifact.binary
                images.append(img)

    return images
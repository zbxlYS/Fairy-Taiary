from django.shortcuts import render 
from django.http import JsonResponse 
import openai

openai.api_key='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'


def get_completion(prompt): 
	print(prompt) 
	query = openai.ChatCompletion.create( 
		model="gpt-3.5-turbo",
		messages=[
        	{'role':'user','content': prompt}
    	], 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 
	response = query.choices[0].message["content"]
	print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		prompt=str(prompt)
		response = get_completion(prompt)
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 


from stability_sdk import client
from stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


def generate_image(request):
    stability_api = client.StabilityInference(
        key='YOUR_API_KEY',
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0"
    )

    answers = stability_api.generate(
        prompt="expansive landscape rolling greens with gargantuan yggdrasil, intricate world-spanning roots towering under a blue alien sky, masterful, ghibli",
        style_preset="anime",
        seed=4253978046,
        steps=50,
        cfg_scale=8.0,
        width=1024,
        height=1024,
        samples=3,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )

    images = []
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = artifact.binary
                images.append(img)

    return render(request, 'image_generation/generate_image.html', {'images': images})
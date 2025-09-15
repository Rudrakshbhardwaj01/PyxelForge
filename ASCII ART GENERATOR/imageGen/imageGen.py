from mistralai import Mistral
from mistralai.models import ToolFileChunk

API_KEY = "YOUR-MISTRAL-API-KEY"

client = Mistral(api_key=API_KEY)

def simple_generate_image(prompt, output_path="out.png"):
    
    agent = client.beta.agents.create(
        model="mistral-medium-2505",
        name="temp-image-agent",
        tools=[{"type": "image_generation"}]
    )

    resp = client.beta.conversations.start(
        agent_id=agent.id,
        inputs=prompt
    )

    for chunk in resp.outputs[-1].content:
        if isinstance(chunk, ToolFileChunk):
            data = client.files.download(file_id=chunk.file_id).read()
            with open(output_path, "wb") as f:
                f.write(data)
            return output_path

    raise RuntimeError("No image returned")




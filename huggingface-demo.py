import hashlib
import os
from huggingface_hub import HfApi, ModelCard
from umarise import UmariseCore

model_path = "model.pkl"
with open(model_path, "wb") as f:
    f.write(b"dummy model weights v1.0")

client = UmariseCore(api_key=os.environ["UMARISE_API_KEY"])
with open(model_path, "rb") as f:
    sha256 = "sha256:" + hashlib.sha256(f.read()).hexdigest()

result = client.attest(sha256)
origin_id = result.origin_id

repo_id = "your-org/your-model"
api = HfApi()
api.upload_file(path_or_fileobj=model_path, path_in_repo="model.pkl", repo_id=repo_id)

print(f"Anchored: {origin_id}")
print(f"Verify: https://verify-anchoring.org")

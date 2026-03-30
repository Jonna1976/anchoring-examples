import hashlib
import os
import wandb
from umarise import UmariseCore

model_path = "model.pkl"
with open(model_path, "wb") as f:
    f.write(b"dummy model weights v1.0")

client = UmariseCore(api_key=os.environ["UMARISE_API_KEY"])
with open(model_path, "rb") as f:
    sha256 = "sha256:" + hashlib.sha256(f.read()).hexdigest()

result = client.attest(hash_value=sha256)
origin_id = result.origin_id

run = wandb.init(project="my-project")
artifact = wandb.Artifact("model", type="model")
artifact.add_file(model_path)
artifact.metadata["umarise_origin_id"] = origin_id
run.log_artifact(artifact)
run.finish()

print(f"Anchored: {origin_id}")
print(f"Verify: https://verify-anchoring.org")

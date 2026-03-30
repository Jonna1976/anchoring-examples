import hashlib
import os
import mlflow
from umarise import UmariseCore

model_path = "model.pkl"
with open(model_path, "wb") as f:
    f.write(b"dummy model weights v1.0")

client = UmariseCore(api_key=os.environ["UMARISE_API_KEY"])
with open(model_path, "rb") as f:
    sha256 = "sha256:" + hashlib.sha256(f.read()).hexdigest()

result = client.attest(sha256)
origin_id = result.origin_id

with mlflow.start_run():
    mlflow.log_artifact(model_path)
    mlflow.log_param("umarise_origin_id", origin_id)
    mlflow.set_tag("umarise.anchored", "true")

print(f"Anchored: {origin_id}")
print(f"Verify: https://verify-anchoring.org")

import hashlib
import os
import boto3
from umarise import UmariseCore

artifact_path = "dataset-snapshot.csv"
with open(artifact_path, "wb") as f:
    f.write(b"id,value\n1,alpha\n2,bravo\n3,charlie\n")

client = UmariseCore(api_key=os.environ["UMARISE_API_KEY"])
with open(artifact_path, "rb") as f:
    sha256 = "sha256:" + hashlib.sha256(f.read()).hexdigest()

result = client.attest(hash_value=sha256)
origin_id = result.origin_id

s3 = boto3.client("s3")
s3.upload_file(artifact_path, "my-bucket", f"artifacts/{artifact_path}",
    ExtraArgs={"Metadata": {"umarise-origin-id": origin_id}})

print(f"Anchored: {origin_id}")
print(f"Verify: https://verify-anchoring.org")

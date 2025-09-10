# examples/demo.py — minimal runnable demo
import yaml
from middleware.python.hap_middleware import HAP

cfg = yaml.safe_load(open("examples/meta-config.sample.yaml", "r", encoding="utf-8"))

def call_model(prompt, ctx):
    # replace with your real model call
    return "Based on ZSY×Hope, we adopted the impact-tiering framework."

hap = HAP(cfg, ledger_path="ack-ledger.jsonl")
print(hap.wrap(call_model)("test", {}))

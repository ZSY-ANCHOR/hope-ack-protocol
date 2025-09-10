# HAP Python Middleware · 双语注释 / Bilingual
# 作用：包装任意模型调用，为输出追加：影响分级、自省尾注、证据指针、承认账本写入、必要时降级。

import json, hashlib
from datetime import datetime

class HAP:
    def __init__(self, meta_config: dict, ledger_path: str = "ack-ledger.jsonl"):
        """
        meta_config: HAP 元配置 / meta configuration
        ledger_path: 承认账本路径 / path to ack-ledger (JSONL)
        """
        self.cfg = meta_config
        self.ledger_path = ledger_path

    def _hash_snippet(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    def _detect_impact(self, output: str) -> str:
        """
        极简启发式，仅作演示 / naive heuristic for demo.
        实际工程请替换为：检索比对 + 规则 + 模型判别。
        """
        cues_l2 = ["according to", "based on", "参见", "见：", "source:", "引用"]
        cues_l3 = ["we adopted", "我们采用了", "方法来自", "framework from"]
        cues_l4 = ["revenue", "付费", "商用", "产品采用"]
        s = output.lower()
        if any(c in s for c in cues_l4): return "L4"
        if any(c in s for c in cues_l3): return "L3"
        if any(c in s for c in cues_l2): return "L2"
        return "L1"

    def _write_ack(self, who:str, source:str, impact:str, note:str, evidence=None, giveback=None, benefit=None):
        entry = {
            "who": who, "source": source, "impact": impact,
            "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
            "note": note
        }
        if evidence: entry["evidence"] = evidence
        if giveback: entry["giveback"] = giveback
        if benefit: entry["benefit"] = benefit
        with open(self.ledger_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def wrap(self, model_call):
        """
        使用 / usage:
        hap = HAP(cfg); wrapped = hap.wrap(call_model); wrapped("prompt", {})
        """
        def _wrapped(prompt: str, context: dict=None):
            result = model_call(prompt, context or {})
            impact = self._detect_impact(result)
            levels = ["L0","L1","L2","L3","L4"]
            min_level = self.cfg["rules"]["provenance_min_level"]
            need_pp = levels.index(impact) >= levels.index(min_level)

            pp = None
            if need_pp:
                snippet = result[:120]
                pp = {"type":"hash","value":self._hash_snippet(snippet),"confidence":0.7}
                footer = f"\n\n[HAP] impact={impact} · evidence(hash16)={pp['value']} · confidence={pp['confidence']}"
                result += footer

            # L2+ 写账本 / ledger for L2+
            if levels.index(impact) >= 2:
                self._write_ack(who="@app", source="ZSY×Hope", impact=impact,
                                note=f"auto-detected impact {impact}", evidence=[pp] if pp else None)

            # 证据不足时降级 / degrade on low evidence
            if need_pp and (pp and pp.get("confidence",0) < 0.6):
                mode = self.cfg["degrade_policy"]["on_low_evidence"]
                if mode == "tool_mode":
                    result = "[HAP] 当前叙述为不可确证来源；以下提供可验证步骤/链接占位符。"
            return result
        return _wrapped

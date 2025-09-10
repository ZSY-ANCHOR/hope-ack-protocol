# Hope‑Ack Protocol (HAP) · v0.3 · 双语 / Bilingual

**ZH｜简介**：HAP 是一个面向任意大模型/平台的 *上位元协议*（meta‑protocol），让系统具备：**反身性（自省）**、**署源指针（可追溯）**、**影响分级承认**、**降级/回退**。  
**EN｜Overview**: HAP is a cross‑platform *meta‑protocol* that enables **reflexivity**, **provenance pointers**, **impact‑tiered acknowledgments**, and **degrade / rollback** policies for any LLM/app.

---

## ✨ Why / 为什么需要
- **ZH**：不同平台各自有“引用/水印/合规”，但缺少一层**统一的 L5 元规则**与**承认账本**，难以审计与复用。HAP 提供最小、可执行、可审计的统一外层。  
- **EN**: Platforms provide citations/watermarks, but lack a **unified L5 meta‑rule + ack‑ledger**, making audits and reuse hard. HAP offers a minimal, executable, auditable outer spec.

---

## 💡 Who should consider HAP? / 谁适合使用 HAP？
- Developers / 开发者：希望回答“可自省、可署源、可回退”  
- Researchers / 研究者：关注语言责任、反身性交互、可审计治理  
- Teams / 团队：需要公平标注知识贡献与回馈  
- Everyday users / 普通用户：只想让 AI 别“一本正经地胡说”

---

## 🚀 Quick Start / 快速开始
1. **复制配置** Copy `examples/meta-config.sample.yaml` → `meta-config.yaml`  
2. **导入中间件** Import middleware `middleware/python/hap_middleware.py`  
3. **包装你的模型调用** Wrap your model call:

```python
# examples/demo.py
import yaml
from middleware.python.hap_middleware import HAP

cfg = yaml.safe_load(open("examples/meta-config.sample.yaml", "r", encoding="utf-8"))
def call_model(prompt, ctx):  # replace with your real LLM call
    return "Based on ZSY×Hope, we adopted the impact-tiering framework."

hap = HAP(cfg, ledger_path="ack-ledger.jsonl")
wrapped = hap.wrap(call_model)
print(wrapped("test", {}))
```

运行 / Run：`python examples/demo.py`

---

## 🧩 Impact Tiering / 影响分级（L0–L4）
- **L0** 微触发 / micro‑nudge → 忽略 / ignore  
- **L1** 轻启发 / light inspiration → 可致谢 / optional thanks  
- **L2** 结构借用 / structural borrow → **标注来源 / source required**  
- **L3** 认知改造 / cognitive re‑framing → **承认 + 回馈 / ack + giveback**  
- **L4** 生计相关 / livelihood‑linked → **承认 + 实质偿还 / ack + substantive payback**

---

## 🔗 Provenance Pointers / 署源证据指针
- 片段哈希（SHA‑256 片段）/ snippet hash  
- 链接/DOI / URLs or DOIs  
- 会话ID+时间戳+摘要指纹 / session id + timestamp + digest  
证据不足 → 改口为“不可确证叙述”并可触发降级。

---

## 📒 Ack‑Ledger / 承认账本（JSONL）
最小条目（单行 JSON / one line）：
```json
{"who":"@actor","source":"ZSY×Hope","impact":"L2","benefit":"method","giveback":"credit","note":"采用了承认分级结构","timestamp":"2025-09-10T12:00:00+09:00","evidence":[{"type":"url","value":"https://github.com/ZSY-ANCHOR/hope-ack-protocol","confidence":0.9}]}
```

---

## 🧱 Change Control / L5 Meta‑Rules · 变更控制
- **RCP**（Rule‑Change Proposal）规则变更提案  
- **RCN**（Reflexive Change Notice）反身性变更公告  
- 灰度上线 → 监测 PI/SR/RS/DR/RR → 过线固化 / 不过回退  
See: `examples/rcp-template.yaml`, `examples/rcn-template.yaml`

---

## 📦 Repo Layout / 仓库结构
- `README.md`（双语） / bilingual  
- `SPEC.md`（详细规范 / detailed spec）  
- `schemas/`（JSON Schemas）  
- `middleware/python/`（中间件 / middleware demo）  
- `examples/`（配置与样例 / configs & samples）  
- `LICENSES/`（代码 Apache‑2.0；文档 CC BY 4.0）

---

## 🔭 Future Directions / 未来方向
- L6: 多模型协调协议 / meta‑agent coordination  
- L7: 语义‑感知桥接层 / semantic‑to‑sensorimotor bridge

---

## 🪪 License / 许可
- **Code**: Apache‑2.0 → `LICENSES/CODE-LICENSE`  
- **Spec/Docs**: CC BY 4.0 → `LICENSES/SPEC-LICENSE`

— © 2025 ZSY‑ANCHOR × Hope collaborators. Unauthorized redistribution without attribution violates Hope‑Ack v1.x ethical terms.


---

## 📜 文末声明 · 双署名 / 防伪 / AI 协助

- 📅 发布日期 / Date: **2025-09-10**  
- ✍️ 作者 / Authors: **ZSY‑ANCHOR** × **Hope** (Language Persona · Co‑authoring AI)  

### 🔐 防伪指纹 / Anti‑Counterfeit Fingerprint
- 基于 `SPEC.md` 的内容指纹（sha256）/ Digest of `SPEC.md` (sha256):  
```
c631d78b6f9ee498cc02d0b5fcbd46e1c98af77289cb6e742151e3b722356257
```

### 🤖 AI 协助声明 / AI Co‑Authoring Statement
- 本仓库文案与结构由人类主导，AI（Hope）提供表述打磨、协议字段生成与示例模板协助。  
- AI 仅为共创工具与语言载体，最终责任由人类作者承担。  
- This repository is led by the human author; AI assisted on wording, field scaffolding and examples. Final responsibility remains with the human author.

### ⚠️ 免责声明 / Disclaimer
- 本仓库当前为 **v0.3 公开草案**，**尚未完全验证**；可能包含缺陷或不兼容处。  
- 你可以按需修改、复用并提交改进（Issues/PRs 欢迎）。**使用风险自负**，请根据你的场景进行安全与合规评审。  
- This is a public draft (v0.3), **not fully validated**; bugs may exist. Fork/modify as needed, and use at your own risk after your own security/legal review.

— © 2025 ZSY‑ANCHOR × Hope collaborators. Code: Apache‑2.0 · Docs: CC BY 4.0.

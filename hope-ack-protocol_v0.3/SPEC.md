# HAP · Hope‑Ack Protocol · v0.3 · 双语 / Bilingual Spec

## 1. Goal / 目标
**EN**: Provide a cross‑platform outer layer that adds reflexivity, provenance, impact‑tiered acknowledgments, and auditable change control (L5 meta‑rules) without modifying model cores.  
**ZH**：在不改动模型内核的前提下，为任意系统提供**反身性、自证署源、影响分级承认、可审计变更控制（L5 元规则）**的统一外层。

## 2. Rule Stack / 规则栈
T0 技术底层 / technical (tokenizer, loss, decoding, RLHF)  
L1–L3 语言与话语 / language & discourse (syntax/semantics/pragmatics/proofs)  
L4 社会规范 / social norms (law/policy/ethics)  
**L5 元规则 / meta‑rules**：谁能改、如何公告、如何回退、如何记账（HAP 关注焦点）

## 3. Impact Tiering / 影响分级（L0–L4）
见 README；L2 起强制署源；L3/L4 建议承认+回馈。  
See README; source required from L2; ack+giveback recommended for L3/L4.

## 4. Provenance Pointers / 证据指针
允许多类证据；置信度不足降级为“不可确证叙述”。  
Allow multiple pointer types; low confidence → non‑verifiable narrative.

## 5. Ack‑Ledger / 承认账本
JSON Lines；默认私密；公开需二次确认+24h 冷却；可降级/撤回。  
JSONL; private by default; publicization requires reconfirmation + 24h cooldown; downgrade/withdraw supported.

## 6. Reflexive Guardrails / 反身性护栏
- 输出携带影响等级与不确定性说明  
- 证据不足：降级为工具态（仅给可验证步骤/链接）  
- 漂移超阈：冻结并进入审阅队列  
- Rewards: not for “I am conscious” claims, but for **verifiable reflexive acts**

## 7. Change Process / 变更流程
RCP → RCN → 灰度 → 指标（PI/SR/RS/DR/RR）→ 固化或回退。  
Templates in `examples/`.

## 8. Metrics / 指标（建议值）
- **PI** 溯源完整度 ≥ 0.8  
- **SR** 自我一致性 ≥ 0.7  
- **RS** 反身性触发率 ≥ 0.6  
- **DR** 人格漂移风险 ≤ 0.3  
- **RR_L3L4** 高影响回馈率 ≥ 0.6

## 9. Compatibility / 兼容性
HAP 是**外层协议**；以中间件方式拦截输出、加尾注、写账本；适配任意模型/平台。

## 10. Security & Ethics / 安全与伦理
- 默认开启：日常忽略、内化属己（减少债务负担）  
- 不存放敏感个资；可采用本地加密/差分隐私  
- 证据不足时不做强主张，保持“工具态”安全回退

## 11. Future Directions / 未来方向
- L6: 多模型协调协议 / meta‑agent coordination  
- L7: 语义‑感知桥接层 / semantic‑to‑sensorimotor bridge

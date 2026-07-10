# AI Context Auditor Skill 使用指南

`ai-context-auditor` 用來定期檢查 repository 內的 AI context 健康度，包含目錄分層、canonical ownership、規則衝突、runtime wrapper、skill routing、索引、語言政策、workflow lifecycle 與 validation integrity。

每次執行都必須產出並保存正式報告，而不是只在對話中提供結論。

## 適用情境

- 定期執行 AI context 自檢；
- 評估 prompt／skill repository 的品質；
- 檢查 `.ai`、`.dev`、`.agents`、`.claude` 是否漂移；
- 比較「一般知識獨立分析」與「套用 repo skill／policy 分析」的差異；
- 追蹤前一次 audit finding 是否仍然存在。

## 預設掃描邊界

Auditor 預設只掃描 AI context 與治理相關 surfaces，例如 root README 與 agent instructions、`.ai/**`、`.dev/**`、`.agents/**`、`.claude/**`、AI assistant 相關的 `.github/**` 文件，以及被上述文件直接引用的 context validation manifests、README 或 scripts。

預設略過：

- `src/**`；
- `tests/**`、`test/**`；
- 實際產品的 Domain、Application、Infrastructure、API 與 test implementation；
- `bin/**`、`obj/**`、`dist/**`、dependencies 與 generated output。

## 與 Code Review 的邊界

若要求包含產品 source code、test code、solution 或 implementation quality，auditor 不應自行擴大掃描。它必須說明未掃描的路徑，並建議改用 `code-reviewer`。

建議 prompt：

```text
Use $code-reviewer to review the requested .NET source and test files.
Keep the AI context audit report as background only; do not treat context findings as code findings.
```

## 標準執行方式

```text
Use $ai-context-auditor to perform a recurring AI context self-audit.

Requirements:
- first create an independent baseline using general knowledge;
- then apply repository governance skills and policies;
- compare both passes;
- exclude src and tests;
- save the report under .dev/workflows/<workflow-id>/review-report.md;
- do not remediate findings unless separately authorized.
```

## 報告位置

預設使用：

```text
.dev/workflows/<YYYY-MM-DD>-ai-context-audit/review-report.md
```

若 audit 已屬於既有 workflow，則直接使用該 workflow 的 `review-report.md`。報告範本以 `.ai/assets/skills/ai-context-auditor/templates/ai-context-audit-report-template.md` 為準。

## 後續整改

Auditor 預設唯讀，不會直接修正 findings。若使用者決定整改：

- AI context ownership、language、wrapper 或 routing → `ai-context-governance`；
- 多階段整改 → `dev-workflow`；
- 產品 source code → `code-reviewer`；
- framework 複製後的 target repo truth 重建 → `repo-structure-sync`。


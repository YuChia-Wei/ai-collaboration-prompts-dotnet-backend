# Decision Archive Portability Notes

`.dev/adr/` 不再是 portable baseline 的必要組件。

## Default Rule

- 若要把本 repo 移植到新專案，預設可直接刪除整個 `.dev/adr/`

## Exception

- 只有在你明確需要保留少量歷史決策脈絡時，才保留這個目錄
- 即使保留，也不應把它當成新專案的主規則入口

## Canonical Rule Locations

- 結構與限制：`.dev/standards/`
- 使用教學：`.dev/guides/`
- agent-facing assets：`.ai/`
- repo collaboration baseline：`AGENTS.md`

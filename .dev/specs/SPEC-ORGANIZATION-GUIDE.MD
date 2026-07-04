# Spec 檔案組織指南

本文件說明如何依 bounded context、aggregate 與測試目標組織 specs，不預設任何產品 domain。

## 目錄結構

```text
.dev/specs/
  domains/
    <bounded-context>/
      <aggregate>/
        entity/
          <aggregate>-spec.md
        usecase/
          <action>-<aggregate>.json
  tests/
    <bounded-context>/
      aggregate/
      use-cases/
      integration/
    cross-domain/
    e2e/
```

## 放置規則

1. 先識別 use case 主要操作的 aggregate。
2. 再確認 aggregate 所屬 bounded context。
3. production spec 與 test spec 使用相同 bounded-context / aggregate 視角。
4. 關聯關係不代表 ownership；不要因為 A 引用 B，就把 B 的 spec 放進 A 的 aggregate 目錄。
5. 若 bounded context 或 aggregate ownership 不清楚，先使用 `ddd-ca-hex-architect`，不要猜測路徑。

## 命名規則

- Use case spec：`<action>-<aggregate>.json`
- Entity / aggregate spec：`<aggregate>-spec.md`
- Test spec：`<target>.test-spec.md`
- 目錄與檔名使用 kebab-case。

## 中性範例

```text
.dev/specs/
  domains/
    <context-a>/
      <aggregate-a>/
        entity/
          <aggregate-a>-spec.md
        usecase/
          create-<aggregate-a>.json
          update-<aggregate-a>.json
    <context-b>/
      <aggregate-b>/
        usecase/
          process-<aggregate-b>.json
  tests/
    <context-a>/
      aggregate/
        <aggregate-a>.test-spec.md
      use-cases/
        create-<aggregate-a>.test-spec.md
      integration/
        <aggregate-a>-persistence.test-spec.md
```

## 常見錯誤

### 依關聯而不是 ownership 放置

```text
Wrong:
domains/<context-a>/<aggregate-a>/usecase/create-<aggregate-b>.json

Correct:
domains/<context-b>/<aggregate-b>/usecase/create-<aggregate-b>.json
```

### 將所有 use cases 集中在同一層

```text
Wrong:
specs/usecases/<use-case>.json

Correct:
specs/domains/<bounded-context>/<aggregate>/usecase/<use-case>.json
```

## 遷移步驟

1. 確認 bounded context 與 aggregate ownership。
2. 建立正確目錄。
3. 移動 spec 與對應 test specs。
4. 更新 requirement、problem frame、workflow task 與 code reference。
5. 搜尋舊路徑並驗證 JSON / Markdown。

## Review Checklist

- [ ] Spec 路徑反映 bounded context 與 aggregate ownership。
- [ ] Production spec 與 test spec 使用一致命名。
- [ ] Cross-domain 與 E2E specs 沒有被錯放到單一 aggregate。
- [ ] 文件使用目標 repo 的 ubiquitous language。
- [ ] Template placeholders 沒有被誤當成 product truth。

# Context Load Trace Contract

This source-only directory may retain approved representative trace manifests
and their normalized measurement results. It must not contain unpinned
interactive-session recollections or synthetic test output.

The measurement input uses schema `1.0`:

```yaml
schema_version: "1.0"
measurement_id: "<stable-id>"
subject_commit: "<full-current-head>"
prompt_accounting:
  total_prompt_tokens: null
  total_prompt_tokens_source: null
  repository_corpus_is_prompt: false
  repository_token_heuristic:
    method: ceil-utf8-bytes-divided-by-four
    scope: repository_loaded
    is_total_prompt_tokens: false
traces:
  - family: runtime
    events:
      - event_kind: runtime
        path: AGENTS.md
        git_blob: "<full-blob-id>"
        bytes: 0
        whitespace_words: 0
```

Exactly one trace is required for each of `runtime`, `skill-routing`,
`release`, `handoff`, and `development`. Each trace contains one or more
`runtime` or `full-file` events. Paths must be unique within a trace; the same
file may legitimately be loaded by different representative session families.
Every event metric is verified from the subject Git tree.

Run:

```text
python .ai/scripts/measure-ai-context-load.py \
  --traces .ai/evaluation/context-load/<trace>.yaml \
  --output .ai/evaluation/context-load/<result>.yaml
```

The repository must be clean and `subject_commit` must equal the full current
`HEAD`. A retained result is evidence only for its declared repository-backed
load events. It does not measure system instructions, tool schemas,
conversation history, model-internal accounting, or any other non-repository
prompt content.

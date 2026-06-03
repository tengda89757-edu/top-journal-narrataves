# top-journal-narrative-writing

A cross-compatible Agent Skill for Codex and Claude Code that helps diagnose and rewrite academic paper narratives for high-impact journal framing.

## Install for Codex
Copy the folder to a Codex skill directory, for example:

```bash
mkdir -p ~/.agents/skills
cp -R top-journal-narrative-writing ~/.agents/skills/
```

Repository-scoped option:

```bash
mkdir -p .agents/skills
cp -R top-journal-narrative-writing .agents/skills/
```

## Install for Claude Code
Copy the folder to a Claude Code skill directory, for example:

```bash
mkdir -p ~/.claude/skills
cp -R top-journal-narrative-writing ~/.claude/skills/
```

Project-scoped option:

```bash
mkdir -p .claude/skills
cp -R top-journal-narrative-writing .claude/skills/
```

## Example prompts

```text
使用 top-journal-narrative-writing 诊断这篇论文摘要的顶刊叙事，给出 3 个可防守的 framing。
```

```text
请把下面的“方法驱动”摘要改成“问题驱动 + 机制解释”的版本，并标出哪些 claim 需要额外证据。
```

```text
根据我的实验结果，判断是否能从“应用”升级成“原理”，不要过度包装。
```

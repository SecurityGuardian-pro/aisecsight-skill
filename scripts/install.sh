#!/usr/bin/env bash
# AISecSight Skill 安装脚本（macOS / Linux）
# 用法：
#   ./scripts/install.sh                 # 自动探测已安装 Agent 的 skills 目录
#   ./scripts/install.sh ~/.claude/skills   # 指定 skills 目录
set -euo pipefail

SKILL_URL="https://aisecsight.com/api/v1/skill"
NAME="aisecsight"

say() { printf '%s\n' "$*"; }
die() { printf '错误：%s\n' "$*" >&2; exit 1; }

# 1. 决定安装目录
if [ $# -ge 1 ]; then
  SKILLS_DIR="$1"
elif [ -n "${SKILLS_DIR:-}" ]; then
  SKILLS_DIR="${SKILLS_DIR}"
else
  SKILLS_DIR=""
  for d in "$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.cursor/skills" \
           "$HOME/.gemini/skills" "$HOME/.workbuddy/skills"; do
    if [ -d "$d" ]; then SKILLS_DIR="$d"; break; fi
  done
  # 都没找到就默认装到 Claude Code 目录
  [ -n "$SKILLS_DIR" ] || SKILLS_DIR="$HOME/.claude/skills"
fi

TARGET="$SKILLS_DIR/$NAME"
say "安装目录：$TARGET"

command -v curl >/dev/null 2>&1 || die "需要 curl，请先安装 curl。"

# 2. 下载
mkdir -p "$TARGET"
if ! curl -fsSL "$SKILL_URL" -o "$TARGET/SKILL.md.tmp"; then
  die "下载失败，请检查网络或稍后重试（$SKILL_URL）。"
fi
mv "$TARGET/SKILL.md.tmp" "$TARGET/SKILL.md"

# 3. 基本校验
head -1 "$TARGET/SKILL.md" | grep -q '^---$' || die "下载内容不像 SKILL.md（缺少 YAML 头），已保留文件供排查：$TARGET/SKILL.md"
grep -q '^name: aisecsight' "$TARGET/SKILL.md" || die "SKILL.md 的 name 字段异常，请检查 $TARGET/SKILL.md"

say "已安装：$TARGET/SKILL.md（$(wc -c < "$TARGET/SKILL.md" | tr -d ' ') 字节）"

# 4. 接口自检
if command -v python3 >/dev/null 2>&1 && [ -f "$(dirname "$0")/verify.py" ]; then
  say ""
  say "正在做接口连通性自检……"
  python3 "$(dirname "$0")/verify.py" || say "自检未全部通过（不影响安装，可能是网络或限流）。"
fi

say ""
say "装好了。请新开一个会话再提问，例如："
say "  「欧盟 AI 法对通用模型提供者的罚款上限是多少？」"

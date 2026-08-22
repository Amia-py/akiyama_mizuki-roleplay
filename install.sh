#!/usr/bin/env bash
# mizuki-roleplay 安装脚本（Linux / macOS / Windows-GitBash / WSL）
# 用法: bash install.sh [agent...]
#   agent 可选: claude-code codex openclaw workbuddy reasonix opencode hermes
#   不带参数 = 全部安装（跳过未识别的）
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/mizuki-roleplay"
if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
  echo "[ERROR] 未找到 $SKILL_DIR/SKILL.md，请从仓库根目录运行" >&2
  exit 1
fi

install_into() { # $1=目标目录
  local target="$1"
  mkdir -p "$target"
  rm -rf "$target/mizuki-roleplay"
  cp -r "$SKILL_DIR" "$target/mizuki-roleplay"
  echo "[OK] -> $target/mizuki-roleplay"
}

install_into "$HOME/.claude/skills"            # Claude Code
install_into "$HOME/.codex/skills"             # Codex CLI（部分版本读 ~/.agents/skills，可复制一份）
install_into "$HOME/.agents/skills"            # Codex / Reasonix 通用目录
install_into "$HOME/.openclaw/skills"          # OpenClaw
install_into "$HOME/.workbuddy/skills"         # WorkBuddy / CodeBuddy
install_into "$HOME/.reasonix/skills"          # Reasonix
install_into "$HOME/.config/opencode/skills"   # OpenCode

echo
echo "安装完成。重启对应 Agent 后说“扮演晓山瑞希 / 瑞希 / Amia / mzk”即可触发。"
echo "补充：Hermes Agent 等源码浏览型工具，直接把仓库内 mizuki-roleplay/ 目录加入其技能路径即可。"

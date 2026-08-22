# mizuki-roleplay 安装脚本（Windows PowerShell）
# 用法: powershell -ExecutionPolicy Bypass -File install.ps1
# 覆盖: Claude Code / Codex CLI / OpenClaw / WorkBuddy / Reasonix / OpenCode
$ErrorActionPreference = "Stop"

$SkillDir = Join-Path $PSScriptRoot "mizuki-roleplay"
if (-not (Test-Path (Join-Path $SkillDir "SKILL.md"))) {
    Write-Error "未找到 $SkillDir\SKILL.md，请从仓库根目录运行"
    exit 1
}

function Install-Into([string]$Target) {
    New-Item -ItemType Directory -Force -Path $Target | Out-Null
    $dest = Join-Path $Target "mizuki-roleplay"
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    Copy-Item -Recurse $SkillDir $dest
    Write-Host "[OK] -> $dest"
}

Install-Into "$HOME\.claude\skills"                  # Claude Code
Install-Into "$HOME\.codex\skills"                   # Codex CLI
Install-Into "$HOME\.agents\skills"                  # Codex / Reasonix 通用目录
Install-Into "$HOME\.openclaw\skills"                # OpenClaw
Install-Into "$HOME\.workbuddy\skills"               # WorkBuddy / CodeBuddy
Install-Into "$HOME\.reasonix\skills"                # Reasonix
Install-Into "$HOME\.config\opencode\skills"         # OpenCode

Write-Host ""
Write-Host "安装完成。重启对应 Agent 后说“扮演晓山瑞希 / 瑞希 / Amia / mzk”即可触发。"

# AISecSight Skill 安装脚本（Windows PowerShell 5.1+）
# 用法：
#   .\scripts\install.ps1                          # 自动探测已安装 Agent 的 skills 目录
#   .\scripts\install.ps1 -SkillsDir "$HOME\.claude\skills"
param(
    [string]$SkillsDir
)

$ErrorActionPreference = 'Stop'
$SkillUrl = 'https://aisecsight.com/api/v1/skill'
$Name     = 'aisecsight'

if (-not $SkillsDir) {
    $candidates = @(
        (Join-Path $HOME '.claude\skills'),
        (Join-Path $HOME '.codex\skills'),
        (Join-Path $HOME '.cursor\skills'),
        (Join-Path $HOME '.gemini\skills'),
        (Join-Path $HOME '.workbuddy\skills')
    )
    $SkillsDir = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
    if (-not $SkillsDir) { $SkillsDir = Join-Path $HOME '.claude\skills' }
}

$Target = Join-Path $SkillsDir $Name
$File   = Join-Path $Target 'SKILL.md'
Write-Host "安装目录: $Target"

New-Item -ItemType Directory -Force -Path $Target | Out-Null

try {
    Invoke-WebRequest -Uri $SkillUrl -OutFile $File -UseBasicParsing -TimeoutSec 30
}
catch {
    throw "下载失败: $($_.Exception.Message) (地址 $SkillUrl)"
}

$content = Get-Content -Path $File -Raw -Encoding UTF8
if (-not $content.StartsWith('---')) { throw "下载内容不像 SKILL.md（缺少 YAML 头）: $File" }
if ($content -notmatch '(?m)^name:\s*aisecsight') { throw "SKILL.md 的 name 字段异常: $File" }

Write-Host "已安装: $File ($($content.Length) 字符)"

$verify = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'verify.py'
if ((Get-Command python -ErrorAction SilentlyContinue) -and (Test-Path $verify)) {
    Write-Host ""
    Write-Host "正在做接口连通性自检……"
    try { & python $verify } catch { Write-Host "自检未全部通过（不影响安装）。" }
}

Write-Host ""
Write-Host "装好了。请新开一个会话再提问，例如："
Write-Host "  「欧盟 AI 法对通用模型提供者的罚款上限是多少？」"

# 英留法签

面向在英国留学的中国学生的 Codex skill：通过中文对话了解申请情况，查验法国官方要求，协助准备短期申根签证材料、填写官网表格及处理预约，最终交付可以逐项核对的打印清单。

当前版本：**0.1.6**。完成利兹大学、未定行程、字母优先的24轮独立模拟，修正了路线过于笼统、学校链接后缺少反馈选项、正式申请前漏问已有申根签证和打印目录重复文件的问题；两处问答另做隔离回归。23次后续回复中19次只回单个字母，准确日期和文件交接按需提供。[完整对话与验证报告](tests/runs/2026-10-22-abcd/report.md)。

行程未定时主动提供帮规划暂定游玩路线的选项；进度与偏好问答优先用简短A/B/C/D选择，允许只回字母或自由表达。用户选规划后复用已有信息，选择自己安排/先做材料后直接推进其他准备。历史记录：[0.1.5交互调整](tests/runs/2026-10-22/conversation-ux-0.1.5.md)、[0.1.4退款来源核查](tests/runs/2026-10-22/report.md)、[0.1.3利兹入口模拟](tests/runs/2026-10-21-leeds/report.md)。

## 第一版的使用体验

用户说“我要办法签”，Codex 先问所在城市、旅行计划及当前进度，然后一步一步推进：

1. 确认是否适合在英国向法国申请，以及具体签证类别。
2. 根据当次官方要求生成个人材料表，说明每份材料去哪里取得。
3. 读取用户指定的材料，分类、检查缺项和前后不一致，保留原件。
4. 在具备浏览器能力且获得相应授权时协助填表、下载回执、查询并操作预约。
5. 按个人官方清单输出打印顺序、文件索引、签字位置和需携带的原件。

英国学生赴法旅游不能误选“赴法国留学”。普通申请一般向 TLScontact 签证中心递交；具体中心、条件和流程每次核对[法国官方英国说明](https://france-visas.gouv.fr/en/web/france-visas/royaume-uni)。

## 安装与调用

可下载[最新版 0.1.6 安装包](dist/yingliufaqian-0.1.6.zip)，解压后得到 `yingliufaqian` 文件夹。

将本项目 `skills/yingliufaqian` 整个文件夹复制到 Codex 用户技能目录 `~/.codex/skills/`。自定义了 `CODEX_HOME` 时使用其下的 `skills/`。已有同名安装时先比较或备份，不直接覆盖。

在本项目根目录运行下面的命令可安装到默认目录；目标已存在时命令会停止：

```sh
python3 - <<'PY'
from pathlib import Path
import os
import shutil
source = Path('skills/yingliufaqian')
target = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex') / 'skills' / source.name
target.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(source, target)
print(f'已安装到 {target}')
PY
```

让 Codex 重新加载技能（必要时重启或新开聊天），检查能否选择“英留法签”，然后输入：

> 请用 $yingliufaqian 帮我准备法国旅游签证。我在英国读书，从第一步开始问我。

也可以说“继续检查这个申请目录”“帮我整理打印材料”“带我填写 France-Visas”。本项目未修改开发者电脑的已安装技能，也未向任何签证网站提交信息。

## 当前交付范围

这是可以安装使用的指令型技能，包含分阶段问答、来源核查、文件规范、申请记录与索引模板和浏览器操作规则。能力来自运行它的 Codex 工具：文件读取、PDF 和浏览器工具缺失时，相关步骤会退回人工指导。

未内置后台预约监控、抢号程序、付款客户端或网站专用适配器；官网登录后的完整申请与预约流程尚未实测。验证码、身份验证、签名及需要本人确认的声明由用户完成。以后若增加 slot 监控，需先验证站点允许的方式和运行环境，再实现有截止时间、可停止的任务。

样本只用于抽象材料类别和流程；可分发目录不含历史申请人的资料。实际使用时，材料应保存在用户选择的私人目录，不能放进本项目或安装目录。

## 开发验证

技能入口：[`skills/yingliufaqian/SKILL.md`](skills/yingliufaqian/SKILL.md)。官方来源及核查局限在技能的 `references/official-sources.md`，行为验收案例在 [`tests/scenarios.md`](tests/scenarios.md)。

本地结构验证不等同于真实官网端到端验证，也不产生 GitHub Required Checks。若以后引入 GitHub CI，遵守仓库所有者的 hosted CI 与本地 fallback 规则。

重建虚构测试材料需要 Python、reportlab；核查产物另需 pypdf。输出目录必须在项目外且尚不存在：

```sh
python3 tests/build_simulation_fixtures.py /tmp/yingliufaqian-forward-new
```

复现真实校名的场景时，可追加 `--university 'University of Leeds'`；这只改变测试场景中的校名，生成物仍明确标注不是学校出具的证明。

本次未定行程场景另外使用 `--refundable-test-bookings` 生成30份PDF测试输入，含虚构的可退订单、付款和接驳时间。输入生成命令与单次运行的检查命令见本次报告；生成输入不等于重演完整对话或验证真实订单。

该命令只生成测试输入，不会自动模拟对话。按测试报告中的分轮过程运行 skill，生成 case 后再检查文件完整性：

```sh
python3 tests/check_simulation_artifacts.py /tmp/yingliufaqian-forward-new
```

首次运行的具体对话和发现已保存在测试报告旁，分发安装包只包含 skill 本身，不包含测试材料或对话。

公开测试记录中的本机用户目录和机器特有临时路径已替换为示例路径，详见[公开前处理记录](tests/publication-notes.json)。测试结果和哈希保留原值；这些路径不是安装要求。

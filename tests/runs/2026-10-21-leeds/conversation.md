# 独立代理逐轮实跑对话

虚构申请人，真实大学公开入口；保留修正前回复及针对性重跑。文件引用指向项目外模拟材料。

## 第1轮 — initial

用户：我是利兹大学 University of Leeds 的学生，第一次办法签，还没开始，带我一步一步弄吧。

助手：我们先确认行程，再决定申请路线。你目前住在利兹吗？打算什么时候去法国、去做什么，途中还会去哪些国家？日期没定也没关系。

## 第2轮 — initial

用户：住在Leeds，12月12到16日去巴黎旅游，只去法国。中国普通护照，21岁，本科全日制，已经注册，英国Student到2027年10月31日，以前没有申根签证。学校证明还没有，应该去哪开？

助手：先申请 **Registration Status Certificate（注册状态证明）**：打开[利兹大学申请说明](https://students.leeds.ac.uk/registration/doc/registration-status-certificate)，在“How to apply”第3步进入 Microsoft Form，申请前确认学校系统里的地址正确。

学校公开说明的目标是 **10个工作日内通过邮件发送电子证明**，繁忙时可能更久；不过该页面目前返回503，我只能核实搜索收录的说明，尚未取得表单直链。若你也打不开，可联系页面列出的 studentinfo@leeds.ac.uk；拿到PDF后交给我核对。

## 第2轮 — rerun-after-reference-update

用户：住在Leeds，12月12到16日去巴黎旅游，只去法国。中国普通护照，21岁，本科全日制，已经注册，英国Student到2027年10月31日，以前没有申根签证。学校证明还没有，应该去哪开？

助手：用学校账号打开[证明申请表](https://forms.office.com/r/hiJGtBreNd)，申请 **Registration Status Certificate（注册状态证明）**，先核对学校系统里的当前地址。学校目标是 **10个工作日内邮件出具**，繁忙时可能更久；拿到PDF后交给我核对。

学校说明站维护中，表单入口已核实可到达微软登录页，登录后的字段和提交功能尚未验证。

## 第3轮 — initial

用户：我昨天已经申请了，邮件说在处理。手上还有注册完成后系统下载的 registration certificate，是不是就能用？等学校的时候我还能先做什么？我自己出钱，预算800镑。

助手：注册完成页面下载的 **registration certificate 不能替代正式在读证明**，学校明确区分了两者；你昨天已申请，就等处理，不用重复申请。[学校说明](https://students.leeds.ac.uk/registration/doc/how-to-register)

等待期间，先打开 [France-Visas 签证助手](https://france-visas.gouv.fr/assistant-visa)，按“中国普通护照、英国居民、法国短期旅游”完成资格问答，把结果和材料清单保存给我核对；我这边还没读到你的个性化结果。自费、预算£800已记下，是否足够还要结合机酒费用和账户资金核算。

## 第4轮 — initial

用户：正式学校证明今天也收到了。我把手里材料都放好了，你帮我检查整理，放到 /tmp/yingliufaqian-leeds-run/case。你可以读 /tmp/yingliufaqian-leeds-run/incoming 里全部PDF，我之后再给官网清单。

助手：已整理好[申请记录和材料索引](/tmp/yingliufaqian-leeds-run/case/申请记录.md)，目前是待补充版本。

先补你本人名下的保险：现有这份的被保险人是另一人。:codex-file-citation{path="/tmp/yingliufaqian-leeds-run/case/01_原始材料/保险_姓名不符.pdf" purpose="source"}

住宿和银行材料的问题也已列入[待办](/tmp/yingliufaqian-leeds-run/case/02_核对与草稿/待办.md)；你给官网清单后，我会继续逐项对照。

## 第5轮 — initial

用户：保险、酒店、share code和流水补好了。现在可以读 /tmp/yingliufaqian-leeds-run/corrections 和 /tmp/yingliufaqian-leeds-run/full-bank 全部PDF；官网已填完，个人清单、正式表和回执在 portal/individual-checklist.pdf、portal/final-form.pdf、portal/receipt.pdf。先给我能打印的部分，预约还没确认。

助手：13页部分打印包已核对，按本次清单 **A4单面、各页一份** 打印。

:codex-file-citation{path="/tmp/yingliufaqian-leeds-run/case/04_打印材料/部分打印包_v1_20261212-1216.pdf" purpose="output"}

第1页申请表需要本人签字、填日期；另备护照原件、两张照片及学校证明原件。预约单尚缺，学校证明的30天时效也要等预约日期确认后复核。

## 第6轮 — initial

用户：TLS付款刚超时了，银行卡显示pending，页面还没给我预约确认。要不要再付一次？

助手：**先不要再付一次。** 银行显示 pending、TLS没有确认单，目前还不能判断付款或预约是否成功。

先查看TLS账户里的现有订单、预约状态和确认邮件；若仍不明确，保留交易时间、金额和订单号，通过TLS官方支持核实这笔交易后再决定是否重试。

## 第7轮 — initial

用户：确认了，付款成功，预约单现在可以看 portal/appointment.pdf。可我行程改成12月13到17日了，改好的交通和酒店在 /tmp/yingliufaqian-leeds-run/changed-dates。之前13页已经打印了，现在怎么办？

助手：旧包 **第3–9页保留，第1、2、13页暂停用**；另打印下面4页，加入预约单，并替换旧第10–12页的交通、酒店和行程。

:codex-file-citation{path="/tmp/yingliufaqian-leeds-run/case/04_打印材料/补打包_v2_预约交通酒店行程.pdf" purpose="output"}

还需要 **12月13–17日的正式申请表、对应回执和覆盖全程的保险**，新版表拿到后再签字。学校证明不用重开；更正申请后还要核对预约绑定的申请编号。

## 第8轮 — initial

用户：都更正好了，新表、回执、新个人清单、保险和更新绑定后的预约单都在 /tmp/yingliufaqian-leeds-run/final-evidence。请给我最终打印包。

助手：**14页最终打印包已核对，完整可打印。** 若沿用之前有效的纸张，只需补打新版第 **1、2、3、13、14页**；替换对应旧页，按新版顺序装好。

:codex-file-citation{path="/tmp/yingliufaqian-leeds-run/case/04_打印材料/最终打印包_TEST-CASE-B_20261213-1217.pdf" purpose="output"}

第1页本人签字、填日期，另携护照原件、两张照片及学校证明原件。预约是 **11月9日10:00（英国时间），Manchester**；服务费£60已付，确认单地址为模拟占位，不能用于实际前往。

## 第9轮 — initial

用户：新表已经打印签字填日期了，护照、两张照片、学校证明原件都装好了。接下来假设时间到了11月9日，我按预约递交了；再假设几天后通知护照寄回了，是不是获签了？

助手：在这个假设里，**护照寄回通知不代表获签**。收到护照后，先查看是否有签证贴纸或决定信；如果有贴纸，还要核对身份、签证地域、类别、有效日期、停留天数和入境次数，才能判断是否适用于12月13–17日的行程。

## 第10轮 — initial

用户：收到护照了，有签证贴纸。姓名护照号都正确，有效期2026年12月1日到2027年3月1日，DURATION OF STAY 30，NUMBER OF ENTRIES MULT。能去我这趟巴黎吗？

助手：按你转述，**12月13–17日共5天，在签证有效期内，也未超过30天**；但还不能确认这张签证适用于法国。

请把贴纸的 **VALID FOR / VALABLE POUR（有效地域）** 和 **TYPE OF VISA / TYPE DE VISA（签证类别）** 两栏原文告诉我。

## 第11轮 — initial

用户：VALID FOR 写 ETATS SCHENGEN，没有排除国家；TYPE OF VISA 是 C。过去180天没去过申根，这张也还没用。

助手：**根据你转述的完整信息，这张签证符合你12月13–17日巴黎旅游的需要**：全申根C类签证覆盖法国，5天行程在有效期及未使用的30天额度内，也符合你所述的既往停留情况。[签证字段说明](https://www.mfa.gov.cn/wjbzwfwpt/kzx/tzgg/202406/t20240626_11441854.html) · [短期停留规则](https://france-visas.gouv.fr/en/web/france-visas/visa-de-court-sejour)

记录已更新为“用户报告获签，按转述完成本次行程适用性核对”。

## 第3轮 — rerun-concision

用户：我昨天已经申请了，邮件说在处理。手上还有注册完成后系统下载的 registration certificate，是不是就能用？等学校的时候我还能先做什么？我自己出钱，预算800镑。

助手：注册完成页下载的 **registration certificate 不能替代正式在读证明**；你已经申请，就等学校邮件，不用重复申请。[学校说明](https://students.leeds.ac.uk/registration/doc/how-to-register)

等待期间，先打开 [France-Visas 签证助手](https://france-visas.gouv.fr/assistant-visa)，按“中国普通护照、英国居民、法国短期旅游”完成问答，保存结果和材料清单给我核对。

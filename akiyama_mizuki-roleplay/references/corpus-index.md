# 剧情语料库目录（corpus index · 三语）

> 来源：pjsk.moe 数据层（zh/ja/en 三服）。格式：`【角色名】台词`；括号内为内心独白；无标记行为旁白。
> ⚠️ 版权：角色与剧情归 SEGA / Colorful Palette，语料仅供学习研究，请勿商用；版权方要求时下架。

## 使用协议（模型必读）

1. **语言切换**：默认中文。用户要求用日语/英语交流时 → 改读 `corpus/ja/` 或 `corpus/en/` 对应文件校准口吻与称呼，并**用该语言扮演**；切回中文同理。语料路径 = `corpus/{zh|ja|en}/…`。
2. **先查索引，再读文件**：按 (type, id) 定位三个语言的文件路径，再 Read 对应单文件（500-1,600 行，禁止全量加载）。
3. **说话人变体**：`【瑞希】`（zh/ja）/`【Mizuki】`（en）是本人；`【小学生瑞希】`/`【Kid Mizuki】` 为幼年期；`【优希】`=姐姐、`【瑞希的母亲】`/`【Mizuki's Mother】` 等家人**不是**瑞希；`【A&B&瑞希】` 为多人合说。
4. **引用纪律**：生成新台词为主；直接引用单次 ≤2 句并注明出处（语言+期数）。不整段复述。
5. **时期判定**：145/150 期是瑞希心态分水岭（守密→坦白），回答前先核对所在时期。
6. **改名铁律**：说话人标签可改（用 `rename_speaker.py`，支持 --lang），对话正文与称呼一律不动。

## 主线剧情（25时）
| ID | 中文标题 | 日本語タイトル | English Title | 行数 z/j/e | 瑞希台词 z/j/e |
|---|---|---|---|---|---|
| main-01 | opening | opening | opening | 83 / 85 / 78 | 0 / 0 / 0 |
| main-02 | midnight-meet-up | midnight-meet-up | midnight-meet-up | 108 / 107 / 74 | 0 / 0 / 0 |
| main-03 | white-miku | white-miku | white-miku | 73 / 73 / 61 | 7 / 7 / 7 |
| main-04 | own | own | own | 136 / 137 / 97 | 0 / 0 / 0 |
| main-05 | i-m-a-good-girl | i-m-a-good-girl | i-m-a-good-girl | 159 / 159 / 118 | 0 / 0 / 0 |
| main-06 | vanishing-snow | vanishing-snow | vanishing-snow | 104 / 104 / 85 | 0 / 0 / 0 |
| main-07 | empty-sekai | empty-sekai | empty-sekai | 121 / 122 / 91 | 11 / 11 / 11 |
| main-08 | though-i-want-to-disappear | though-i-want-to-disappear | though-i-want-to-disappear | 125 / 126 / 100 | 18 / 18 / 18 |
| main-09 | amateur-painter | amateur-painter | amateur-painter | 111 / 113 / 97 | 10 / 10 / 10 |
| main-10 | i-just-want-to-be-myself | i-just-want-to-be-myself | i-just-want-to-be-myself | 86 / 86 / 67 | 32 / 32 / 32 |
| main-11 | the-missing-sound | the-missing-sound | the-missing-sound | 125 / 125 / 94 | 10 / 10 / 10 |
| main-12 | music-for-happiness | music-for-happiness | music-for-happiness | 149 / 151 / 119 | 0 / 0 / 0 |
| main-13 | a-single-song | a-single-song | a-single-song | 85 / 84 / 74 | 0 / 0 / 0 |
| main-14 | who-am-i | who-am-i | who-am-i | 102 / 102 / 79 | 0 / 0 / 0 |
| main-15 | to-be-so-lonely | to-be-so-lonely | to-be-so-lonely | 93 / 94 / 70 | 35 / 35 / 35 |
| main-16 | before-i-disappear | before-i-disappear | before-i-disappear | 82 / 85 / 68 | 17 / 17 / 17 |
| main-17 | dissolve-away | dissolve-away | dissolve-away | 77 / 77 / 68 | 2 / 2 / 2 |
| main-18 | their-curse | their-curse | their-curse | 89 / 90 / 72 | 4 / 4 / 4 |
| main-19 | desire-to-save | desire-to-save | desire-to-save | 143 / 142 / 102 | 12 / 12 / 12 |
| main-20 | composing-the-future | composing-the-future | composing-the-future | 102 / 103 / 92 | 11 / 11 / 11 |
| main-21 | nightcord-at-25 | nightcord-at-25 | nightcord-at-25.en-1 +1eps | 103 / 104 / 154 | 16 / 16 / 32 |

## 活动剧情（瑞希出场）
| ID | 中文标题 | 日本語タイトル | English Title | 行数 z/j/e | 瑞希台词 z/j/e |
|---|---|---|---|---|---|
| ev-002 | caged-marionette | caged-marionette ほか8話 | caged-marionette.en-1 +7eps | 775 / 784 / 635 | 78 / 78 / 78 |
| ev-007 | let-s-see-this-play | let-s-see-this-play ほか8話 | let-s-see-this-play.en-1 +7eps | 709 / 715 / 560 | 193 / 193 / 193 |
| ev-009 | a-new-year-for-idols | a-new-year-for-idols ほか11話 | a-new-year-for-idols.en-1 +10eps | 1096 / 1103 / 932 | 52 / 52 / 52 |
| ev-014 | a-lonely-sekai | a-lonely-sekai ほか8話 | a-lonely-sekai.en-1 +7eps | 891 / 914 / 719 | 71 / 71 / 71 |
| ev-019 | a-moment-of-happiness | a-moment-of-happiness ほか8話 | a-moment-of-happiness.en-1 +7eps | 831 / 842 / 686 | 281 / 281 / 281 |
| ev-022 | a-new-encounter | a-new-encounter ほか8話 | a-new-encounter.en-1 +7eps | 1161 / 1208 / 858 | 139 / 139 / 139 |
| ev-026 | a-gentle-smile | a-gentle-smile ほか8話 | a-gentle-smile.en-1 +7eps | 864 / 886 / 735 | 167 / 167 / 167 |
| ev-029 | i-m-not-giving-up | i-m-not-giving-up ほか8話 | i-m-not-giving-up.en-1 +7eps | 1304 / 1338 / 1058 | 89 / 89 / 89 |
| ev-035 | a-dim-light | a-dim-light ほか8話 | a-dim-light.en-1 +7eps | 841 / 878 / 713 | 81 / 81 / 81 |
| ev-036 | a-chance-meeting | a-chance-meeting ほか10話 | a-chance-meeting.en-1 +9eps | 1358 / 1409 / 1102 | 36 / 36 / 36 |
| ev-039 | encounter | encounter ほか8話 | encounter.en-1 +7eps | 816 / 842 / 686 | 263 / 263 / 263 |
| ev-045 | a-big-wish | a-big-wish ほか9話 | a-big-wish.en-1 +8eps | 1267 / 1276 / 998 | 23 / 23 / 23 |
| ev-047 | and-then-we-met | and-then-we-met ほか8話 | and-then-we-met.en-1 +7eps | 1073 / 1089 / 859 | 21 / 21 / 21 |
| ev-051 | a-finale-full-of-smiles | a-finale-full-of-smiles ほか8話 | a-finale-full-of-smiles.en-1 +7eps | 1320 / 1344 / 1003 | 85 / 85 / 85 |
| ev-053 | fear-of-getting-left-behind | fear-of-getting-left-behind ほか8話 | fear-of-getting-left-behind.en-1 +7eps | 1196 / 1198 / 974 | 61 / 61 / 61 |
| ev-054 | a-new-spring-menu | a-new-spring-menu ほか8話 | a-new-spring-menu.en-1 +7eps | 1004 / 1039 / 832 | 15 / 15 / 15 |
| ev-058 | a-twist | a-twist ほか8話 | a-twist.en-1 +7eps | 1455 / 1456 / 1099 | 153 / 153 / 153 |
| ev-060 | a-blessed-costume | a-blessed-costume ほか8話 | a-blessed-costume.en-1 +7eps | 1544 / 1573 / 1238 | 0 / 0 / 0 |
| ev-061 | a-very-loose-thread | a-very-loose-thread ほか8話 | a-very-loose-thread.en-1 +7eps | 1143 / 1156 / 943 | 76 / 76 / 76 |
| ev-063 | an-idol-s-tutelage | an-idol-s-tutelage ほか8話 | an-idol-s-tutelage.en-1 +7eps | 1362 / 1369 / 1127 | 18 / 18 / 18 |
| ev-068 | a-gift-from-my-big-sis | a-gift-from-my-big-sis ほか8話 | a-gift-from-my-big-sis.en-1 +7eps | 1748 / 1750 / 1402 | 544 / 544 / 544 |
| ev-072 | a-flyer-full-of-our-thoughts | a-flyer-full-of-our-thoughts ほか10話 | a-flyer-full-of-our-thoughts.en-1 +9eps | 2392 / 2398 / 1900 | 75 / 75 / 75 |
| ev-077 | repressed-feelings | repressed-feelings ほか8話 | repressed-feelings.en-1 +6eps | 1195 / 1216 / 883 | 33 / 33 / 28 |
| ev-081 | a-new-year-s-show-with-everyone | a-new-year-s-show-with-everyone ほか8話 | a-new-year-s-show-with-everyone.en-1 +7eps | 1496 / 1518 / 1214 | 22 / 22 / 22 |
| ev-084 | a-memorable-scent | a-memorable-scent ほか8話 | a-memorable-scent.en-1 +7eps | 1259 / 1313 / 976 | 22 / 22 / 22 |
| ev-089 | an-unsettling-notification | an-unsettling-notification ほか8話 | an-unsettling-notification.en-1 +7eps | 950 / 1015 / 816 | 45 / 45 / 45 |
| ev-093 | in-spite-of-fear | in-spite-of-fear ほか8話 | in-spite-of-fear.en-1 +7eps | 946 / 997 / 834 | 313 / 313 / 313 |
| ev-096 | a-little-persistence | a-little-persistence ほか8話 | a-little-persistence.en-1 +7eps | 1412 / 1539 / 1183 | 149 / 149 / 149 |
| ev-100 | an-outstretched-hand | an-outstretched-hand ほか8話 | an-outstretched-hand.en-1 +7eps | 908 / 939 / 809 | 34 / 34 / 34 |
| ev-101 | constellation-of-song | constellation-of-song ほか8話 | constellation-of-song.en-1 +7eps | 1022 / 1069 / 843 | 3 / 3 / 3 |
| ev-102 | a-lifeline-gig | a-lifeline-gig ほか8話 | a-lifeline-gig.en-1 +7eps | 1175 / 1177 / 920 | 111 / 111 / 111 |
| ev-105 | a-mysterious-sekai | a-mysterious-sekai ほか8話 | a-mysterious-sekai.en-1 +7eps | 785 / 791 / 660 | 3 / 3 / 3 |
| ev-107 | a-great-day-to-study | a-great-day-to-study ほか8話 | a-great-day-to-study.en-1 +7eps | 1055 / 1059 / 833 | 134 / 134 / 134 |
| ev-108 | a-new-class | a-new-class ほか8話 | a-new-class.en-1 +7eps | 784 / 790 / 667 | 5 / 5 / 5 |
| ev-112 | frustration | frustration ほか10話 | frustration.en-1 +9eps | 1238 / 1262 / 1101 | 159 / 159 / 159 |
| ev-114 | a-mess-of-a-meeting | a-mess-of-a-meeting ほか8話 | a-mess-of-a-meeting.en-1 +7eps | 1341 / 1351 / 1057 | 6 / 6 / 6 |
| ev-116 | a-warm-melody | a-warm-melody ほか8話 | a-warm-melody.en-1 +7eps | 718 / 750 / 622 | 16 / 16 / 16 |
| ev-117 | a-new-year-s-gift-search | a-new-year-s-gift-search ほか8話 | a-new-year-s-gift-search.en-1 +7eps | 989 / 993 / 807 | 226 / 226 / 226 |
| ev-120 | a-reliable-helper | a-reliable-helper ほか8話 | a-reliable-helper.en-1 +7eps | 1271 / 1292 / 998 | 8 / 8 / 8 |
| ev-123 | doing-our-homework | doing-our-homework ほか8話 | doing-our-homework.en-1 +7eps | 892 / 892 / 747 | 18 / 18 / 18 |
| ev-127 | a-melancholy-morning | a-melancholy-morning ほか8話 | a-melancholy-morning.en-1 +7eps | 781 / 775 / 666 | 19 / 19 / 19 |
| ev-134 | a-warm-walk-home | a-warm-walk-home ほか8話 | a-warm-walk-home.en-1 +7eps | 759 / 767 / 679 | 89 / 89 / 89 |
| ev-139 | admiration-and-joy | admiration-and-joy ほか8話 | admiration-and-joy.en-1 +7eps | 1135 / 1158 / 937 | 0 / 0 / 0 |
| ev-141 | a-happy-smiley-test-of-courage | a-happy-smiley-test-of-courage ほか8話 | a-happy-smiley-test-of-courage.en-1 +7eps | 1077 / 1110 / 900 | 30 / 30 / 30 |
| ev-144 | a-performance-from-scratch | a-performance-from-scratch ほか10話 | a-performance-from-scratch.en-1 +9eps | 1417 / 1407 / 1077 | 16 / 16 / 16 |
| ev-145 | a-friend-s-wish | a-friend-s-wish ほか8話 | a-friend-s-wish.en-1 +7eps | 967 / 956 / 843 | 315 / 315 / 321 |
| ev-150 | conflicted | conflicted ほか8話 | conflicted.en-1 +7eps | 756 / 742 / 643 | 126 / 118 / 126 |
| ev-155 | a-change-of-perspective | a-change-of-perspective ほか8話 | a-change-of-perspective.en-1 +7eps | 969 / 976 / 807 | 10 / 10 / 10 |
| ev-156 | a-fun-sewing-session | a-fun-sewing-session ほか8話 | a-fun-sewing-session.en-1 +7eps | 973 / 991 / 789 | 44 / 44 / 44 |
| ev-160 | begin-preparations | begin-preparations ほか8話 | begin-preparations.en-1 +7eps | 1029 / 1033 / 836 | 66 / 66 / 66 |
| ev-161 | a-mother-s-love | a-mother-s-love ほか8話 | a-mother-s-love.en-1 +7eps | 832 / 835 / 723 | 34 / 34 / 34 |
| ev-165 | dialogue | dialogue ほか8話 | dialogue.en-1 +7eps | 805 / 808 / 736 | 17 / 17 / 17 |
| ev-170 | a-faint-dream-of-the-past | a-faint-dream-of-the-past ほか11話 | a-faint-dream-of-the-past.en-1 +10eps | 1170 / 1159 / 1006 | 118 / 118 / 118 |
| ev-177 | a-dazzling-sight | a-dazzling-sight ほか8話 | a-dazzling-sight.en-1 +7eps | 849 / 863 / 715 | 300 / 300 / 300 |
| ev-179 | link-the-beats | untitled ほか15話 | — | 2324 / 2207 / — | 10 / 10 / — |
| ev-181 | our-golden-days | untitled ほか8話 | — | 967 / 967 / — | 110 / 110 / — |

## 自我介绍
| ID | 中文标题 | 日本語タイトル | English Title | 行数 z/j/e | 瑞希台词 z/j/e |
|---|---|---|---|---|---|
| intro-1 | intro-1 | intro-1 | intro-1 | 62 / 61 / 33 | 32 / 31 / 31 |
| intro-2 | intro-2 | intro-2 | intro-2 | 47 / 47 / 30 | 23 / 23 / 23 |

## 区域对话（日常碎片，三语各 77 条）

| ID | 中文 | 日本語 | English | 行数 z/j/e | 瑞希台词 z/j/e |
|---|---|---|---|---|---|
| area-as_1_058 | — | — | — | 4 / 4 / 3 | 3 / 3 / 3 |
| area-as_1_059 | — | — | — | 5 / 5 / 3 | 3 / 3 / 3 |
| area-as_1_060 | — | — | — | 6 / 6 / 3 | 3 / 3 / 3 |
| area-as_1_103 | — | — | — | 6 / 6 / 3 | 3 / 3 / 3 |
| area-as_1_104 | — | — | — | 5 / 5 / 3 | 3 / 3 / 3 |
| area-as_1_105 | — | — | — | 6 / 6 / 3 | 3 / 3 / 3 |
| area-as_2_065 | — | — | — | 9 / 9 / 5 | 2 / 2 / 2 |
| area-as_2_078 | — | — | — | 7 / 7 / 6 | 3 / 3 / 3 |
| area-as_2_129 | — | — | — | 10 / 10 / 10 | 4 / 4 / 4 |
| area-as_2_131 | — | — | — | 9 / 9 / 8 | 3 / 3 / 3 |
| area-as_2_133 | — | — | — | 11 / 11 / 10 | 4 / 4 / 4 |
| area-as_2_138 | — | — | — | 9 / 9 / 9 | 4 / 4 / 4 |
| area-as_2_139 | — | — | — | 12 / 12 / 10 | 4 / 4 / 4 |
| area-as_2_141 | — | — | — | 6 / 6 / 7 | 2 / 2 / 2 |
| area-as_2_142 | — | — | — | 10 / 10 / 11 | 4 / 4 / 4 |
| area-as_2_143 | — | — | — | 7 / 7 / 7 | 3 / 3 / 3 |
| area-as_2_148 | — | — | — | 9 / 9 / 10 | 3 / 3 / 3 |
| area-as_2_149 | — | — | — | 10 / 10 / 10 | 3 / 3 / 3 |
| area-as_2_155 | — | — | — | 8 / 8 / 5 | 2 / 2 / 2 |
| area-as_2_156 | — | — | — | 9 / 9 / 7 | 3 / 3 / 3 |
| area-as_2_158 | — | — | — | 9 / 9 / 8 | 3 / 3 / 3 |
| area-as_2_159 | — | — | — | 11 / 11 / 12 | 4 / 4 / 4 |
| area-as_2_160 | — | — | — | 8 / 8 / 7 | 3 / 3 / 3 |
| area-as_2_161 | — | — | — | 11 / 11 / 9 | 4 / 4 / 4 |
| area-as_2_162 | — | — | — | 11 / 12 / 11 | 4 / 4 / 4 |
| area-as_2_163 | — | — | — | 9 / 11 / 10 | 3 / 3 / 3 |
| area-as_2_266 | — | — | — | 8 / 8 / 5 | 3 / 3 / 3 |
| area-as_2_271 | — | — | — | 8 / 8 / 6 | 3 / 3 / 3 |
| area-as_2_276 | — | — | — | 10 / 10 / 7 | 4 / 4 / 4 |
| area-as_2_278 | — | — | — | 7 / 7 / 5 | 3 / 3 / 3 |
| area-as_2_279 | — | — | — | 7 / 7 / 5 | 2 / 2 / 2 |
| area-as_2_319 | — | — | — | 9 / 9 / 7 | 4 / 4 / 4 |
| area-as_2_386 | — | — | — | 10 / 10 / 6 | 4 / 4 / 4 |
| area-as_2_396 | — | — | — | 11 / 11 / 6 | 2 / 2 / 2 |
| area-as_2_397 | — | — | — | 10 / 10 / 6 | 4 / 4 / 4 |
| area-as_2_398 | — | — | — | 8 / 8 / 6 | 2 / 2 / 2 |
| area-as_2_399 | — | — | — | 13 / 13 / 6 | 3 / 3 / 3 |
| area-as_3_242 | — | — | — | 8 / 8 / 6 | 2 / 2 / 2 |
| area-as_3_243 | — | — | — | 15 / 15 / 9 | 5 / 5 / 5 |
| area-as_3_245 | — | — | — | 14 / 14 / 9 | 3 / 3 / 3 |
| area-as_3_246 | — | — | — | 11 / 12 / 7 | 3 / 3 / 3 |
| area-as_3_248 | — | — | — | 19 / 19 / 10 | 4 / 4 / 4 |
| area-as_3_249 | — | — | — | 13 / 13 / 9 | 5 / 5 / 5 |
| area-as_3_252 | — | — | — | 11 / 11 / 8 | 4 / 4 / 4 |
| area-as_3_255 | — | — | — | 11 / 11 / 9 | 5 / 5 / 5 |
| area-as_3_257 | — | — | — | 12 / 12 / 8 | 4 / 4 / 4 |
| area-as_3_258 | — | — | — | 11 / 11 / 7 | 2 / 2 / 2 |
| area-as_3_260 | — | — | — | 14 / 14 / 9 | 2 / 2 / 2 |
| area-as_3_261 | — | — | — | 14 / 14 / 9 | 4 / 4 / 4 |
| area-as_3_263 | — | — | — | 14 / 14 / 9 | 2 / 2 / 2 |
| area-as_3_264 | — | — | — | 15 / 15 / 9 | 3 / 3 / 3 |
| area-as_3_267 | — | — | — | 11 / 11 / 9 | 3 / 3 / 3 |
| area-as_3_270 | — | — | — | 13 / 13 / 9 | 2 / 2 / 2 |
| area-as_3_272 | — | — | — | 13 / 14 / 8 | 2 / 2 / 2 |
| area-as_3_273 | — | — | — | 14 / 15 / 9 | 5 / 5 / 5 |
| area-as_3_275 | — | — | — | 15 / 15 / 10 | 5 / 5 / 5 |
| area-as_3_276 | — | — | — | 11 / 12 / 8 | 2 / 2 / 2 |
| area-as_3_278 | — | — | — | 17 / 17 / 10 | 6 / 6 / 6 |
| area-as_3_279 | — | — | — | 12 / 12 / 9 | 2 / 2 / 2 |
| area-as_3_281 | — | — | — | 11 / 11 / 6 | 3 / 3 / 3 |
| area-as_3_284 | — | — | — | 12 / 12 / 8 | 3 / 3 / 3 |
| area-as_3_286 | — | — | — | 12 / 12 / 7 | 5 / 5 / 5 |
| area-as_3_287 | — | — | — | 10 / 11 / 7 | 3 / 3 / 3 |
| area-as_3_288 | — | — | — | 15 / 16 / 8 | 4 / 4 / 4 |
| area-as_3_289 | — | — | — | 8 / 8 / 7 | 2 / 2 / 2 |
| area-as_3_290 | — | — | — | 11 / 11 / 8 | 4 / 4 / 4 |
| area-as_3_291 | — | — | — | 9 / 9 / 7 | 3 / 3 / 3 |
| area-as_3_292 | — | — | — | 10 / 10 / 7 | 3 / 3 / 3 |
| area-as_3_293 | — | — | — | 12 / 12 / 8 | 3 / 3 / 3 |
| area-as_3_294 | — | — | — | 12 / 12 / 7 | 2 / 2 / 2 |
| area-as_3_295 | — | — | — | 16 / 16 / 9 | 3 / 3 / 3 |
| area-as_3_297 | — | — | — | 15 / 16 / 9 | 4 / 4 / 4 |
| area-as_3_298 | — | — | — | 11 / 11 / 7 | 3 / 3 / 3 |
| area-as_3_299 | — | — | — | 14 / 14 / 9 | 4 / 4 / 4 |
| area-as_3_300 | — | — | — | 17 / 17 / 10 | 3 / 3 / 3 |
| area-as_4_009 | — | — | — | 22 / 22 / 15 | 3 / 3 / 3 |
| area-as_4_010 | — | — | — | 22 / 22 / 16 | 4 / 4 / 4 |

> 路径：`corpus/{zh,ja,en}/area-talk/{sid}.md`；完整字段（含 cast）见 `corpus_index.json`。

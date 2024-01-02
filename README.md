# nbnhhsh-hoshino
 适用于Hoshino Bot的“能不能好好说话”插件  
# 简介
社交平台上通过拼音首字母缩写指代特定词句的情况越来越多，为了让更多人能勉强理解这一门另类沟通方式、[原作者](https://github.com/itorr)做了这一个划词转义工具。  ~~求求网络弄潮儿们把字打全吧一段话里字母比汉字还多😭~~   
  
本插件功能来自原作者的[‘能不能好好说话’网站](https://lab.magiconch.com/nbnhhsh/)与[‘能不能好好说话’GitHub仓库](https://github.com/itorr/nbnhhsh)，原功能提供了网站在线查询与油猴插件，本插件的原理是调用原作者在GitHub上提供的线上Api实现，本插件不会保存聊天记录与查询内容。
#  效果

![image](https://github.com/Fatfish588/nbnhhsh-hoshino/assets/59791439/e164469c-cb1d-4aa2-bab3-fe0be756987e)

#  部署方式
1.下载或git clone本插件：  
在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目：  
git clone https://github.com/Fatfish588/nbnhhsh-hoshino.git

2.启用：  
在 HoshinoBot\hoshino\config\bot.py 文件的 MODULES_ON 加入 'nbnhhsh-hoshino'。  

3.重启 HoshinoBot。  
#  指令
在群聊中发送“缩写” + 【英文缩写】 + “是什么意思” 触发，中间不要有空格，参考下方的示例和上方的效果。  
因为各种打字习惯不一样，支持常用中英文标点符号结尾，也支持没有标点符号结尾。  
不支持多个缩写放在一个指令中发送。  
示例：  
1、缩写yysy是什么意思  
2、缩写yysy是什么意思？  
3、缩写yysy是什么意思。  

# 碎碎念
很简单的一个小东西，但对我帮助很大，改成Hoshino插件形式分享给大家。  
查询出来的内容均是来自[‘能不能好好说话’](https://github.com/itorr/nbnhhsh)，所以如果有~~潮流词语~~没有被收录请勿在此仓库下回复，欢迎关注[‘能不能好好说话GitHub仓库’](https://github.com/itorr/nbnhhsh)

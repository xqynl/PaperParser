# 期望目标

按章节的读取Paper文字内容，转化为txt格式，便于后期喂给LLM
现在仅需读取Paper的摘要、Intro以及作者信息就可，喂给LLM，

# 进度

利用PyMupdf 读取paper时 难以区分图片部分的文字
Paper可能有的下标、页码都还没做，做个字符串匹配过滤就好
章节匹配问题

通过semanticscholar API搜索论文，不确定能否获得pdf，需要申请key，12/17刚填写申请不知道什么时候可以获得
search_paper.py 调用semanticscholar接口代码，没有key，不知道结果怎么样




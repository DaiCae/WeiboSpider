# 微博爬虫
Forked from https://github.com/nghuyong/WeiboSpider

基于原有项目进行修改,作为[舆论监查平台](https://github.com/DaiCae/PublicOpinionMonitoring)子服务

仅使用search,comment类型爬取模块

## 主要更改如下
- 更改目录结构以集成flask框架
- 自动注册到nacos方便其他微服务调用
- 在comment结果中添加其的mblogid
- 集成rabbitmq管道对结果进行发送
- 修改结果字段为驼峰命名
- 修改日期格式为 yyyy-MM-dd HH:mm:ss
- 修改spider.name命名方式

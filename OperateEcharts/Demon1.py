#  @Function: 柱状图
#　＠Time:2020/5/28 下午12:30
#  @Author:Flank
from pyecharts.charts import Bar
from pyecharts import options as opts # 导入配置模块

bar=Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家",[5, 20, 36, 10, 75, 90])
bar.set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'))
bar.render('./HtmlFile/Demon1.html')





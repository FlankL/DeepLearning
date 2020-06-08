#  @Function:  x轴和y轴交换
#　＠Time:2020/5/28 下午3:48
#  @Author:Flank
from pyecharts.charts import Bar
from pyecharts import options as opts
bar=Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家",[5, 20, 36, 10, 75, 90])
bar.set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'))

bar.render('./HtmlFile/Demon2.html')

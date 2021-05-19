/*
 * @Descripttion: 
 * @version: 
 * @Author: LiQiang
 * @Date: 2021-01-28 13:44:58
 * @LastEditTime: 2021-01-28 14:24:05
 */
// 年龄-心率-患病 三者关系散点图
var sex_distribution=echarts.init(document.getElementById('sex_distribution'),"dark");

sex_distribution_option = {
 tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['未患病', '患病']
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {show: false},
            data: ['男性','女性']
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: '未患病',
            type: 'bar',
            barGap: 0,
            emphasis: {
                focus: 'series'
            },
            data: [320, 332]
        },
        {
            name: '患病',
            type: 'bar',
            emphasis: {
                focus: 'series'
            },
            data: [220, 182]
        },
       ]
};
sex_distribution.setOption(sex_distribution_option)

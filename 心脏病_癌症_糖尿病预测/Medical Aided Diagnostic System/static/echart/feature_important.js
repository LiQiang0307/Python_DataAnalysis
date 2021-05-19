/*
 * @Descripttion: 
 * @version: 
 * @Author: LiQiang
 * @Date: 2021-01-28 13:44:58
 * @LastEditTime: 2021-01-28 14:24:05
 */
// 年龄-血压-患病 三者关系散点图
var important=echarts.init(document.getElementById('important'),"dark");

important_option = {
    title: {
        text: '特征重要性分析' ,
        left: '5%',
        top: '3%'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {            // Use axis to trigger tooltip
            type: 'shadow'        // 'shadow' as default; can also be 'line' or 'shadow'
        }
    },

    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value'
    },
    yAxis: {
        type: 'category',
        data: []
    },
    series: [
        {
            name: 'Direct',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: []
        },

    ]
};
important.setOption(important_option)

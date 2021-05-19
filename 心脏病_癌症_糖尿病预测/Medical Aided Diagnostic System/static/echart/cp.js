/*
 * @Descripttion: 
 * @version: 
 * @Author: LiQiang
 * @Date: 2021-01-28 13:44:58
 * @LastEditTime: 2021-01-28 14:24:05
 */
//胸痛类型
var cp=echarts.init(document.getElementById('cp'),"dark");

cp_option = {
    title:{
        text: '胸痛类型' ,
        left: '5%',
        top: '3%'
    },
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
            name:'胸痛类型',
            axisTick: {show: false},
            data: ['4','3','2','1']
        }
    ],
    yAxis: [
        {name:'数量',
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
            data: []
        },
        {
            name: '患病',
            type: 'bar',
            emphasis: {
                focus: 'series'
            },
            data: []
        },
       ]
};
cp.setOption(cp_option)

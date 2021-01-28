// 年龄-心率-患病 三者关系散点图
var age_thalach=echarts.init(document.getElementById('age_thalach'),"dark");

var data=[[],[]];
age_thalach_option = {
    // backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
    //     offset: 0,
    //     color: '#f7f8fa'
    // }, {
    //     offset: 1,
    //     color: '#cdd0d5'
    // }]),
    title: {
        text: '年龄-心率-与患病三者关系' ,
        left: '5%',
        top: '3%'
    },
    legend: {
        right: '10%',
        top: '3%',
        data: ['患病', '未患病']
    },
    grid: {
        left: '8%',
        top: '10%'
    },
    xAxis: {
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        }
    },
    yAxis: {
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
        scale: true
    },
    series: [{
        name: '患病',
        data: data[0],
        type: 'scatter',
        symbolSize:15,
        emphasis: {
            focus: 'series',
            label: {
                show: true,
                formatter: function (param) {
                    return param.data[3];
                },
                position: 'top'
            }
        },
        itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(120, 36, 50, 0.5)',
            shadowOffsetY: 5,
            color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(251, 118, 123)'
            }, {
                offset: 1,
                color: 'rgb(204, 46, 72)'
            }])
        }
    }, {
        name: '未患病',
        data: data[1],
        type: 'scatter',
        symbolSize: 15,
        emphasis: {
            focus: 'series',
            label: {
                show: true,
                formatter: function (param) {
                    return param.data[3];
                },
                position: 'top'
            }
        },
        itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(25, 100, 150, 0.5)',
            shadowOffsetY: 5,
            color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(129, 227, 238)'
            }, {
                offset: 1,
                color: 'rgb(25, 183, 207)'
            }])
        }
    }]
};
age_thalach.setOption(age_thalach_option)

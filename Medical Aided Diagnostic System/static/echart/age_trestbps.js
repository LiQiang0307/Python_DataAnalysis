/*
 * @Descripttion: 
 * @version: 
 * @Author: LiQiang
 * @Date: 2021-01-28 13:44:58
 * @LastEditTime: 2021-01-28 14:24:05
 */
// 年龄-血压-患病 三者关系散点图
var age_trestbps=echarts.init(document.getElementById('age_trestbps'),"dark");
 var dataBJ = [

    [2,25,""],

];

var dataSH = [

    [31,187,""]
];

age_trestbps_option = {
    title: {
        text: '年龄-血压与患病三者关系' ,
        left: '5%',
        top: '3%'
    },

    color: [
        '#dd4444', '#fec42c', '#80F1BE'
    ],
    legend: {
        top: 10,
        right: '10%',
        data: ['患病', '未患病'],
        textStyle: {
            fontSize: 16
        }
    },
    grid: {
        left: '10%',
        right: 150,
        top: '18%',
        bottom: '10%'
    },
    tooltip: {
         backgroundColor: ['rgba(255,255,255,0.7)'],
    },
    xAxis: {
        type: 'value',
        name: '年龄',
        nameGap: 16,
        nameTextStyle: {
            fontSize: 16
        },
        splitLine: {
            show: false
        },
    },
    yAxis: {
        type: 'value',
        name: '血压',
        nameLocation: 'end',
        nameGap: 20,
        nameTextStyle: {
            fontSize: 16
        },
        splitLine: {
            show: false
        }
    },
    series: [
        {
            name: '患病',
            type: 'scatter',
            data: dataBJ
        },
        {
            name: '未患病',
            type: 'scatter',
            data: dataSH
        },

    ]
};
age_trestbps.setOption(age_trestbps_option)

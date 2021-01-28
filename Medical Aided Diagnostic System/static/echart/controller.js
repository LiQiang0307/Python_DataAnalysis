//控制器，获取数据进行可视化

//年龄-心率-患病三者之间的关系
function scatter_age_thalach() {
    $.ajax({
        url: "/scatter_age_thalach",
        success: function (data) {
            age_thalach_option.series[0].data = data['have'];
            // console.log(data['have']);
            age_thalach_option.series[1].data = data['no'];
            age_thalach.setOption(age_thalach_option);

        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

scatter_age_thalach();
//每隔一秒获取一次数据
// setInterval(scatter_age_thalach,1000*1000);

//患病男女分布
function sex_distribution_() {
    $.ajax({
        url: "/sex_distribution",
        success: function (data) {
            sex_distribution_option.series[0].data = data['no'];
            sex_distribution_option.series[1].data = data['have'];

            sex_distribution.setOption(sex_distribution_option);

        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

sex_distribution_();

//胸痛类型分布
function cp_() {
    $.ajax({
        url: "/cp",
        success: function (data) {
            cp_option.series[0].data = data['no'];
            cp_option.series[1].data = data['have'];

            cp.setOption(cp_option);

        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

cp_();

//年龄-血压-患病三者之间的关系
function age_trestbps_() {
    $.ajax({
        url: "/age_trestbps",
        success: function (data) {
            age_trestbps_option.series[0].data = data['have'];
            // console.log(data['have']);
            age_trestbps_option.series[1].data = data['no'];
            age_trestbps.setOption(age_trestbps_option);

        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

age_trestbps_();

//血压与心率
//年龄-血压-患病三者之间的关系
function trestbps_thalach_() {
    $.ajax({
        url: "/trestbps_thalach",
        success: function (data) {
            trestbps_thalach_option.series[0].data = data['have'];
            // console.log(data['have']);
            trestbps_thalach_option.series[1].data = data['no'];
            trestbps_thalach.setOption(trestbps_thalach_option);

        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

trestbps_thalach_();

//获取协方差计算
function corr_() {
    $.ajax({
        url: "/corr",
        success: function (data) {
            data_corr = data;
        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

corr_();

//特征重要性分析
function feature_important() {
    $.ajax({
        url: "/feature_important",
        success: function (data) {
            important_option.yAxis.data = data['y'];
            important_option.series[0].data = data['x'];
            important.setOption(important_option);
        },
        error: function (xhr, type, errorThrown) {
        }
    })
}

feature_important();
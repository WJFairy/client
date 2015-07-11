if (!window.util) {
    window.util = {};
}


// 设置左边栏导航定位 
util.setNav = function(navClass) {
    $('.nav-bracket ' + navClass).addClass('active').parent('ul').addClass('open').parents('li').addClass('active nav-active open');
}


// 根据iframe面body的高度自动调整iframe的高度
util.setIframeAutoHeight = function(iframe, minHeight) {
    var mainheight;

    minHeight = minHeight || 0;
    iframe = iframe || 'iframe';

    $(iframe).load(function(){
       mainheight = $(this).contents().find("body").height()+30;

       mainheight = mainheight < minHeight ? minHeight : mainheight;
       $(this).height(mainheight);
    }); 

    $(window).resize(function(){
        mainheight = $(iframe).contents().find("body").height()+30;
        mainheight = mainheight < minHeight ? minHeight : mainheight;
        $(iframe).height(mainheight);
    });

    return mainheight;
};

util.getJsonLength = function(json) {
    var length = 0;

    $.each(json, function(index, val) {
        length++;
    });
    return length;
}

// 写入cookie
util.setCookie = function(key, v) {
    document.cookie = key + '=' + v;
}

// 按key从cookie中取值
util.getCookie = function(key) {
    var arrCookie = document.cookie.split(';');
   
    for (var i=0; i<arrCookie.length; i++) {

        var arr = arrCookie[i].split('=');

        // arr[0] 前多了一个空格？
        if (key === $.trim(arr[0])) {
            return arr[1];
        }
    }

    // 没有找到返回空字符串
    return '';
};

// 获取modal（modal可放在当前页面或者父页面）， modalId不带#号
util.getModal = function(modalId) {
    return $(document.getElementById(modalId) 
                    || window.parent.document.getElementById(modalId)
                    || window.parent.parent.document.getElementById(modalId));
}

// 获取modal（modal可放在当前页面或者父页面）， modalId不带#号
util.getModal = function(modalId) {
    return $(document.getElementById(modalId) 
                    || window.parent.document.getElementById(modalId)
                    || window.parent.parent.document.getElementById(modalId));
};

util.alert = function(txt) {
    var tmp = '<div class="myalert widget-box light-border" style="opacity: 1;"><div class="widget-header"><h5 class="smaller">桥梁信息管理系统</h5><div class="widget-toolbar no-border"><a href="#" data-action="close"> <i class="icon-remove"></i></a></div></div><div class="widget-body"><div class="widget-main padding-6"><div class="alert"></div><a class="btn btn-sm btn-danger" href="#" data-action="close">确定</a></div></div></div>';

    $tmp = $(tmp);
    $tmp.find('.alert').text(txt);
    $('body').append($tmp);

    $('.myalert a').click(function(event) {
        $('.myalert').css('opacity', '0');
    });
};


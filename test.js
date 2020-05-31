var result;

function callEleMeFun(url_path) { //定义导出函数
    Java.perform(function () {
        var a = Java.use('class');//这边改了，需要自己去找饿了么的加密类
        var context = Java.use('android.app.ActivityThread').currentApplication().getApplicationContext();
        var res = a.sneer(context, "4f93e640-5c6f-4980-bd3d-c1256672a64d", url_path, "a");
        result = {"ex_r": res[0], "ex_dc": res[1], "ex_d": res[2]};
    });
    return result;
}

function callDYFun(url) { //定义导出函数
    Java.perform(function () {
        var ss = Java.use('com.ss.sys.ces.gg.tt$1');
        var HashMap = Java.use("java.util.HashMap").$new();
        var jsonObj = Java.use('org.json.JSONObject');
        var str = Java.use("java.lang.String");
        var res = jsonObj.$new(ss.$new().a(url, HashMap));
        result = str.valueOf(res);
    });
    return result;
}

rpc.exports = {
    callsecretfunctioneleme: callEleMeFun,
    callsecretfunctionedy: callDYFun,
};
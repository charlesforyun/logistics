$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();
        var telephone = $("input[name='telephone']").val();
        var password = $("input[name='password']").val();
        var remember = $("input[name='remember']").val();

        myajax.post({
            'url': '/logistics/login/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember,
            },
            'success': function (data) {
                console.log(data);
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
});

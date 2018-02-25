$(document).ready(function () {

    // login form

    $(".login_link").click(function () {
        $(".opacity").fadeIn(500);
        $(".login_form").fadeIn(500);
        $(".close_login").fadeIn(500);
        $(".register_sheet").fadeIn(600);
        $(".forget_sheet").fadeIn(550);
        $(".backg_sheet").fadeIn(500);
        $(".login_forget").hide();
        $(".log_register").hide();
    });

    $(".close_login").click(function () {
        $(".opacity").fadeOut(300);
        $(".login_form").fadeOut(300);
        $(".close_login").fadeOut(300);
        $(".forget_sheet").fadeOut(250);
        $(".register_sheet").fadeOut(200);
        $(".backg_sheet").fadeOut(150);
    });

    $(this).keydown(function (eventObject) {
        if (eventObject.which == 27) {
            $(".opacity").fadeOut(300);
            $(".login_form").fadeOut(300);
            $(".close_login").fadeOut(300);
            $(".forget_sheet").fadeOut(250);
            $(".register_sheet").fadeOut(200);
            $(".backg_sheet").fadeOut(150);
        }
    });

    $(".login_help_a").click(function () {
        $(".login_form").fadeOut(300);
        $(".login_forget").show();
    });

    $(".login_back_a").click(function () {
        $(".login_form").fadeIn(500);
        $(".login_forget").fadeOut(300);
        $(".forget_sheet").fadeIn(500);
    });

    $(".first_login_a").click(function () {
        $(".log_register").show();
        $(".login_form").fadeOut(500);
        $(".forget_sheet").fadeOut(450);
    });

});
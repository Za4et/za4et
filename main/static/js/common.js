$(document).ready(function () {

        //preloader

        var preloader = document.getElementById("preloader_disp");

        function fadeOutnojquery(el) {
            el.style.opacity = 1;
            var interpreloader = setInterval(function () {
                el.style.opacity = el.style.opacity - 0.02;
                if (el.style.opacity <= 0.02) {
                    clearInterval(interpreloader);
                    preloader.style.display = "none";
                }
            }, 16);
        }

        window.onload = function () {
            setTimeout(function () {
                    fadeOutnojquery(preloader);
                }
                , 3500);
        };

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

    }
);
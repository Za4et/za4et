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

        // search

        $(".open_main_search").click(function () {
            $(".main_search").fadeIn(500);
        });

        $(".search_main_close").click(function () {
            $(".main_search").fadeOut(300);
        });

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
                $(".main_search").fadeOut(300);
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

        /* --- bac --- */

        if ($('.baccalaureate input').is(':checked')) {
            $('.direc_opac_bac').css('opacity', '1');
            $('.direc_opac_bac').css('background-color', '#52011A');
            $('.direc_opac_spe').css('opacity', '');
            $('.direc_opac_spe').css('background-color', '');
            $('.direc_opac_mag').css('opacity', '');
            $('.direc_opac_mag').css('background-color', '');
            $('.text_direc_bac').css('opacity', '0');
            $('.block_course_bac').css('opacity', '1');
            $('.text_direc_spe').css('opacity', '');
            $('.block_course_spe').css('opacity', '');
            $('.text_direc_mag').css('opacity', '');
            $('.block_course_mag').css('opacity', '');
        }

        $('.block_course_bac').click(function () {
            if ($('.baccalaureate input').is(':checked')) {
                $('.direc_opac_bac').css('opacity', '1');
                $('.direc_opac_bac').css('background-color', '#52011A');
                $('.direc_opac_spe').css('opacity', '');
                $('.direc_opac_spe').css('background-color', '');
                $('.direc_opac_mag').css('opacity', '');
                $('.direc_opac_mag').css('background-color', '');
                $('.direc_opac_mag').css('opacity', '');
                $('.text_direc_bac').css('opacity', '0');
                $(this).css('opacity', '1');
                $('.text_direc_spe').css('opacity', '');
                $('.block_course_spe').css('opacity', '');
                $('.text_direc_mag').css('opacity', '');
                $('.block_course_mag').css('opacity', '');
            }
        })

        /* --- bac end --- */

        /* --- spe --- */

        if ($('.specialty input').is(':checked')) {
            $('.direc_opac_bac').css('opacity', '');
            $('.direc_opac_bac').css('background-color', '');
            $('.direc_opac_spe').css('opacity', '1');
            $('.direc_opac_spe').css('background-color', '#52011A');
            $('.direc_opac_mag').css('opacity', '');
            $('.direc_opac_mag').css('background-color', '');
            $('.text_direc_bac').css('opacity', '');
            $('.block_course_bac').css('opacity', '');
            $('.text_direc_spe').css('opacity', '0');
            $('.block_course_spe').css('opacity', '1');
            $('.text_direc_mag').css('opacity', '');
            $('.block_course_mag').css('opacity', '');
        }

        $('.block_course_spe').click(function () {
            if ($('.specialty input').is(':checked')) {
                $('.direc_opac_bac').css('opacity', '');
                $('.direc_opac_bac').css('background-color', '');
                $('.direc_opac_spe').css('opacity', '1');
                $('.direc_opac_spe').css('background-color', '#52011A');
                $('.direc_opac_mag').css('opacity', '');
                $('.direc_opac_mag').css('background-color', '');
                $('.direc_opac_mag').css('opacity', '');
                $('.text_direc_bac').css('opacity', '');
                $('.block_course_bac').css('opacity', '');
                $('.text_direc_spe').css('opacity', '0');
                $(this).css('opacity', '1');
                $('.text_direc_mag').css('opacity', '');
                $('.block_course_mag').css('opacity', '');
            }
        })

        /* --- spe end --- */

        /* --- mag --- */

        if ($('.magistracy input').is(':checked')) {
            $('.direc_opac_bac').css('opacity', '');
            $('.direc_opac_bac').css('background-color', '');
            $('.direc_opac_spe').css('opacity', '');
            $('.direc_opac_spe').css('background-color', '');
            $('.direc_opac_mag').css('opacity', '1');
            $('.direc_opac_mag').css('background-color', '#52011A');
            $('.text_direc_bac').css('opacity', '');
            $('.block_course_bac').css('opacity', '');
            $('.text_direc_spe').css('opacity', '');
            $('.block_course_spe').css('opacity', '');
            $('.text_direc_mag').css('opacity', '0');
            $('.block_course_mag').css('opacity', '1');
        }

        $('.block_course_mag').click(function () {
            if ($('.magistracy input').is(':checked')) {
                $('.direc_opac_bac').css('opacity', '');
                $('.direc_opac_bac').css('background-color', '');
                $('.direc_opac_spe').css('opacity', '');
                $('.direc_opac_spe').css('background-color', '');
                $('.direc_opac_mag').css('opacity', '1');
                $('.direc_opac_mag').css('background-color', '#52011A');
                $('.text_direc_bac').css('opacity', '');
                $('.block_course_bac').css('opacity', '');
                $('.text_direc_spe').css('opacity', '');
                $('.block_course_spe').css('opacity', '');
                $('.text_direc_mag').css('opacity', '0');
                $(this).css('opacity', '1');
            }
        })

        /* --- mag end --- */

        /*jrnls*/

        $('.journ_frame').hover(
            function () {
                $('.journ_win_frame').css('background-color', '#AC0439')
            },
            function () {
                $('.journ_win_frame').css('background-color', '#333233')
            });


        /*jrnls end*/

        /* lbrr */

        $('.lib_frame').hover(
            function () {
                $('.lib_backg_frame').css('background-color', '#AC0439')
            },
            function () {
                $('.lib_backg_frame').css('background-color', '#333233')
            });

        /* lbrr end */
    }
);
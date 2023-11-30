$(document).ready(function() {
            var n = $(".flower1 span").length;
            var val = -90;
            var ans = 20;
            $(".flower1 span").not(":first-child").click(function() {
                $(".flower1 span").css({
                    "transform": "translate(-50%, -50%) rotate(" + 0 + "deg)"
                });
                $(".flower1 span").not(":first-child").fadeOut(450);

            });
            $(".flower1 span").eq(0).click(function() {
                $(".flower1 span").fadeIn(500);
                for (i = 0; i < n; i++) {
                    var an2 = ans * i - 90;
                    $(".flower1 span").eq(i).css({
                        "transform": "translate(-50%, -50%) rotate(" + an2 + "deg)"
                    });
                }
            });
            for (i = 0; i < n; i++) {
                var an2 = ans * i - 90;
                $(".flower1 span").eq(i).css({
                    "transform": "translate(-50%, -50%) rotate(" + an2 + "deg)"
                })
            }
        });

$(document).ready(function () {
    function setRandImage() {
        var images = [
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg",
            "7.jpg",
            "8.jpg",
            "9.jpg",
            "10.jpg",
            "11.jpg",
            "12.jpg",
            "13.jpg",
            "14.jpg",
            "15.jpg",
            "16.jpg",
            "17.jpg"
        ];
        var i;
        i = parseInt(Math.random() * images.length);
        $("#garage").fadeOut(function () {
            $("#garage").attr("src", "img/" + images[i]);
            $("#garage").fadeIn();
        });
    }
    function setDeathImage() {
        $("#garage").fadeOut(function () {
            $("#garage").attr("src", "img/dead.jpg");
            $("#garage").fadeIn();
        });
    }
    $("#refresh-card").click(function () {
        $("#message").text("");
        $.get("validate-token")
            .done(function (data, status) {
                if (data["message"] == "0") {
                    setRandImage();
                }
                else if (data["message"] == "1") {
                    setDeathImage();
                }
                else {
                    $("#garage").fadeOut();
                    $("#message").text(data["message"]).css("visibility", "hidden");
                    $("#message").fadeIn();
                }
            })
            .fail(function (data) {
                setRandImage();
            })
    });
});
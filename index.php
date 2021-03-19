<!doctype html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
    <title>Hello, world!</title>

    <script>
    $(function() {
        $('button').on('click', function(event) {
            event.preventDefault();
            var tablink = "";
            tablink = document.getElementById("check").value;
            if (tablink) {
                $("#url_").text("The URL being tested is: " + tablink);
                var xhr = new XMLHttpRequest();
                params = "url=" + tablink;
                alert(params);
                var markup = "url=" + tablink + "&html=" + document.documentElement.innerHTML;
                xhr.open("POST", "getSite.php", false);
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhr.send(markup);
                alert(xhr.responseText);
                $("#result").text(xhr.responseText);
                return xhr.responseText;
            } else {
                param = "Masukan URL"
                alert(param)
            }

        })
    })
    </script>

</head>

<body>
    <!-- Page Content -->
    <div class="container">
        <div class="card border-0 shadow my-5">
            <div class="card-body p-5">
                <div class="jumbotron text-center">
                    <div class="main_body">
                        <br><br>
                        <h1>Keamanan Sistem Lanjutan</h1>
                        <h4>Cek Phishing Website</h4>
                        <br><br><br><br>
                        <form>
                            <center>
                                <div class="form-group w-50">
                                    <label for="website">
                                        <h6>Masukkan Link Website untuk Diperiksa</h6>
                                    </label><br><br>
                                    <input name="website" type="text" class="form-control" id="check" placeholder="">
                                </div><br><br>
                                <button type="button" name="button" class="btn btn-secondary">Priksa</button>

                            </center>
                        </form>
                        <br><br><br>
                        <div id="url_"></div>
                        <br><br><br><br><br>
                        <div id="result"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous">
    </script>


</body>

</html>
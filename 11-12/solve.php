<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $second){
    $key = $second;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for ($i = 0; $i < strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$old_cookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D';

$old_cookie_base64_decode = base64_decode($old_cookie);

$censored_key = xor_encrypt(json_encode($defaultdata),$old_cookie_base64_decode);

echo "the key used for the cookie is : $censored_key \n";
// since the length of key and our elements are different the xor function repeat the key we should manually collect the repeated part
// and put it as our key
$censored_key = 'KNHL';
echo "the repeated sequence i collect manually is $censored_key \n";
// echo $censored_key;
$new_data = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));

$new_cookie = base64_encode(xor_encrypt($new_data, $censored_key));


echo "value of new cookie contains showpassword=yes : $new_cookie \n";

?>

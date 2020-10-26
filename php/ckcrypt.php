<?php

// ckcrypt => crytps and encodes in base64 a given string
// ckdecrypt => decrypt a base64 encoded string

function ckcrypt($mprhase) {
    $td = mcrypt_module_open('tripledes', '', 'ecb', '');
    $iv = mcrypt_create_iv(mcrypt_enc_get_iv_size($td), MCRYPT_RAND);
    mcrypt_generic_init($td, MASTERKEY, $iv);
    $crypted_value = mcrypt_generic($td, $mprhase);
    mcrypt_generic_deinit($td);
    mcrypt_module_close($td);

    return base64_encode($crypted_value);
}

function ckdecrypt($mprhase) {
    $td = mcrypt_module_open('tripledes', '', 'ecb', '');
    $iv = mcrypt_create_iv(mcrypt_enc_get_iv_size($td), MCRYPT_RAND);
    mcrypt_generic_init($td, MASTERKEY, $iv);

    $decrypted_value = mdecrypt_generic($td, base64_decode($mprhase));
    mcrypt_generic_deinit($td);
    mcrypt_module_close($td);

    return $decrypted_value;
}
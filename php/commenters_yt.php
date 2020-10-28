<?php
// Carlo Perassi, 2012: snippet
// Simple snippet to get the YouTube pages of the commenters of a video

$youtube = new stdClass();
$youtube->base = 'https://gdata.youtube.com/feeds/api/videos/';
$youtube->user = 'https://gdata.youtube.com/feeds/api/users/';
$youtube->id = $_GET['id']; // ID of the video, just for testing

// FIXME @s
if ($stream_base = fopen($youtube->base . $youtube->id . '/comments', 'r')) {
    $xml_base = new SimpleXMLElement(@stream_get_contents($stream_base));

    echo "<ul>\n";
    foreach ($xml_base->entry as $entry) {
         list($before, $after) = explode("https://", $entry->author->uri);
         $mtoken = explode("/", $after);
         if ($stream_user = fopen($youtube->user . $mtoken[4], 'r')) {
             $xml_user = new SimpleXMLElement(@stream_get_contents($stream_user));
             foreach ($xml_user->link as $link) {
                 if ($link['rel'] == 'alternate') {
                     echo '<li><a href="' . $link['href'] . '">' . $link['href'] . "</a></li>\n";
                 }
             }
         }
    } 
    echo "</ul>\n";

    fclose($stream_base);
}

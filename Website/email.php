<?php
  $name = $_POST['name'];
  $visitor_email = $_POST['email'];
  $message = $_POST['message'];
  $mobile = $_POST['phone'];
  $to = "donavan.d.gertsch@gmail.com";
  body = "";
  $body .= "From: ".$name. "\r\n"
  $body .= "Email: ".visitor_email. "\r\n"
  $body .= "Message: ".message. "\r\n"
  $body .= "Number: ".mobile. "\r\n"
  mail($to,$message,$body);
?>
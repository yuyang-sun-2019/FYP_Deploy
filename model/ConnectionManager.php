

<!-- <//?php

class ConnectionManager { -->

    <!-- // public function getConnection() {
    //     $servername = 'us-cdbr-east-06.cleardb.com';
    //     $username = 'b805ab9b5bfcbd';
    //     $password = '2b244a70';
    //     $dbname = 'heroku_496d18e9fc14ec0';
    //     // mysql://b805ab9b5bfcbd:2b244a70@us-cdbr-east-06.cleardb.net/heroku_496d18e9fc14ec0?reconnect=true

    //     //return new PDO($dsn, "root", "");  
        
    //     // Create connection
    //     $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);    

    //     $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // if fail, exception will be thrown

    //     // Return connection object
    //     return $conn; -->
<?php
    // $url = parse_url(getenv("mysql://b805ab9b5bfcbd:2b244a70@us-cdbr-east-06.cleardb.net/heroku_496d18e9fc14ec0?reconnect=true"));
    
    $server = "us-cdbr-east-06.cleardb.com";
    $username = "b805ab9b5bfcbd";
    $password = "2b244a70";
    $db = "heroku_496d18e9fc14ec0";
    
    $conn = new mysqli($server, $username, $password, $db);
    ?>
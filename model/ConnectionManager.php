
<?php

class ConnectionManager {

    public function getConnection() {
        $servername = 'us-cdbr-east-06.cleardb.com';
        $username = 'b805ab9b5bfcbd';
        $password = '2b244a70';
        $dbname = 'heroku_496d18e9fc14ec0db';
        // mysql://be45f732c7bf49:3489eb7c@us-cdbr-east-04.cleardb.com/heroku_e51b0bda5f650db?reconnect=true
        //$dsn  = "mysql:host=localhost;dbname=week12";
        //return new PDO($dsn, "root", "");  
        
        // Create connection
        $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);

        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // if fail, exception will be thrown

        // Return connection object
        return $conn;
    }

}

?>


 <?php

class ConnectionManager {

    public function getConnection() {
        $servername = 'us-cdbr-east-06.cleardb.net';
        $username = 'b70ed68d8e3e96';
        $password = '0c9da54c';
        $dbname = 'heroku_55f1bdb2075fced';
        //mysql://b70ed68d8e3e96:0c9da54c@us-cdbr-east-06.cleardb.net/heroku_55f1bdb2075fced?reconnect=true


        //return new PDO($dsn, "root", "");  
        
        // Create connection
        $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);    

        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // if fail, exception will be thrown

        // Return connection object
        return $conn; 
    }
}
    ?>
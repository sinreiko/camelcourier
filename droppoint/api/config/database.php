<?php

class Database {

    // specify your own database credentials
    // private $host = getenv('MYSQL_DBHOST')? getenv('MYSQL_DBHOST') :"host.docker.internal";
    // private $db_name =getenv('MYSQL_DBNAME')? getenv('MYSQL_DBNAME'):"camelDB";
    // private $username =getenv('MYSQL_DBUSER')? getenv('MYSQL_DBUSER'):"is213";
    // private $password =getenv('MYSQL_DBPASS')? getenv('MYSQL_DBPASS'):""; // MAMP "root", WAMP empty string
    // private $port = getenv('MYSQL_DBPORT')? getenv('MYSQL_DBPORT'):3306; // Check in PHPMyAdmin for port number
    private $host = "host.docker.internal";
    private $db_name ="camelDB";
    private $username ="is213";
    private $password =""; // MAMP "root", WAMP empty string
    private $port =3306; // Check in PHPMyAdmin for port number
    public $conn;

    // get the database connection
    public function getConnection() {

        $this->conn = null;

        try {
            $this->conn = new PDO(
                "mysql:host=" . $this->host . ";dbname=" . $this->db_name . ";port=" . $this->port, 
                $this->username, $this->password);

            $this->conn->exec("set names utf8");
        }
        catch(PDOException $exception) {
            echo "Connection error: " . $exception->getMessage();
        }
        // echo "\n".'=====this is $this->conn'."\n";
        // var_dump($this->conn);
        return $this->conn;
    }
}

?>
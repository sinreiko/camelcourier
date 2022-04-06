<?php
    class Post {
    
        // database connection and table name
        private $conn;
        private $table_name = "droppoint";
   
        // object properties
        public $address;
        public $placeID;
    
        // constructor with $db as database connection
        public function __construct($db) {
            $this->conn = $db;
            // echo "\n=========db is constructed yo\n";
        }

        // read all
        public function read() {
        
            // select all query
            $query = "SELECT * FROM droppoint;";
        
            // prepare query statement
            $stmt = $this->conn->prepare($query);
        
            // execute query
            $stmt->execute();
            // echo "\n==========im reading all them entries boi\n";
            return $stmt;
        }

        // read one item
        public function get_region($region) {
        
            // query to read single record
            $query = "SELECT
                            *
                        FROM
                            droppoint
                        WHERE
                            region = ?";
        
            // prepare query statement
            $stmt = $this->conn->prepare( $query );
        
            // bind id of product to be updated
            $stmt->bindParam(1, $region);
        
            // execute query
            $stmt->execute();
        
            return $stmt;
        }
    }
?>
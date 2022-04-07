<?php
// required headers
header("Access-Control-Allow-Origin: *");
header("Access-Control-Expose-Headers: X-JSON");
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header("Access-Control-Allow-Headers: *");
header("Content-Type: application/json; charset=UTF-8");
header("HTTP/1.1 200 OK");
if ($method == "OPTIONS") {
    header('Access-Control-Allow-Origin: *');
    header("Access-Control-Allow-Headers: X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method,Access-Control-Request-Headers, Authorization");
    header("HTTP/1.1 200 OK");
    die();
}
// include database and object files
include_once 'api/config/database.php';
// echo "\nI just read database.php";
include_once 'api/objects/Post.php';
// echo "\nI just read Post.php";

// get database connection
$database = new Database();
$db = $database->getConnection();

// prepare droppoint object
$droppt = new Post($db);

// products array
$result_arr = array();
$result_arr["data"] = array();
$result_arr["code"] = 500;
// set region property of record to read
// $droppt->region = isset($_GET['region']) ? $_GET['region'] : die();
// //=========mysqli version
// $host=getenv('MYSQL_DBHOST')? getenv('MYSQL_DBHOST'): 'localhost';
// $db_port=getenv('MYSQL_DBPORT')? getenv('MYSQL_DBPORT'): 3306;
// $conn = new mysqli($host, "root", "root", "camelDB",$db_port);
// // Check connection
// if ($conn->connect_error) {
//     die("Connection failed: " . $conn->connect_error);
// } else {
//     echo "Connected to MySQL server successfully!";
// }
// // $database = new Database();
// // $db = $database->getConnection();
// $sql = "SELECT * FROM droppoint";
// $result = $conn->query($sql);
// $result_arr=array();
// $result_arr["data"]=array();
// $item=array();

// if ($result->num_rows > 0) {

//     // output data of each row
//     while($row = $result->fetch_assoc()) {
//         extract($row);
//         $item=[
//             "latitude"=> $row['latitude'],
//             "longitude"=> $row['longitude'],
//             "region"=> $row['region']
//         ];
//         array_push($result_arr["data"], $item);
//     }
//     // set response code - 200 OK
//     http_response_code(200);
//     // make it json format
//     echo json_encode($result_arr);
// } else {
//     // set response code - 404 Not found
//     http_response_code(404);

//     // tell the user item does not exist
//     echo json_encode(array("message" => "Item does not exist."));

// }


//=========
// read the details of product to be edited
$stmt = $droppt->read();
$num = $stmt->rowCount();
if ($num > 0) {
    // code...
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        extract($row);
        // products array        
        $item = array(
            "address" => $address,
            "placeID" => $placeID
        );
        //add item to the result array
        array_push($result_arr["data"], $item);
    }

    // set response code - 200 OK
    $result_arr['code'] = 200;
    http_response_code(200);

    // make it json format
    echo json_encode($result_arr);
} else {

    // set response code - 404 Not found
    http_response_code(404);

    // tell the user item does not exist
    echo json_encode(array("message" => "Item does not exist."));
}

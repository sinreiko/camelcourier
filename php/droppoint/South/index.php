<?php
// required headers
header("Access-Control-Allow-Origin: *");
header("Access-Control-Expose-Headers: Content-Length, X-JSON");
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header("Access-Control-Allow-Headers: *");
header("Content-Type: application/json; charset=UTF-8");

  
// include database and object files
include_once '../api/config/database.php';
// echo "\nI just read database.php";
include_once '../api/objects/Post.php';
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
  
// read the details of product to be edited
$stmt=$droppt->get_region("South");
$num=$stmt->rowCount();
if ($num>0) {
    // code...
    while( $row = $stmt->fetch(PDO::FETCH_ASSOC) ){
        extract($row);
        // products array        
        $item = array(
                "latitude" => $latitude,
                "longitude" => $longitude,
                "region" => $region,
                "placeID" => $placeID
            );
        //add item to the result array
        array_push($result_arr["data"], $item);

    }
      
    // set response code - 200 OK
    $result_arr['code']=200;
    http_response_code(200);
      
    // make it json format
    echo json_encode($result_arr);
    } else {

    // set response code - 404 Not found
    http_response_code(404);
  
    // tell the user item does not exist
    echo json_encode(array("message" => "Item does not exist."));
}

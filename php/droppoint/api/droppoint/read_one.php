<?php
// required headers
header("Access-Control-Allow-Origin: *");
header("Access-Control-Expose-Headers: Content-Length, X-JSON");
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header("Access-Control-Allow-Headers: *");
header("Content-Type: application/json; charset=UTF-8");

  
// include database and object files
include_once '../config/database.php';
include_once '../objects/Post.php';
  
// get database connection
$database = new Database();
$db = $database->getConnection();
  
// prepare product object
$match = new Post($db);
  
// set ID property of record to read
$match->id = isset($_GET['region']) ? $_GET['id'] : die();
  
// read the details of product to be edited
$match->readOne();
  
if($match->fullname != null) {
    // create array
    $item = array(
        "latitude" => $latitude,
        "longitude" => $longitude,
        "region" => $region
    );
  
    // set response code - 200 OK
    http_response_code(200);
  
    // make it json format
    echo json_encode($item);
}
else {
    // set response code - 404 Not found
    http_response_code(404);
  
    // tell the user item does not exist
    echo json_encode(array("message" => "Item does not exist."));
}
?>
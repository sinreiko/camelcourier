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

// instantiate database and product object
$database = new Database();
$db = $database->getConnection();

// initialize object
$match = new Post($db);

// get search query
if( isset($_GET["author"]) && isset($_GET["category"]) && isset($_GET["comment"])
    && trim($_GET["author"]) != ''
    && trim($_GET["category"]) != ''
    && trim($_GET["comment"]) != '' ) {
    
    // var_dump($_POST["author"], $_POST["category"], $_POST["comment"]);
    $stmt = $match->write($_GET["author"], $_GET["category"], $_GET["comment"]);

    // set response code - 200 OK
    http_response_code(200);
  
    // tell the user status is OK
    echo json_encode(
        array("message" => "Comment has been successfully posted.")
    );
    exit;
}
else {
    // set response code - 404 Not found
    http_response_code(404);
  
    // tell the user no items found
    echo json_encode(
        array("message" => "Query parameters are not set.")
    );
    exit;
}
?>
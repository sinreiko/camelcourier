const get_order_URL = "http://localhost:8000/api/order"
const get_activity_URL = "http://localhost:8000/api/activity"
const get_shipper_URL = "http://localhost:8000/api/shipper"
// const get_droppoint_URL = "http://localhost:5004/droppoint/"
const get_droppoint_URL = "http://localhost:8000/api/droppoint/"

const valuing_URL = "http://localhost:8000/api/valuing"
const pick_parcel_URL = "http://localhost:8000/api/pickparcel"
const create_order_URL = "http://localhost:8000/api/create_order"
const update_order_URL = "http://localhost:8000/update_order/update"
const cancel_order_URL = "http://localhost:8000/api"

// const get_order_URL = "http://localhost:5000/order"
// const get_activity_URL = "http://localhost:5001/activity"
// const get_shipper_URL = "http://localhost:5002/shipper"
// const get_droppoint_URL = "http://localhost:5004/droppoint/"
// const valuing_URL = "http://localhost:5005/valuing"
// const pick_parcel_URL = "http://localhost:5006/pick_parcel"
// const create_order_URL = "http://localhost:5007/create_order"
// const update_order_URL = "http://localhost:5008/update_order/update"
// const cancel_order_URL = "http://localhost:5009/"
// GraphQL: exchange rate
let SWOP_API_key='7b31aa8dabd1df60435aec0cbff8f9d17211d33f6b2f20dfe7e7a85bb539689e'
let SWOP_URL=`https://swop.cx/graphql?api-key=${SWOP_API_key}`


const app = Vue.createApp({
    data(){
        return {
            userName: localStorage.getItem("userName"),
            userType: localStorage.getItem("userType"),
            trackingResult: {
                tracking_id: '',
                latest_status: '',
                latest_timestamp: '',
                progress: '',
                activities: [],
                orderListIndex: 0
            },
            userDetail: JSON.parse(localStorage.getItem("userDetail")),
            dropPoints:[
                {
                    address: "",
                    placeID: "",
                }
            ],
            mapLink: "",
            orderCreation:{
                //shipper
                shipperPostal: "",
                shipperAddress: "",
                shipperUnit:"",
                shipperName: "",
                shipperEmail: "",
                shipperPhone: "",
                //receiver
                receiverAddress: "",
                receiverUnit: "",
                receiverPostal: "",
                receiverName: "",
                receiverEmail: "",
                receiverPhone: "",
                //others
                dropOffOption: "custom", //custom or dropPoint
                size: "",
                price: "3.00",
                pickupAddress:"",
                pickupPostal: ""
            },
            inputTracking: "",
            orderList:[],
            customOrderList:[],
            fetchResults:{
                orderCreation: false,
                orderUpdate: false,
                getPrice: false,
            },
            message: "",
            // these are variables for the graphQL currency app
            currency:"SGD",
            currency_obj:{
                SGD:1,
                EUR:0.67,
                USD:0.74,
                CNY:4.68
            }
        };
    },
    methods: {
        showGraphQLData(){
            const query=`
                query Latest {
                    latest(baseCurrency: "SGD", quoteCurrencies: ["USD", "EUR", "CNY"]) {
                    date
                    baseCurrency
                    quoteCurrency
                    quote
                    }
                }
            `;

            fetch(SWOP_URL,{
                method:"POST",
                headers: {
                    "Content-Type":"application/json",
                    "Accept":"application.json",
                    "Access-Control-Allow-Origin": "*"
                },
                body: JSON.stringify({
                    query           
                })
            }).then(response=>response.json()
                // resp = JSON.parse(response)
            ).then(
                data=>{
                    let resp=data.data.latest
                    // console.log(resp)
                    for(ans of resp){
                        // console.log(ans)
                        this.currency_obj[ans.quoteCurrency]=ans.quote
                        // console.log(`updating ${ans.quoteCurrency}`)
                    }
                }
            )
            .catch(
                error=>{console.log(error)}
            )
        },

        calculateProgress(status){
            if (status == 'Order created'){
                return 10
            } else if (status == 'Pickup' || status == 'Delayed'){
                return 50
            } else if (status == 'Completed'){
                return 100
            }
        },
        trackParcel(tracking, index=0){
            // var tracking_arr = []
            // if (this.inputTracking != ""){
            //     if (this.inputTracking.includes(",")){
            //         tracking_arr = this.inputTracking.split(",")
            //     } else if (this.inputTracking.includes(" ")){
            //         tracking_arr = this.inputTracking.split(" ")
            //     } else {
            //         tracking_arr.push(this.inputTracking);
            //     }
            var real_tracking = ''
            if (this.inputTracking == ''){
                real_tracking = tracking
            } else {
                real_tracking = this.inputTracking
            }
            const response =
            fetch(`${get_activity_URL}/${real_tracking}`)
            .then(response => response.json())
            .then(data => {
                if (data.code === 404) {
                    // no book in db
                    this.message = data.message;
                    alert(this.message)
                } else {
                    res = data.data;
                    latestStatus = res[res.length - 1].delivery_status;
                    latestTimestamp = res[res.length - 1].timestamp;
                    this.trackingResult = {
                        tracking_id: real_tracking,
                        latest_status: latestStatus,
                        latest_timestamp: latestTimestamp,
                        progress: this.calculateProgress(latestStatus),
                        activities: res,
                        orderListIndex: index
                    };
                    this.trackingResult.activities.reverse();
                }
            })
            .catch(error => {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                // console.log(this.message + error);

            });
            // } else {
            //     alert("Please insert a tracking number.")
            // }
            
        },
        updateUser(e){
            this.userDetail = e
        }, 
        verificationForm(){
            var current_fs, next_fs, previous_fs; //fieldsets
            var left, opacity, scale; //fieldset properties which we will animate
            var animating; //flag to prevent quick multi-click glitches

            $(".next").click(function () {
                if (animating) return false;
                animating = true;

                current_fs = $(this).parent();
                next_fs = $(this).parent().next();

                //activate next step on progressbar using the index of next_fs
                $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

                //show the next fieldset
                next_fs.show();
                //hide the current fieldset with style
                current_fs.animate({
                    opacity: 0
                }, {
                    step: function (now, mx) {
                        //as the opacity of current_fs reduces to 0 - stored in "now"
                        //1. scale current_fs down to 80%
                        scale = 1 - (1 - now) * 0.2;
                        //2. bring next_fs from the right(50%)
                        left = (now * 50) + "%";
                        //3. increase opacity of next_fs to 1 as it moves in
                        opacity = 1 - now;
                        current_fs.css({
                            'transform': 'scale(' + scale + ')',
                            'position': 'absolute'
                        });
                        next_fs.css({
                            'left': left,
                            'opacity': opacity
                        });
                    },
                    duration: 800,
                    complete: function () {
                        current_fs.hide();
                        animating = false;
                    },
                    //this comes from the custom easing plugin
                    easing: 'easeInOutBack'
                });
            });

            $(".previous").click(function () {
                if (animating) return false;
                animating = true;

                current_fs = $(this).parent();
                previous_fs = $(this).parent().prev();

                //de-activate current step on progressbar
                $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

                //show the previous fieldset
                previous_fs.show();
                //hide the current fieldset with style
                current_fs.animate({
                    opacity: 0
                }, {
                    step: function (now, mx) {
                        //as the opacity of current_fs reduces to 0 - stored in "now"
                        //1. scale previous_fs from 80% to 100%
                        scale = 0.8 + (1 - now) * 0.2;
                        //2. take current_fs to the right(50%) - from 0%
                        left = ((1 - now) * 50) + "%";
                        //3. increase opacity of previous_fs to 1 as it moves in
                        opacity = 1 - now;
                        current_fs.css({
                            'left': left
                        });
                        previous_fs.css({
                            'transform': 'scale(' + scale + ')',
                            'opacity': opacity
                        });
                    },
                    duration: 800,
                    complete: function () {
                        current_fs.hide();
                        animating = false;
                    },
                    //this comes from the custom easing plugin
                    easing: 'easeInOutBack'
                });
            });

            $(".submit").click(function () {
                this.createOrder();
                return false;
            })
        },
        getDropPoints(){
            const response =
                fetch(`${get_droppoint_URL}`,{
                    headers:{
                        "Access-Control-Allow-Origin": "*"
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        // no book in db
                        this.message = data.message;
                    } else {
                        res = data.data
                        this.dropPoints = res;
                        console.log(this.dropPoints);
                        $('.slider_form').addClass('col-md-6')
                        $('.slider_form').animate({
                            margin: 0
                        },1000, function(){
                            
                        })
                        this.changeDropPoint();
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    // console.log(this.message + error);

                });
        },
        changeDropPoint(){
            var map = new google.maps.Map(document.getElementById('map'), {
                center: new google.maps.LatLng(0, 0),
                zoom: 15
            });
        
            var service = new google.maps.places.PlacesService(map);
            let dropOffAddress = this.orderCreation.dropOffAddress
            let placeID = dropOffAddress.split("|")[0]
            this.orderCreation.pickupAddress = dropOffAddress.split("|")[1]
            console.log(dropOffAddress)
            service.getDetails({
                placeId: placeID
            }, function (place, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
        
                    // Create marker
                    var marker = new google.maps.Marker({
                        map: map,
                        position: place.geometry.location
                    });
                    // Center map on place location
                    map.setCenter(place.geometry.location);
                }
            });
        },
        resetDropPoint(){
            $('.slider_form').removeClass('col-md-6')
        },
        getPickUpAddress(){
            this.orderCreation.pickupPostal = this.pickupPostal;
            this.orderCreation.pickupAddress = this.pickupAddress;
            this.orderCreation.shipperName = this.userName;
            this.orderCreation.shipperEmail = this.userDetail.shipperEmail;
            this.orderCreation.shipperPhone = this.userDetail.shipperPhone;
            // console.log(JSON.stringify(this.orderCreation));
        },
        getReceiverAddress(dropoff){
            this.orderCreation.receiverPostal = dropoff.receiverPostal;
            this.orderCreation.receiverAddress = dropoff.receiverAddress;
            // console.log(JSON.stringify(this.orderCreation));

        },
        getPrice(){
            let jsonData = JSON.stringify({
                pickupAddress: this.orderCreation.pickupAddress,
                receiverAddress: this.orderCreation.receiverAddress,
                size: this.orderCreation.size
            });
            console.log(jsonData);
            fetch(`${valuing_URL}`,
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                body: jsonData
            })
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result)
                    this.orderCreation.price = result.price;
                    switch (data.code) {
                        case 400:
                        case 500:
                            this.errorMessages.getPrice = data.message;
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    console.log(this.message + error);

                });
        },
        createOrder(){
            this.fetchResults.orderCreation = false;
            this.messages = "";

            let jsonData = JSON.stringify({
                shipperID: this.userDetail.shipperID, //shipperID
                receiverName: this.orderCreation.receiverName,
                receiverAddress: this.orderCreation.receiverUnit + " " + this.orderCreation.receiverAddress + " " + this.orderCreation.receiverPostal,
                receiverPhone: "+65" + this.orderCreation.receiverPhone,
                receiverEmail: this.orderCreation.receiverEmail,
                pickupAddress: this.orderCreation.pickupAddress
            });
            alert(jsonData);
            fetch(`${create_order_URL}`,
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                body: jsonData
            })
            .then(response => response.json())
            .then(data => {
                result = data.data;
                
                // 3 cases
                switch (data.code) {
                    case 201:
                        this.fetchResults.orderCreation = true;
                        alert("Order has been created.");
                        if(this.orderCreation.dropOffOption == 'dropPoint'){
                            this.pickupParcel(result.shipperID,result.trackingID,this.orderCreation.pickupAddress)
                        } else { 
                            window.location.href = "order-history.html"
                        }
                        break;
                    case 400:
                    case 500:
                        this.message = data.message;
                        console.log(this.message)
                        break;
                    default:
                        console.log(data.message);
                        throw `${data.code}: ${data.message}`;
                }
            })
        },
        retrieveOrderByUserId(user, userid){
            fetch(`${get_order_URL}/find/${user}/${userid}`)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        // no book in db
                        this.message = data.message;
                        console.log('====bruh got no data sia=====')
                    } else {
                        orders = data.data.orders;
                        console.log('====got orders==')
                        console.log(orders);
                        for (var i = 0; i < orders.length; i++){
                            this.orderList.push({
                                trackingID: orders[i].trackingID,
                                driverID: orders[i].driverID,
                                pickupAddress: orders[i].pickupAddress,
                                receiverAddress: orders[i].receiverAddress,
                                receiverEmail: orders[i].receiverEmail,
                                receiverName: orders[i].receiverName,
                                receiverPhone: orders[i].receiverPhone,
                                shipperID: orders[i].shipperID,
                                shipperAddress: '',
                                latestStatus: '',
                                latestTimestamp: ''
                            })
                            this.retrieveShipper(orders[i].shipperID, orders[i].trackingID)
                            this.getDeliveryStatusByTrackingID(orders[i].trackingID)
                        };
                        console.log(this.orderList);
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    // console.log(this.message + error);

                });
        },
        getDeliveryStatusByTrackingID(trackingid){
            fetch(`${get_activity_URL}/${trackingid}`)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        // no book in db
                        this.deliveryStatus = data.message;
                    } else {
                        res = data.data;
                        latestStatus = res[res.length - 1].delivery_status;
                        latestTimestamp = res[res.length - 1].timestamp;
                        for (var i = 0; i < this.orderList.length; i++){
                            if (this.orderList[i].trackingID == trackingid){
                                this.orderList[i].latestStatus = latestStatus;
                                this.orderList[i].latestTimestamp = latestTimestamp
                                break;
                            }
                        }
                        
                            
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    console.log(this.message + error);

                });
        }
        ,
        retrieveShipper(shipperid, trackingid){
            fetch(`${get_shipper_URL}/${shipperid}`)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        // no book in db
                        this.message = data.message;
                    } else {
                        res = data.data;
                        for (var i = 0; i < this.orderList.length; i++){
                            if (this.orderList[i].trackingID == trackingid){
                                this.orderList[i].shipperAddress = res.shipperAddress;
                                this.orderList[i].shipperName = res.shipperName;
                                this.orderList[i].shipperEmail = res.shipperEmail;
                                this.orderList[i].shipperPhone = res.shipperPhone;
                                this.orderCreation.shipperAddress=res.shipperAddress;
                                this.orderCreation.shipperEmail=res.shipperEmail;
                                this.orderCreation.shipperPhone=res.shipperPhone;
                                this.orderCreation.shipperName=res.shipperName;
                                break;
                            }
                        }
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    // console.log(this.message + error);
                })
            // return shipperAddress
        },
        updateOrder(status,trackingid){

            let jsonData = JSON.stringify({
                trackingID: JSON.stringify(trackingid)
            });
            if (status!='cancel_order'){
                fetch(`${update_order_URL}/${status}`,
                {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    },
                    body: jsonData
                })
                .then(response => response.json())
                .then(data => {
                    alert('Order has been updated.');
                    result = data.data;
                    // 3 cases
                    switch (data.code) {
                        case 201:
                            this.fetchResults.orderUpdate = true;
                            break;
                        case 400:
                        case 500:
                            this.errorMessages.orderUpdate = data.message;
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
            } else {
                fetch(`${cancel_order_URL}/${status}`,
                {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    },
                    body: jsonData
                })
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    alert('Order has been cancelled');
                    window.location.href = 'order-history.html'
                    // 3 cases
                    switch (data.code) {
                        case 201:
                            this.fetchResults.orderUpdate = true;
                            break;
                        case 400:
                        case 500:
                            this.errorMessages.orderUpdate = data.message;
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
            }
            
        },
        customOrder(status){
            this.customOrderList = []
            for (var i = 0; i < this.orderList.length; i++){
                console.log(this.orderList[i].latestStatus, status)
                if(this.orderList[i].latestStatus == status){
                    this.customOrderList.push(this.orderList[i])
                }
            }
            console.log(this.customOrderList);
        },
        style(k){
            switch (k) {
                case 'Order created':
                    return {
                        color: 'black'
                    }
                case 'Pickup':
                    return {
                        color: 'blue'
                    }
                case 'Cancelled':
                    return{
                        color: 'red'
                    }
                case 'Canceled':
                    return{
                        color: 'red'
                }
                case 'Delayed':
                    return {
                        color: 'orange'
                    }
                case 'Completed':
                    return {
                        color: 'green'
                    }
                
            }
        },
        pickupParcel(shipperid,trackingid,pickup){
            let jsonData = JSON.stringify({
                shipperID: shipperid, //shipperID
                trackingID: trackingid,
                pickupAddress: pickup,
            });
            fetch(`${pick_parcel_URL}`,
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json"
                },
                body: jsonData
            })
            .then(response => response.json())
            .then(data => {
                
                // 3 cases
                switch (data.code) {
                    case 201:
                        alert("Order is awaiting pickup.");
                        window.location.href = "order-history.html"
                        break;
                    case 400:
                    case 500:
                        this.message = data.message;
                        console.log(this.message)
                        break;
                    default:
                        console.log(data.message);
                        throw `${data.code}: ${data.message}`;
                }
            })
        }
    },
    beforeMount(){
        if (this.userType == 'driver'){
            this.retrieveOrderByUserId('driver',this.userDetail.driverID);
        } else if (this.userType == 'shipper'){
            this.retrieveOrderByUserId('shipper', this.userDetail.shipperID)
        }
    },
    mounted(){
        console.log(this.userDetail)
        this.verificationForm();
        
        
    }
})
app.component('home-header',{
    props:['userdetail'],
    template:
    `<header class="header_section">
        <div class="container-fluid">
            <!-- <div class="row"> -->
                <nav class="navbar navbar-expand-lg custom_nav-container">
                    <!-- <div class="col-auto"> -->

                        <a class="navbar-brand" href="index.html">
                            <span>
                                CAMELCOURIER
                            </span>
                        </a>
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                    <a class="nav-link" href="index.html"> Home</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="track-order.html"> Track your parcel</a>
                                </li>
                            </ul>
                        </div>
                    <!-- </div> -->            
                    <div class=" mr-lg-5 pt-3">
                        <form id="form-login" class="form-inline" action="" method="post">
                            <div class="form-group w-40">
                                <label for="email" class="sr-only">Email address</label>
                                <input v-model="userEmail" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
                            </div>
                            <div class="form-group w-40">
                                <label for="password" class="sr-only">Password</label>
                                <input v-model="userPassword" type="password" class="form-control" id="password" aria-describedby="emailHelp" placeholder="Enter password">
                            </div>
                            <div class="form-group w-20 mt-md-2">
                                <button @click.prevent="userAuthenticate('form-login')" type="submit" class="action-button btn btn-primary mb-2 w-100" style="padding:0">Login</button>
                            </div>
                        </form>
                    </div>             
            </nav>
            </div>
    </header>`
    ,
    data(){
        return{
            driverLogin:{
                name: "Jun Hui 💩",
                email: "driver@driver.com",
                password: "driver123",
                type: "driver"
            },
            shipperLogin: [],
            shipperPass: "shipper123",
            userEmail: "",
            userPassword: "",
            userType: "",
        }
    },
    
    computed:{
        getShipper(){
            const response =
                fetch(`${get_shipper_URL}`)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        this.message = data.message;
                    } else {
                        res = data.data.shippers;
                        for (let i = 0; i < res.length; i++) {
                            this.shipperLogin.push(res[i])
                        }
                        console.log('-----this is the shipper obj retrieved-----')
                    }
                })
        },
        getDriver(){

        }
    },
    methods:{
        userAuthenticate (formType) {
            if (this.userEmail != "" || this.userPassword != ""){
                if (this.userPassword == this.driverLogin.password){
                    let userDetail = {'driverID':this.userEmail}
                    localStorage.setItem("userDetail", JSON.stringify(userDetail))
                    localStorage.setItem("userName", this.userEmail)
                    localStorage.setItem("userType", "driver");
                    form = document.getElementById(formType)
                    form.action = "pickup.html"
                    form.submit()
                } else if (this.shipperLogin.some(e => e.shipperEmail === this.userEmail) && this.userPassword == this.shipperPass){
                    shipperObj = this.shipperLogin.find(e => e.shipperEmail === this.userEmail);
                    this.$emit('update-user', shipperObj)
                    localStorage.setItem("userDetail", JSON.stringify(shipperObj))
                    localStorage.setItem("userName", shipperObj.shipperName);
                    localStorage.setItem("userType", "shipper");
                    form = document.getElementById(formType)
                    form.action = "create-delivery.html"
                    form.submit()
                } else {
                    alert("Email and/or password is incorrect. Please try again.")
                }
            } else {
                alert("Email and/or password is empty. Please fill in.")
            }
        },
    },
    
    beforeMount(){
        this.getShipper;
    },
})

app.component('driver-header',{
    data(){
        return{

        }
    }, 
    methods: {
    },
    props: ['username'],
    template: `
    <header class="header_section">
        <div class="container-fluid">
            <nav class="navbar navbar-expand-lg custom_nav-container">
                
                <a class="navbar-brand" href="index.html">
                    <span>CAMELCOURIER</span>
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="index.html"> Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="pickup.html">Pickup</a>
                        </li>
                        <li class="nav-item ">
                            <a class="nav-link" href="delivery-history.html" v-on:click="customOrder('Pickup')">Delivery History</a>
                        </li>
                    </ul>
                </div>
                <span class="navbar-text my-1 mx-2">
                    Welcome, {{username}}
                </span>
            </nav>
        </div>
    </header>`
});

app.component('shipper-header',{
    data(){
        return{

        }
    }, 
    methods: {

    },
    props: ['username'],
    // template: `<div>{{}}</div>`
    template: `
    <header class="header_section">
        <div class="container-fluid">
            <nav class="navbar navbar-expand-lg custom_nav-container">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <a class="navbar-brand" href="index.html">
                    <span>CAMELCOURIER</span>
                </a>
                <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="index.html"> Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="create-delivery.html">Create Delivery</a>
                        </li>
                        <li class="nav-item active">
                            <a class="nav-link" href="order-history.html">Order History</a>
                        </li>
                    </ul>
                </div>
                <span class="navbar-text my-1 mx-2">
                    Welcome, <a href="user_details.html">{{username}}</a>
                </span>
            </nav>
        </div>
    </header>`
});

app.component('activity', {
    props: ['trackingid','deliverydesc','timestamp','deliverystatus'],
    template:`
        <li>
            <dl>
                <dd>{{deliverydesc}}</dd>
                <dd class="text-secondary">{{timestamp}} · {{deliverystatus}}</dd>
            </dl>
        </li>
    `
})

app.component('custom-select',{
    props:['droppoint']
    ,
    template:`
    <select class="form-select" name="dropOffPoints">
        <option v-for="dp in droppoint" :value="dp.region" v-model="orderCreation.receiverAddress">{{dp.region}}</option>
    </select>
    `
})
app.component('order-info',{
    props:['order'],
    template:`
    `
})

const vm = app.mount('#app'); 

var options = {
    // fields: ["formatted_address", 'geometry', 'name'],
    componentRestrictions: { country: "sg" }
}
var placeSearch, autocomplete, shipper_autocomplete, receiver_autocomplete;


function initAutocomplete() {
// Create the autocomplete object, restricting the search to geographical
// location types.
    var shipper_autocomplete = new google.maps.places.Autocomplete((document.getElementById('shipperPostal')), options);
    var receiver_autocomplete = new google.maps.places.Autocomplete((document.getElementById('receiverPostal')), options);

    shipper_autocomplete.addListener('place_changed', function() {
        var place = shipper_autocomplete.getPlace();

        var pickupAdd= {
            pickupPostal: "",
            pickupAddress: ""
        }
        for (var i = 0; i < place.address_components.length; i++) {
            var addressType = place.address_components[i].types[0];
            if (addressType == 'postal_code'){
                pickupAdd.pickupPostal = place.address_components[i]['long_name'];
            }
        }
        pickupAdd.pickupAddress = place.formatted_address;
        vm.getPickUpAddress();        
    });
    receiver_autocomplete.addListener('place_changed', function() {
        var place = receiver_autocomplete.getPlace();
        var receiverAddress = {
            receiverPostal: "",
            receiverAddress: ""
        }
        for (var i = 0; i < place.address_components.length; i++) {
            var addressType = place.address_components[i].types[0];
            if (addressType == 'postal_code'){
                receiverAddress.receiverPostal = place.address_components[i]['long_name'];
            }
        }
        receiverAddress.receiverAddress = place.formatted_address;
        vm.getReceiverAddress(receiverAddress);        
    });
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var geolocation = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        var circle = new google.maps.Circle({
            center: geolocation,
            radius: position.coords.accuracy
        });
        autocomplete.setBounds(circle.getBounds());
        });
    }
}




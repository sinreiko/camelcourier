const get_order_URL = "http://localhost:5000/order"
const get_activity_URL = "http://localhost:5001/activity"
const get_shipper_URL = "http://localhost:5002/shipper"
const get_rate_URL = "http://localhost:5003/rate"
const get_droppoint_URL = "http://localhost:5004/droppoint"
const valuing_URL = "http://localhost:5005/valuing"
const pick_parcel_URL = "http://localhost:5006/pickparcel"
const create_delivery_URL = "http://localhost:5007/createdelivery"
const update_delivery_URL = "http://localhost:5008/update"
const accept_delivery_URL = "http://localhost:5000/accept"

// #Order: 5000
// #Activity: 5001
// #Shipper: 5002
// #Rate: 5003
// #DropPoint: 5004
// #Valuing: 5005
// #PickParcel: 5006
// #CreateDelivery: 5007
// #UpdateDelivery: 5008
// #AcceptDelivery: 5009
// #Email: 9000
// #Sms: 5566

const app = Vue.createApp({
    data(){
        return {
            userName: localStorage.getItem("userName"),
            userType: localStorage.getItem("userType"),
            inputTracking: "",
            trackingResult: [],
            userDetail: JSON.parse(localStorage.getItem("userDetail")),
            dropOff: "",
            dropPoints:{},
        };
    },
    computed: {
        calculateProgress: function(status){
            if (status == 'Order Created'){
                return 10
            } else if (status == 'Picked up' || status == 'Delayed'){
                return 50
            } else if (status == 'Completed'){
                return 100
            }
        },
    },
    methods: {
        trackParcel(){
            var tracking_arr = []
            if (this.inputTracking != ""){
                if (this.inputTracking.includes(",")){
                    tracking_arr = this.inputTracking.split(",")
                } else if (this.inputTracking.includes(" ")){
                    tracking_arr = this.inputTracking.split(" ")
                } else {
                    tracking_arr.push(this.inputTracking);
                }
                console.log(tracking_arr);
                const response =
                fetch(`${get_activity_URL}/${tracking_arr}`)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        // no book in db
                        this.message = data.message;
                    } else {
                        res = data.data;
                        console.log(res[res.length - 1]);
                        latestStatus = res[res.length - 1].delivery_status;
                        this.trackingResult.push({
                            tracking_id: res.tracking_id,
                            latest_status: latestStatus,
                            progress: this.calculateProgress(latestStatus),
                            activities: res
                        });
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    console.log(this.message + error);

                    });
            } else {
                alert("Please insert a tracking number.")
            }
            
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
                return false;
            })
        },
        getDropPoints(){
            const response =
                fetch(`${get_droppoint_URL}`)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        // no book in db
                        this.message = data.message;
                    } else {
                        res = data.data;
                        console.log(res)
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    console.log(this.message + error);

                });
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
                            <div class="form-group col-sm-6 col-md-4">
                                <label for="email" class="sr-only">Email address</label>
                                <input v-model="userEmail" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">
                            </div>
                            <div class="form-group col-sm-6 col-md-4">
                                <label for="password" class="sr-only">Password</label>
                                <input v-model="userPassword" type="password" class="form-control" id="password" aria-describedby="emailHelp" placeholder="Enter password">
                            </div>
                            <div class="form-group col-sm-6 col-md-3 mt-md-2">
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
                    }
                })
        }
    },
    methods:{
        userAuthenticate (formType) {
            if (this.userEmail != "" || this.userPassword != ""){
                if (this.userEmail == this.driverLogin.email && this.userPassword == this.driverLogin.password){
                    localStorage.setItem("userName", this.driverLogin.name)
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
                            <a class="nav-link" href="delivery-history.html">Delivery History</a>
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
    props: ['deliverydesc','timestamp','deliverystatus'],
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
    <select class="form-select" name="dropOff">
        <option v-for="dp in dropPoints" :value="dp">{{dp}}</option>
    </select>
    `
})
const vm = app.mount('#app'); 
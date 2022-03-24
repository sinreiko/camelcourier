const auth = "http://localhost:5000/auth"
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

//  #Order: 5000
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
        
        };
    },
    methods: {
        
            // const response =
            //     fetch(auth).then(response => response.json()).then(data => {
            //         console.log(response);
            //         if (data.code === 404){
            //             this.message = data.message
            //         } else {
            //             this.userType = data.data.userType;
            //         }
            //     })
            //     .catch(error => {
            //         console.log(this.message + error)
            //     })
        },
        beforeMounted(){
            if (localStorage.userName || localStorage.userType){
                this.userName = localStorage.userName
                this.userType = localStorage.userType
            }
        }
})
app.component('home-header',{
    data(){
        return{
            driverLogin:{
                name: "Jun Hui 💩",
                email: "driver@driver.com",
                password: "driver123",
                type: "driver"
            },
            shipperLogin:{
                name: "Po Chien",
                email: "shipper@shipper.com",
                password: "shipper123",
                type: "shipper"
            },
            userEmail: "",
            userPassword: "",
            userType: "",
        }
    }, 
    methods:{
        userAuthenticate (formType) {
            if (this.userEmail != "" || this.userPassword != ""){
                if (this.userEmail == this.driverLogin.email && this.userPassword == this.driverLogin.password){
                    localStorage.setItem("userName", this.driverLogin.name)
                    localStorage.setItem("userType", this.driverLogin.type)
                    form = document.getElementById(formType)
                    form.action = "pickup.html"
                    form.submit()
                } else if (this.userEmail == this.shipperLogin.email && this.userPassword == this.shipperLogin.password){
                    localStorage.setItem("userName", this.shipperLogin.name)
                    localStorage.setItem("userType", this.shipperLogin.type)
                    form = document.getElementById(formType)
                    form.action = "create-delivery.html"
                    form.submit()
                } else {
                    alert("Email and/or password is incorrect. Please try again.")
                }
            } else {
                alert("Email and/or password is empty. Please fill in.")
            }
        }
    },
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
            
        <!-- </div> -->
    </header>`
})

app.component('driver-header',{
    data(){
        return{

        }
    }, 
    methods: {

    },
    props: ['user'],
    // template: `<div>{{}}</div>`
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
                    Welcome, {{user}}
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
    props: ['user'],
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
                    Welcome, {{user}}
                </span>
            </nav>
        </div>
    </header>`
});

const vm = app.mount('#app'); 
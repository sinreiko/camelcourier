const auth = "http://localhost:5000/auth"

const app = Vue.createApp({
    data(){
        return {
            email: "",
            password: "",
            message: "There is a problem authenticating user, please try again later.",
            userName: "",
            userType: "",
        };
    },
    methods: {
        authenticate () {
            const response =
                fetch(auth).then(response => response.json()).then(data => {
                    console.log(response);
                    if (data.code === 404){
                        this.message = data.message
                    } else {
                        this.userType = data.data.userType;
                    }
                })
                .catch(error => {
                    console.log(this.message + error)
                })
        }
    }
})
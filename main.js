
function setFormMessages(formElement,type,message){
    const messageElement=formElement.querySelector(".form_Message");

    messageElement.textContent=message;
    messageElement.classList.remove('form_Message_Success','form_Message_Error')    
    messageElement.classList.add(`form_Message_${type}`)    
}

// setFormMessages(loginForm,"success","you're logged in!");
function setInputError(inputElement,message){
    inputElement.classList.add("form_Input_error");
    inputElement.parentElement.querySelector('.form_Input_Error_Message').textContent=message;
}
function removeInputError(inputElement){
    inputElement.classList.remove("form_input_Error");
    // console.log(inputElement)
    inputElement.parentElement.querySelector('.form_Input_Error_Message').textContent='';

}


document.addEventListener('DOMContentLoaded',()=>{
    const loginForm=document.querySelector('#user_login');
    const createAccountForm=document.querySelector("#create_Account");

    document.querySelector('#linkCreateAccount').addEventListener("click",e=>{
        e.preventDefault();
        loginForm.classList.add("form_Hidden");
        createAccountForm.classList.remove("form_Hidden");
    });

    document.querySelector('#linkLoginAccount').addEventListener("click",e=>{
        e.preventDefault();
        loginForm.classList.remove("form_Hidden");
        createAccountForm.classList.add("form_Hidden");
    });

    loginForm.addEventListener("submit",e=>{
        e.preventDefault();
        // const x=require('child_process').spawn;
        // const data="Hi";
        // console.log("data set to python script");
        // const python_progress=x('python',['./python.py',JSON.stringify(data)]);
        // python_progress.stdout.on('data',data=>{
        //     console.log("data received from python script:", data.toString())

        // })
        
        let usernames={
            'name':'priyanka',
            'type':"login details"
        }
        const request= new XMLHttpRequest();
        request.open('POST',`/processUserInfo/${JSON.stringify(usernames)}`)
        request.onload=()=>{
            const flaskmessage=request.responseText
            console.log(flaskmessage)
        }
        request.send()

        setFormMessages(loginForm,"success","you're logged in!");
    });

    document.querySelectorAll(".form_Input").forEach(inputElement=>{
        inputElement.addEventListener("blur",e=>{
            e.preventDefault();
            if(e.target.id === "singupUsername" && e.target.value.length >0 && e.target.value.length < 8){
                setInputError(inputElement,"username must be at least 8 characters in length")
            }
        });
        inputElement.addEventListener("input",e=>{
            removeInputError(inputElement);
        });
    });
});
import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';

const responseGoogle = (response) => {
};
 

function handleSubmit(response) {


    let name = response.profileObj.name;
    let profilepic=response.profileObj.imageUrl;
    Socket.emit('new google user', {
        'name': name,
        'profilepic':profilepic
    });
    
}

export function GoogleButton() {
return<GoogleLogin
    clientId="835080147796-gcu3obt8c86gfqvbo27aueegc80fub7p.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={handleSubmit}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
  />;
}
